# 🔍 QRiftly - Professional QR Code Scanner v2.0

<div align="center">

![QRiftly Logo](https://img.shields.io/badge/QRiftly-Professional%20QR%20Scanner%20v2.0-blue?style=for-the-badge&logo=qr-code)

**The ultimate Windows QR code scanner with popup camera, themes, and WiFi auto-connect**

[![Download](https://img.shields.io/badge/Download-v2.0%20Release-green?style=for-the-badge)](https://github.com/anubhav-n-mishra/Desktop-QR-Scanner/releases)
[![Windows](https://img.shields.io/badge/Platform-Windows%207%2B-lightgrey?style=for-the-badge&logo=windows)](https://github.com/anubhav-n-mishra/Desktop-QR-Scanner)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*Made by [Anubhav Mishra](https://github.com/anubhav-n-mishra)*

</div>

---

## 🎉 Version 2.0 - Major Update!

### 🆕 **New in v2.0**
- **🎯 Popup Camera Window** - Dedicated camera scanning with large preview
- **🎨 Light/Dark Themes** - Professional theming system with instant toggle
- **🐛 Bug Report System** - Direct GitHub Issues integration for feedback
- **⚡ Auto-Stop Camera** - Camera automatically stops after successful scan
- **📱 Enhanced UI** - Modern, responsive design with better usability

## ✨ Features

### 🔍 **Multiple Scanning Methods**
- 📸 **Screenshot Capture** - Scan QR codes directly from your screen
- 📁 **File Scanning** - Load and scan image files (PNG, JPG, BMP, etc.)
- 📷 **Live Camera Popup** - Dedicated camera window with auto-stop detection

### 🎨 **Theming & Customization**
- 🌙 **Dark Theme** - Modern dark interface (default)
- ☀️ **Light Theme** - Clean, professional light interface
- ⌨️ **Quick Toggle** - Ctrl+T to instantly switch themes
- 🎯 **Complete Theming** - All windows and dialogs adapt to selected theme

### 📶 **Smart WiFi Integration**
- 🔗 **One-Click WiFi Connection** - Automatically connect to WiFi networks
- 🔐 **All Security Types** - WPA/WPA2, WEP, Open, and Hidden networks
- 🛡️ **Secure Processing** - No password storage, Windows-native integration

### 🎯 **Intelligent Actions**
- 🌐 **URL Auto-Opening** - Direct browser launch for website QR codes
- 📧 **Email Integration** - Launch email client for mailto links
- 📞 **Phone Dialing** - Detect and handle phone numbers
- 📋 **Clipboard Support** - One-click copy to clipboard

### 🔒 **Security & Privacy**
- 🏠 **100% Offline** - Works completely without internet
- 🛡️ **Secure Processing** - Input validation and secure file handling
- 🔐 **No Data Collection** - All processing happens locally
- 🧹 **Clean Cleanup** - Automatic temporary file removal

---

### 🎯 **Enhanced Camera Experience (v2.0)**
- **📱 Popup Window** - Dedicated camera window with large preview area
- **⚡ Auto-Stop** - Camera automatically stops after successful QR detection
- **🔄 Real-time Status** - Live scanning status and detection feedback
- **🎨 Theme Aware** - Camera window matches your selected theme
- **🖥️ Flexible Layout** - Resizable and moveable camera window

### � **User Support & Feedback**
- **🐛 Bug Report System** - Easy bug reporting directly to GitHub Issues
- **📝 Pre-filled Templates** - Structured bug reports with environment info
- **🔗 Direct Integration** - One-click access to project issues page
- **💬 Community Support** - Active development and user feedback

## �🚀 Quick Start

### 📥 Download & Install

#### Option 1: Download Executable (Recommended)
1. Go to [Releases](https://github.com/anubhav-n-mishra/Desktop-QR-Scanner/releases)
2. Download `QRiftly-v2.0.exe`
3. Run the executable - no installation needed!

#### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/anubhav-n-mishra/Desktop-QR-Scanner.git
cd Desktop-QR-Scanner

# Install dependencies
pip install -r requirements.txt

# Run the application
python qr_scanner.py
```

---

## 📖 How to Use

### 1. 📸 Screenshot Scanning
1. Click **"📷 Scan Screen"**
2. Application window minimizes
3. Screenshot is captured and analyzed
4. Results appear instantly!

### 2. 📁 File Scanning
1. Click **"📁 Scan File"**
2. Select your image file
3. QR codes are detected and decoded
4. Results display with action buttons

### 3. 📷 Live Camera Scanning
1. Click **"🎥 Start Camera"**
2. Point camera at QR code
3. Real-time detection with visual feedback
4. Automatic scanning every 2 seconds

### 4. 📶 WiFi Auto-Connect
1. Scan any WiFi QR code
2. **"📶 Connect WiFi"** button appears
3. Click to see network details
4. Confirm to connect automatically

---

## 🎯 Supported QR Code Types

| Type | Example | Action |
|------|---------|--------|
| 🌐 **URL** | `https://github.com` | Opens in browser |
| 📶 **WiFi** | `WIFI:T:WPA;S:MyNet;P:Pass123;;` | Auto-connects |
| 📧 **Email** | `mailto:user@example.com` | Opens email client |
| 📞 **Phone** | `tel:+1234567890` | Shows dial option |
| 📍 **Location** | `geo:37.7749,-122.4194` | Shows coordinates |
| 📄 **Text** | Any text content | Displays and copies |

---

## 🔧 Technical Requirements

### 💻 **System Requirements**
- **OS**: Windows 7 or higher
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 50MB free space
- **Camera**: Optional for webcam scanning

### 📦 **Dependencies** (for source installation)
```
opencv-python >= 4.8.0
pyzbar >= 0.1.9
Pillow >= 10.0.0
pyautogui >= 0.9.50
numpy >= 1.24.0
```

---

## 🏗️ Building from Source

### 🔨 **Create Executable**
```bash
# Install build dependencies
pip install pyinstaller

# Build standalone executable
pyinstaller qr_scanner.spec

# Executable will be in: dist/QRiftly.exe
```

### 🧪 **Development Setup**
```bash
# Clone repository
git clone https://github.com/anubhav-n-mishra/Desktop-QR-Scanner.git
cd Desktop-QR-Scanner

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python qr_scanner.py
```

---

## 🐛 Troubleshooting

### ❓ **Common Issues**

**Camera not working?**
- Check if camera is being used by another application
- Verify camera permissions in Windows settings
- Try disconnecting and reconnecting USB cameras

**WiFi connection fails?**
- Run as administrator for network profile creation
- Check if network is in range
- Verify QR code contains correct WiFi format

**QR codes not detected?**
- Ensure QR code is clear and well-lit
- Try adjusting camera distance
- Check if image file is not corrupted

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### 🎯 **Ways to Contribute**
- 🐛 **Bug Reports** - Found an issue? Let us know!
- 💡 **Feature Requests** - Have an idea? Share it!
- 🔧 **Code Contributions** - Submit pull requests
- 📚 **Documentation** - Help improve our docs

### 📋 **Development Guidelines**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by [Anubhav Mishra](https://github.com/anubhav-n-mishra)**

*If you find QRiftly useful, please consider giving it a ⭐!*

</div>