import cv2
import numpy as np
from pyzbar import pyzbar
from PIL import Image
import pyautogui
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import time
import webbrowser
from typing import List, Tuple, Optional
import os
import sys
import subprocess
import re
import xml.etree.ElementTree as ET
from urllib.parse import unquote


class QRiftlyScanner:
    """
    QRiftly - Professional QR Code Scanner
    A comprehensive QR code scanner that supports multiple input methods:
    - Screenshot capture (full screen or selection)
    - Image file scanning
    - Live webcam detection
    - WiFi auto-connect functionality
    
    Made by Anubhav Mishra
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui()
        self.camera = None
        self.camera_running = False
        self.camera_thread = None
        
    def setup_ui(self):
        """Initialize the main user interface with responsive modern styling"""
        self.root.title("QRiftly - Professional QR Scanner")
        
        # Get screen dimensions for responsive sizing
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set responsive window size (80% of screen, but with limits)
        window_width = min(1200, max(900, int(screen_width * 0.8)))
        window_height = min(900, max(700, int(screen_height * 0.8)))
        
        # Center window on screen
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.minsize(900, 700)
        
        # Make window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Set window icon (using our logo)
        try:
            # Try to use our custom icon
            if os.path.exists("qriftly_icon.ico"):
                self.root.iconbitmap("qriftly_icon.ico")
            elif os.path.exists("logo.png"):
                # Fallback to PNG if ICO not available
                icon_img = tk.PhotoImage(file="logo.png")
                self.root.iconphoto(True, icon_img)
        except Exception as e:
            print(f"Could not set icon: {e}")
            pass
        
        # Configure modern theme with proper button styling
        style = ttk.Style()
        
        # Use a reliable theme
        try:
            style.theme_use('clam')  # This theme works well across platforms
        except:
            pass
        
        # Configure vibrant styles that actually work
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 24, 'bold'), 
                       foreground='#667eea')
        
        style.configure('Subtitle.TLabel', 
                       font=('Segoe UI', 12), 
                       foreground='#4a90e2')
        
        style.configure('Credit.TLabel', 
                       font=('Segoe UI', 10), 
                       foreground='#fd79a8')
        
        style.configure('Status.TLabel', 
                       font=('Segoe UI', 11, 'bold'), 
                       foreground='#00b894')
        
        # Fix button styles - use colors that work with clam theme
        style.configure('Action.TButton', 
                       font=('Segoe UI', 11, 'bold'),
                       padding=(15, 10))
        
        style.map('Action.TButton',
                 background=[('active', '#e8f4fd'),
                            ('pressed', '#cce7f0')])
        
        style.configure('Primary.TButton', 
                       font=('Segoe UI', 10, 'bold'),
                       padding=(12, 6))
        
        style.map('Primary.TButton',
                 background=[('active', '#e8f4fd'),
                            ('pressed', '#cce7f0')])
        
        style.configure('Secondary.TButton', 
                       font=('Segoe UI', 10),
                       padding=(12, 6))
        
        style.map('Secondary.TButton',
                 background=[('active', '#f0f0f0'),
                            ('pressed', '#e0e0e0')])
        
        # Set window background
        self.root.configure(bg='#f8f9fa')
        
        # Create menu bar
        self.create_menu_bar()
        
        # Simple, reliable main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header section
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title and subtitle
        title_label = ttk.Label(header_frame, text="🚀 QRiftly", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, 
                                  text="✨ Professional QR Code Scanner with WiFi Auto-Connect ✨", 
                                  style='Subtitle.TLabel')
        subtitle_label.pack(pady=(5, 0))
        
        credit_label = ttk.Label(header_frame, text="Made with 💜 by Anubhav Mishra", 
                               style='Credit.TLabel')
        credit_label.pack(pady=(5, 0))
        
        # Scanning methods section
        scan_frame = ttk.LabelFrame(main_frame, text="🎯 Choose Your Scanning Method", padding="15")
        scan_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Button container with proper grid
        button_container = ttk.Frame(scan_frame)
        button_container.pack(fill=tk.X)
        
        # Configure columns for responsive layout
        for i in range(3):
            button_container.columnconfigure(i, weight=1, minsize=200)
        
        # Scan buttons with fixed styling
        self.screenshot_btn = ttk.Button(button_container, 
                                       text="📸 Capture Screen\n🖥️ Screenshot QR", 
                                       command=self.scan_screenshot, 
                                       style='Action.TButton')
        self.screenshot_btn.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        
        self.file_btn = ttk.Button(button_container, 
                                 text="📂 Load Image\n🖼️ From File", 
                                 command=self.scan_file, 
                                 style='Action.TButton')
        self.file_btn.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
        
        self.camera_btn = ttk.Button(button_container, 
                                   text="📹 Live Camera\n📱 Real-time Scan", 
                                   command=self.toggle_camera, 
                                   style='Action.TButton')
        self.camera_btn.grid(row=0, column=2, padx=5, pady=10, sticky="ew")
        
        # Status section
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(0, 15))
        
        status_icon = ttk.Label(status_frame, text="⚡", font=('Segoe UI', 14))
        status_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        self.status_label = ttk.Label(status_frame, text="🚀 Ready to scan amazing QR codes...", 
                                    style='Status.TLabel')
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var, 
                                          length=100, mode='indeterminate')
        self.progress_bar.pack(side=tk.RIGHT)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="🎉 Scan Results & Quick Actions", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame, 
            height=12, 
            width=70,
            font=('Consolas', 10),
            wrap=tk.WORD,
            bg='#f8f9fa',
            fg='#2d3436'
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Action buttons
        buttons_frame = ttk.Frame(results_frame)
        buttons_frame.pack(fill=tk.X)
        
        self.copy_btn = ttk.Button(buttons_frame, text="📋 Copy All", 
                                 command=self.copy_results, state='disabled',
                                 style='Primary.TButton')
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.open_url_btn = ttk.Button(buttons_frame, text="🌐 Open URL", 
                                     command=self.open_url, state='disabled',
                                     style='Primary.TButton')
        self.open_url_btn.pack(side=tk.LEFT, padx=5)
        
        self.connect_wifi_btn = ttk.Button(buttons_frame, text="📶 Connect WiFi", 
                                         command=self.connect_wifi, state='disabled',
                                         style='Primary.TButton')
        self.connect_wifi_btn.pack(side=tk.LEFT, padx=5)
        
        self.help_btn = ttk.Button(buttons_frame, text="❓ Help", 
                                 command=self.show_help, 
                                 style='Secondary.TButton')
        self.help_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        self.clear_btn = ttk.Button(buttons_frame, text="🗑️ Clear", 
                                  command=self.clear_results,
                                  style='Secondary.TButton')
        self.clear_btn.pack(side=tk.RIGHT, padx=5)
        
        # Camera preview frame (hidden initially)
        self.camera_frame = ttk.LabelFrame(main_frame, text="📹 Live Camera Preview", padding="15")
        self.camera_label = ttk.Label(self.camera_frame, 
                                     text="📷 Camera feed will appear here\nPoint camera at QR codes for automatic detection",
                                     font=('Segoe UI', 11),
                                     foreground='#7f8c8d',
                                     justify='center')
        self.camera_label.pack(pady=20)
        
        # Store last scan result for actions
        self.last_qr_data = ""
        self.last_wifi_config = None
        
    def update_status(self, message: str, show_progress: bool = False, emoji: str = "⚡"):
        """Update the status label with colorful messages and animations"""
        # Add emoji and style to status messages
        colorful_message = f"{emoji} {message}"
        self.status_label.config(text=colorful_message)
        
        if show_progress:
            self.progress_bar.start(15)  # Faster progress animation
        else:
            self.progress_bar.stop()
        
        # Auto-update the UI
        self.root.update_idletasks()
        
    def show_help(self):
        """Show help dialog with usage instructions"""
        help_text = """🚀 QRiftly - Professional QR Scanner

🔍 SCANNING METHODS:
• Screenshot: Capture your screen to scan QR codes
• File Upload: Load image files (PNG, JPG, etc.)
• Live Camera: Real-time scanning via webcam

📱 FEATURES:
• WiFi Auto-Connect: Automatically connects to WiFi networks
• Multi-format Support: URLs, WiFi, Email, Phone, Text
• Offline Operation: Works without internet connection
• Secure Processing: No data sent to external servers

💡 TIPS:
• Ensure QR codes are clear and well-lit
• For WiFi: Run as admin for best results
• Use good lighting for camera scanning
• Keep QR codes steady for detection

Made with ❤️ by Anubhav Mishra"""
        
        messagebox.showinfo("QRiftly Help", help_text)
        
    def add_result(self, qr_data: str, source: str = ""):
        """Add a QR scan result to the results area with improved formatting"""
        timestamp = time.strftime("%H:%M:%S")
        qr_type = self.detect_qr_type(qr_data)
        
        # Create formatted result with emojis and better structure
        result_text = f"🕐 {timestamp} | {source}\n"
        result_text += f"📋 Content: {qr_data}\n"
        result_text += f"🏷️  Type: {qr_type}\n"
        
        # Add type-specific information
        if qr_type == "WiFi Configuration":
            wifi_config = self.parse_wifi_qr(qr_data)
            if wifi_config:
                result_text += f"📶 Network: {wifi_config['ssid']}\n"
                result_text += f"🔐 Security: {wifi_config['security']}\n"
                result_text += f"👁️  Hidden: {'Yes' if wifi_config['hidden'] else 'No'}\n"
        elif qr_type == "URL":
            result_text += f"🌐 Ready to open in browser\n"
        elif qr_type == "Email":
            result_text += f"📧 Ready to open in email client\n"
        elif qr_type == "Phone Number":
            result_text += f"📞 Phone number detected\n"
            
        result_text += "=" * 60 + "\n\n"
        
        # Insert at beginning for newest first
        self.results_text.insert(tk.INSERT, result_text)
        self.results_text.see(tk.INSERT)
        
        # Enable buttons
        self.copy_btn.config(state='normal')
        if self.is_url(qr_data):
            self.open_url_btn.config(state='normal')
        
        # Check if it's a WiFi QR code
        wifi_config = self.parse_wifi_qr(qr_data)
        if wifi_config:
            self.connect_wifi_btn.config(state='normal')
            self.last_wifi_config = wifi_config
            
        # Store for actions
        self.last_qr_data = qr_data

    def clear_results(self):
        """Clear all scan results and reset buttons"""
        self.results_text.delete('1.0', tk.END)
        self.copy_btn.config(state='disabled')
        self.open_url_btn.config(state='disabled')
        self.connect_wifi_btn.config(state='disabled')
        self.last_qr_data = ""
        self.last_wifi_config = None
        self.update_status("Results cleared. Ready to scan QR codes...")
    
    def create_menu_bar(self):
        """Create menu bar with app shortcuts and options"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="📸 Screenshot Scan", command=self.scan_screenshot, accelerator="Ctrl+S")
        file_menu.add_command(label="📂 Open Image File", command=self.scan_file, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="🗑️ Clear Results", command=self.clear_results, accelerator="Ctrl+L")
        file_menu.add_separator()
        file_menu.add_command(label="❌ Exit", command=self.root.quit, accelerator="Alt+F4")
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="📷 Toggle Camera", command=self.toggle_camera, accelerator="Ctrl+C")
        tools_menu.add_command(label="📋 Copy All Results", command=self.copy_results, accelerator="Ctrl+A")
        tools_menu.add_separator()
        tools_menu.add_command(label="🖥️ Create Desktop Shortcut", command=self.create_desktop_shortcut)
        tools_menu.add_command(label="📌 Pin to Taskbar", command=self.pin_to_taskbar)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="❓ Help & Usage", command=self.show_help, accelerator="F1")
        help_menu.add_command(label="🌟 About QRiftly", command=self.show_about)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-s>', lambda e: self.scan_screenshot())
        self.root.bind('<Control-o>', lambda e: self.scan_file())
        self.root.bind('<Control-c>', lambda e: self.toggle_camera())
        self.root.bind('<Control-l>', lambda e: self.clear_results())
        self.root.bind('<Control-a>', lambda e: self.copy_results())
        self.root.bind('<F1>', lambda e: self.show_help())
    
    def create_desktop_shortcut(self):
        """Create a desktop shortcut for QRiftly"""
        try:
            import winshell
            desktop = winshell.desktop()
            exe_path = os.path.abspath(sys.executable) if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
            
            # Create shortcut
            shortcut_path = os.path.join(desktop, "QRiftly.lnk")
            
            # Use PowerShell to create shortcut (more reliable)
            ps_script = f'''
            $WshShell = New-Object -comObject WScript.Shell
            $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
            $Shortcut.TargetPath = "{exe_path}"
            $Shortcut.Description = "QRiftly - Professional QR Code Scanner"
            $Shortcut.WorkingDirectory = "{os.path.dirname(exe_path)}"
            $Shortcut.Save()
            '''
            
            subprocess.run(["powershell", "-Command", ps_script], check=True, capture_output=True)
            
            messagebox.showinfo("Success", "Desktop shortcut created successfully! 🖥️✅")
            self.update_status("Desktop shortcut created! 🖥️✅", emoji="🎉")
            
        except Exception as e:
            # Fallback method
            try:
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                exe_path = os.path.abspath(sys.executable) if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
                
                # Create a simple batch file shortcut
                batch_path = os.path.join(desktop, "QRiftly.bat")
                with open(batch_path, 'w') as f:
                    f.write(f'@echo off\ncd /d "{os.path.dirname(exe_path)}"\nstart "" "{exe_path}"\n')
                
                messagebox.showinfo("Success", "Desktop shortcut (batch file) created successfully! 🖥️✅")
                self.update_status("Desktop shortcut created! 🖥️✅", emoji="🎉")
                
            except Exception as e2:
                messagebox.showerror("Error", f"Failed to create desktop shortcut: {str(e2)}")
                self.update_status(f"Shortcut creation failed: {str(e2)}", emoji="❌")
    
    def pin_to_taskbar(self):
        """Show instructions for pinning to taskbar"""
        instructions = """📌 Pin QRiftly to Taskbar:

🔹 Method 1 (Windows 10/11):
   1. Right-click on the QRiftly.exe file
   2. Select "Pin to taskbar"

🔹 Method 2:
   1. Open QRiftly
   2. Right-click on the QRiftly icon in taskbar
   3. Select "Pin to taskbar"

🔹 Method 3:
   1. Create desktop shortcut first (Tools → Create Desktop Shortcut)
   2. Drag the shortcut to your taskbar

💡 Tip: Keep QRiftly running and right-click its taskbar icon to pin it!"""
        
        messagebox.showinfo("Pin to Taskbar", instructions)
        self.update_status("Taskbar pinning instructions shown! 📌", emoji="💡")
    
    def show_about(self):
        """Show about dialog with app information"""
        about_text = """🚀 QRiftly v1.0.1
Professional QR Code Scanner

✨ Features:
• Screenshot QR scanning
• File-based QR scanning  
• Live camera detection
• WiFi auto-connect
• 100% offline operation

🔒 Privacy:
• No data collection
• Local processing only
• Secure WiFi handling

💜 Made with love by Anubhav Mishra
🌟 Open source on GitHub"""
        
        messagebox.showinfo("About QRiftly", about_text)

    def copy_results(self):
        """Copy all results to clipboard"""
        content = self.results_text.get('1.0', tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.update_status("All results copied to clipboard! ✅")
        else:
            self.update_status("No results to copy")

    def scan_screenshot(self):
        """Capture screenshot and scan for QR codes with vibrant UI feedback"""
        try:
            self.update_status("Preparing magical screenshot capture...", show_progress=True, emoji="🪄")
            
            # Hide window temporarily for clean screenshot
            self.root.withdraw()
            time.sleep(0.5)  # Give time for window to hide
            
            # Take screenshot
            self.update_status("Capturing your screen in 3... 2... 1...", emoji="📸")
            screenshot = pyautogui.screenshot()
            
            # Show window again
            self.root.deiconify()
            
            self.update_status("Scanning for awesome QR codes...", show_progress=True, emoji="🔍")
            
            # Scan for QR codes
            qr_codes = self.decode_qr_codes(screenshot)
            
            self.update_status("", show_progress=False)  # Stop progress
            
            if qr_codes:
                for qr_data in qr_codes:
                    self.add_result(qr_data, "📸 Screenshot")
                self.update_status(f"Found {len(qr_codes)} QR code(s)! ✅", emoji="🎉")
            else:
                self.update_status("No QR codes found in screenshot", emoji="😕")
                
        except Exception as e:
            self.update_status(f"Screenshot error: {str(e)}", emoji="❌")
            messagebox.showerror("Error", f"Failed to capture screenshot: {str(e)}")

    def scan_file(self):
        """Open file dialog and scan selected image for QR codes"""
        try:
            file_path = filedialog.askopenfilename(
                title="Select Image File",
                filetypes=[
                    ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                    ("All files", "*.*")
                ]
            )
            
            if file_path:
                self.update_status("Loading and analyzing image...", show_progress=True, emoji="📂")
                
                # Load and scan image
                image = Image.open(file_path)
                qr_codes = self.decode_qr_codes(image)
                
                self.update_status("", show_progress=False)
                
                if qr_codes:
                    for qr_data in qr_codes:
                        self.add_result(qr_data, f"📁 File: {os.path.basename(file_path)}")
                    self.update_status(f"Found {len(qr_codes)} QR code(s)! ✅", emoji="🎉")
                else:
                    self.update_status("No QR codes found in image", emoji="😕")
                    
        except Exception as e:
            self.update_status(f"File scan error: {str(e)}", emoji="❌")
            messagebox.showerror("Error", f"Failed to scan file: {str(e)}")

    def decode_qr_codes(self, image) -> List[str]:
        """Decode QR codes from an image"""
        try:
            # Convert PIL Image to OpenCV format if needed
            if hasattr(image, 'save'):  # PIL Image
                image_np = np.array(image)
                image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            else:
                image_cv = np.array(image)
                
            # Convert to grayscale for better detection
            gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
            
            # Decode QR codes
            qr_codes = pyzbar.decode(gray)
            
            # Extract data from detected QR codes
            results = []
            for qr in qr_codes:
                try:
                    data = qr.data.decode('utf-8')
                    if data and data not in results:  # Avoid duplicates
                        results.append(data)
                except UnicodeDecodeError:
                    # Try other encodings
                    try:
                        data = qr.data.decode('latin-1')
                        if data and data not in results:
                            results.append(data)
                    except:
                        continue
                        
            return results
            
        except Exception as e:
            print(f"QR decode error: {e}")
            return []

    def detect_qr_type(self, qr_data: str) -> str:
        """Detect the type of QR code content"""
        qr_data_lower = qr_data.lower()
        
        # WiFi QR code
        if qr_data.startswith('WIFI:'):
            return "WiFi Configuration"
        
        # URL
        if any(qr_data_lower.startswith(prefix) for prefix in ['http://', 'https://', 'www.', 'ftp://']):
            return "URL"
        
        # Email
        if qr_data_lower.startswith('mailto:') or '@' in qr_data and '.' in qr_data:
            return "Email"
        
        # Phone number
        if qr_data_lower.startswith('tel:') or (qr_data.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '').isdigit() and len(qr_data.replace(' ', '').replace('-', '').replace('+', '').replace('(', '').replace(')', '')) >= 10):
            return "Phone Number"
        
        # SMS
        if qr_data_lower.startswith('sms:') or qr_data_lower.startswith('smsto:'):
            return "SMS"
        
        # Contact (vCard)
        if qr_data.upper().startswith('BEGIN:VCARD'):
            return "Contact (vCard)"
        
        # Event (vCalendar)
        if qr_data.upper().startswith('BEGIN:VEVENT'):
            return "Calendar Event"
        
        # Location/GPS
        if qr_data_lower.startswith('geo:'):
            return "Location/GPS"
        
        return "Text"

    def is_url(self, text: str) -> bool:
        """Check if text is a URL"""
        return any(text.lower().startswith(prefix) for prefix in ['http://', 'https://', 'www.', 'ftp://'])

    def parse_wifi_qr(self, qr_data: str) -> Optional[dict]:
        """Parse WiFi QR code data"""
        if not qr_data.startswith('WIFI:'):
            return None
            
        try:
            # Remove WIFI: prefix and split by semicolons
            wifi_params = qr_data[5:].split(';')
            
            config = {
                'ssid': '',
                'password': '',
                'security': 'NONE',
                'hidden': False
            }
            
            for param in wifi_params:
                if ':' in param:
                    key, value = param.split(':', 1)
                    key = key.upper()
                    
                    if key == 'S':  # SSID
                        config['ssid'] = value
                    elif key == 'P':  # Password
                        config['password'] = value
                    elif key == 'T':  # Security type
                        config['security'] = value.upper()
                    elif key == 'H':  # Hidden network
                        config['hidden'] = value.lower() == 'true'
            
            return config if config['ssid'] else None
            
        except Exception as e:
            print(f"WiFi parse error: {e}")
            return None

    def connect_wifi(self):
        """Connect to WiFi network from QR code"""
        if not self.last_wifi_config:
            messagebox.showwarning("Warning", "No WiFi configuration available")
            return
            
        try:
            self.update_status("Connecting to WiFi...", show_progress=True, emoji="📶")
            
            config = self.last_wifi_config
            ssid = config['ssid']
            password = config['password']
            security = config['security']
            
            # Create Windows WiFi profile XML
            profile_xml = self.create_wifi_profile_xml(ssid, password, security)
            
            # Save profile to temporary file
            temp_file = "temp_wifi_profile.xml"
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(profile_xml)
            
            try:
                # Add WiFi profile
                result = subprocess.run([
                    'netsh', 'wlan', 'add', 'profile', f'filename={temp_file}'
                ], capture_output=True, text=True, check=True)
                
                # Connect to network
                result = subprocess.run([
                    'netsh', 'wlan', 'connect', f'name={ssid}'
                ], capture_output=True, text=True, check=True)
                
                self.update_status(f"Successfully connected to {ssid}! ✅", emoji="🎉")
                messagebox.showinfo("Success", f"Connected to WiFi network: {ssid}")
                
            finally:
                # Clean up temporary file
                try:
                    os.remove(temp_file)
                except:
                    pass
                    
        except subprocess.CalledProcessError as e:
            error_msg = f"WiFi connection failed: {e.stderr if e.stderr else 'Unknown error'}"
            self.update_status("WiFi connection failed ❌", emoji="😞")
            messagebox.showerror("Connection Error", error_msg)
        except Exception as e:
            self.update_status(f"WiFi error: {str(e)}", emoji="❌")
            messagebox.showerror("Error", f"WiFi connection error: {str(e)}")
        finally:
            self.update_status("", show_progress=False)

    def create_wifi_profile_xml(self, ssid: str, password: str, security: str) -> str:
        """Create Windows WiFi profile XML"""
        # Escape XML special characters
        ssid_escaped = ssid.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        password_escaped = password.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        
        if security.upper() in ['WPA', 'WPA2', 'WPA2-PSK', 'WPA-PSK']:
            auth_type = "WPA2PSK"
            encryption = "AES"
        elif security.upper() == 'WEP':
            auth_type = "open"
            encryption = "WEP"
        else:  # Open network
            auth_type = "open"
            encryption = "none"
            password_escaped = ""
        
        profile_xml = f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid_escaped}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid_escaped}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>{auth_type}</authentication>
                <encryption>{encryption}</encryption>
                <useOneX>false</useOneX>
            </authEncryption>'''
        
        if password_escaped:
            profile_xml += f'''
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password_escaped}</keyMaterial>
            </sharedKey>'''
        
        profile_xml += '''
        </security>
    </MSM>
    <MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
        <enableRandomization>false</enableRandomization>
    </MacRandomization>
</WLANProfile>'''
        
        return profile_xml

    def open_url(self):
        """Open URL in default browser"""
        if self.last_qr_data and self.is_url(self.last_qr_data):
            try:
                webbrowser.open(self.last_qr_data)
                self.update_status("URL opened in browser! ✅", emoji="🌐")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open URL: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No valid URL found")

    def toggle_camera(self):
        """Toggle camera scanning on/off"""
        if self.camera_running:
            self.stop_camera()
        else:
            self.start_camera()

    def start_camera(self):
        """Start camera scanning"""
        try:
            self.update_status("Starting camera...", show_progress=True, emoji="📹")
            
            # Try to initialize camera
            self.camera = cv2.VideoCapture(0)
            if not self.camera.isOpened():
                raise Exception("Could not open camera")
            
            self.camera_running = True
            self.camera_btn.config(text="🛑 Stop Camera\n📹 Live Scanning")
            
            # Show camera frame with pack layout
            self.camera_frame.pack(fill=tk.X, pady=(0, 15))
            
            # Start camera thread
            self.camera_thread = threading.Thread(target=self.camera_loop, daemon=True)
            self.camera_thread.start()
            
            self.update_status("Camera started - point at QR codes! 📹", emoji="✅")
            
        except Exception as e:
            self.update_status("Camera start failed ❌", emoji="😞")
            messagebox.showerror("Camera Error", f"Failed to start camera: {str(e)}")
            self.camera_running = False

    def stop_camera(self):
        """Stop camera scanning"""
        self.camera_running = False
        self.camera_btn.config(text="📹 Live Camera\n📱 Real-time Scan")
        
        if self.camera:
            self.camera.release()
            self.camera = None
        
        # Hide camera frame
        self.camera_frame.pack_forget()
        
        self.update_status("Camera stopped", emoji="📴")

    def camera_loop(self):
        """Main camera scanning loop"""
        last_scan_time = 0
        scan_cooldown = 2  # Seconds between scans
        
        while self.camera_running and self.camera:
            try:
                ret, frame = self.camera.read()
                if not ret:
                    break
                
                # Update camera preview (resize for display)
                display_frame = cv2.resize(frame, (320, 240))
                frame_rgb = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                
                # Convert to PhotoImage for tkinter
                photo = tk.PhotoImage(data=img.tobytes(), format="PPM")
                
                # Update camera label in main thread
                self.root.after(0, self.update_camera_display, photo)
                
                # Scan for QR codes (with cooldown to prevent spam)
                current_time = time.time()
                if current_time - last_scan_time > scan_cooldown:
                    qr_codes = self.decode_qr_codes(frame)
                    if qr_codes:
                        for qr_data in qr_codes:
                            self.root.after(0, self.add_result, qr_data, "📹 Live Camera")
                        last_scan_time = current_time
                
                time.sleep(0.1)  # Small delay to prevent excessive CPU usage
                
            except Exception as e:
                print(f"Camera loop error: {e}")
                break

    def update_camera_display(self, photo):
        """Update camera display in main thread"""
        if self.camera_running:
            self.camera_label.config(image=photo, text="")
            self.camera_label.image = photo  # Keep a reference

    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        finally:
            self.stop_camera()


if __name__ == "__main__":
    app = QRiftlyScanner()
    app.run()