# Changelog

All notable changes to QRiftly will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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