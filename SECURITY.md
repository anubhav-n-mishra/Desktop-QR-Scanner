# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Features

QRiftly implements several security measures:

### 🛡️ Input Validation
- QR code data length limits (2000 characters max)
- File size restrictions (50MB max)
- Image format validation
- SSID and password length validation

### 🔒 Secure File Handling
- Temporary file cleanup with overwriting
- File permission restrictions
- Path validation and sanitization

### 🌐 Network Security
- No shell injection in WiFi commands
- Command timeout protection
- Input sanitization for XML profiles
- Secure temporary file naming

### 🚫 Privacy Protection
- No data collection or transmission
- No password storage
- Local-only processing
- Automatic credential cleanup

## Reporting a Vulnerability

If you discover a security vulnerability in QRiftly, please report it responsibly:

### 📧 Contact
- **Email**: [Security contact information]
- **Subject**: "QRiftly Security Issue"

### 📋 What to Include
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested fix (if any)

### ⏱️ Response Timeline
- **Initial Response**: Within 48 hours
- **Investigation**: 1-7 days depending on complexity
- **Fix Development**: 1-14 days
- **Public Disclosure**: After fix is released

### 🔄 Process
1. Report received and acknowledged
2. Vulnerability verified and assessed
3. Fix developed and tested
4. Security update released
5. Public disclosure with credit

## Security Best Practices

### For Users
- Download QRiftly only from official sources
- Run with standard user privileges when possible
- Keep Windows updated
- Be cautious with QR codes from untrusted sources

### For Developers
- Follow secure coding practices
- Validate all inputs
- Use parameterized commands
- Implement proper error handling
- Regularly update dependencies

## Known Security Considerations

### WiFi Connection Feature
- Requires elevated privileges for network profile creation
- Creates temporary XML files (automatically cleaned up)
- Uses Windows netsh command with validated parameters

### File Processing
- Large images are automatically resized
- File types are validated before processing
- Binary data is safely handled with encoding fallbacks

### Camera Access
- Standard system camera permissions apply
- No video recording or image saving
- Real-time processing only

## Security Updates

Security updates will be:
- Released as soon as possible
- Clearly marked in release notes
- Accompanied by migration guides if needed
- Communicated through GitHub releases

## Third-Party Dependencies

QRiftly uses these security-relevant dependencies:
- **OpenCV**: Computer vision (trusted, widely used)
- **pyzbar**: QR decoding (open source, audited)
- **Pillow**: Image processing (actively maintained)
- **PyAutoGUI**: Screenshot capture (standard library)

Dependencies are regularly updated to address security issues.

---

## Disclaimer

QRiftly is provided "as is" without warranty. Users are responsible for:
- Verifying QR code sources
- Understanding network security implications
- Following organizational security policies
- Regular software updates

For enterprise use, consider additional security assessments and policies.