# Changelog

All notable changes to QRiftly will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-09-22

### 🎉 Major Release - Camera Popup & Theming

### Added
- **🎯 Popup Camera Window**: Dedicated camera scanning window with large preview area
- **🎨 Theme Toggle**: Complete light/dark theme system with professional styling
- **🐛 Bug Report System**: Integrated GitHub Issues reporting with pre-filled templates
- **⚡ Auto-Stop Camera**: Camera automatically stops after successful QR code detection
- **🎮 Enhanced UX**: Improved user interface with better visual feedback
- **⌨️ New Shortcuts**: Ctrl+T for theme toggle, enhanced keyboard navigation
- **📱 Responsive Design**: Better layout adaptation for different screen sizes

### Improved
- **📹 Camera Experience**: Large, dedicated camera window with real-time status
- **🎨 Visual Design**: Professional light/dark themes with consistent styling
- **🔄 User Workflow**: One-click scan → auto-stop → view results workflow
- **🛠️ Accessibility**: High contrast themes and better readability
- **📋 Menu System**: Added theme and bug report options to menus
- **💫 Performance**: Optimized camera operations and UI responsiveness

### Technical
- **🏗️ Architecture**: Modular theme system with complete UI adaptation
- **🎯 Camera Logic**: Improved camera handling with popup window management
- **🔧 Error Handling**: Enhanced error handling for camera and UI operations
- **📦 Code Quality**: Cleaner code organization and better separation of concerns
- **🎨 Styling**: Comprehensive theming system affecting all UI components
- **🔗 Integration**: Direct GitHub Issues integration for bug reporting

### User Experience
- **🚀 One-Click Scanning**: Camera opens → detects QR → auto-stops → shows result
- **🎨 Personalization**: Choose between light and dark themes instantly
- **🐛 Easy Feedback**: Simple bug reporting directly to GitHub Issues
- **📱 Modern Interface**: Clean, professional design with intuitive controls
- **⚡ Efficient Workflow**: Minimal clicks needed for common tasks
- **🔄 Seamless Operation**: Smooth transitions and responsive interactions

## [1.1.2] - 2025-09-22

### Fixed
- **CAMERA FUNCTIONALITY**: Restored camera feature that was broken after v1.1.1 cleanup fix
- **Missing Import**: Added ImageTk import required for proper camera display
- **Display Method**: Fixed PhotoImage creation for camera frames using ImageTk.PhotoImage
- **Camera Preview**: Improved camera preview resolution to 400x300 for better visibility

### Technical  
- Updated PIL imports to include ImageTk for tkinter camera integration
- Fixed camera frame display method for proper real-time preview
- Enhanced camera preview quality while maintaining performance
- Preserved all safety improvements and bug fixes from v1.1.1

### User Experience
- Live camera QR scanning now works perfectly
- Camera preview displays correctly without errors
- Real-time QR detection fully functional
- All three scanning methods (screenshot, file, camera) working

## [1.1.1] - 2025-09-22

### Fixed
- **CRITICAL BUG**: Resolved "invalid command name" error when closing the application
- **Camera Cleanup**: Fixed tkinter widget reference errors during app shutdown
- **Thread Management**: Improved camera thread cleanup and synchronization
- **Window Close**: Added proper WM_DELETE_WINDOW protocol handler for clean shutdown

### Technical
- Enhanced widget existence checking before tkinter operations
- Added safe error handling for widget destruction scenarios
- Improved camera loop with proper shutdown detection
- Better exception handling for TclError during cleanup

### User Experience
- App now closes cleanly without error popups
- No more annoying error dialogs on exit
- Smoother shutdown process for better user experience

## [1.1.0] - 2025-09-22

### Added
- **Brand New Logo**: Beautiful QRiftly logo now displayed as app icon and window icon
- **Menu Bar**: Complete menu system with File, Tools, and Help menus
- **Keyboard Shortcuts**: Quick access via keyboard shortcuts (Ctrl+S, Ctrl+O, etc.)
- **Desktop Shortcuts**: Create desktop shortcuts for quick access via Tools menu
- **Taskbar Integration**: Instructions and tools for pinning to taskbar
- **About Dialog**: Professional about dialog with app information

### Enhanced
- **User Experience**: Professional branded interface with custom icon
- **Accessibility**: Full keyboard navigation support
- **Convenience**: Easy access to app functionality via shortcuts and menu
- **Branding**: Consistent QRiftly logo throughout the application

### Technical
- Updated PyInstaller configuration to embed custom icon
- Added icon generation from PNG logo for cross-platform compatibility
- Enhanced build process with proper asset inclusion

## [1.0.1] - 2025-09-22

### Fixed
- **Critical Bug Fix**: Resolved `libzbar.dll` missing error in Windows executable
- Added required DLL files (`libzbar-64.dll` and `libiconv.dll`) to PyInstaller build
- Updated GitHub Actions workflow to include DLL dependencies
- QR scanning now works properly in standalone executable

### Technical
- Created custom PyInstaller spec file for proper binary inclusion
- Enhanced build process for better Windows compatibility
- Improved CI/CD pipeline with DLL management

## [1.0.0] - 2025-09-21

### Added
- 🎉 **Initial Release** - QRiftly Professional QR Code Scanner
- 📸 **Screenshot Scanning** - Capture and scan QR codes from screen
- 📁 **File Scanning** - Support for PNG, JPG, BMP, GIF, TIFF image files
- 📷 **Live Camera Scanning** - Real-time QR code detection with webcam
- 📶 **WiFi Auto-Connect** - One-click WiFi network connection
- 🌐 **URL Auto-Opening** - Direct browser launch for website QR codes
- 📧 **Email Integration** - Launch email client for mailto links
- 📋 **Clipboard Support** - Copy scan results to clipboard
- 🔒 **Security Features** - Input validation and secure file handling
- 🎨 **Professional UI** - Clean, modern interface with branding
- 📱 **Multi-format Support** - Handle various QR code types intelligently

### Security
- Input validation for all user data
- File size and type restrictions
- Secure WiFi profile handling
- Automatic temporary file cleanup
- No data collection or transmission

### Supported QR Code Types
- URLs (http/https)
- WiFi networks (WPA/WPA2, WEP, Open, Hidden)
- Email addresses (mailto)
- Phone numbers (tel)
- Geographic locations (geo)
- Plain text content

### Technical Features
- Windows 7+ compatibility
- Offline operation
- Lightweight executable
- Error handling and recovery
- Performance optimizations

---

## Development Notes

### Version History
- **v1.0.0** - Production release with full feature set
- **v0.9.x** - Beta testing and security hardening
- **v0.8.x** - WiFi integration development
- **v0.7.x** - Multi-source scanning implementation
- **v0.6.x** - Initial prototype and core features

### Future Roadmap
- Mobile QR code generation
- Batch file processing
- Custom QR code creation
- Network share scanning
- Additional security enhancements

---

**Note**: This is the initial production release. Previous development versions were not publicly released.