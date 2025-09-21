# WiFi QR Code Auto-Connect Guide

## How WiFi QR Codes Work

WiFi QR codes contain network connection information in a standardized format:
```
WIFI:T:WPA;S:NetworkName;P:Password;H:false;;
```

Where:
- `T` = Security type (WPA, WEP, or empty for open)
- `S` = Network name (SSID)
- `P` = Password (empty for open networks)
- `H` = Hidden network (true/false)

## Using the WiFi Auto-Connect Feature

1. **Scan a WiFi QR Code**: Use any scanning method (screenshot, file, or camera)
2. **Detect WiFi Configuration**: The app automatically detects WiFi QR codes
3. **Connect Button Appears**: A "📶 Connect WiFi" button will appear
4. **Confirm Connection**: Click the button and confirm the connection prompt
5. **Automatic Connection**: Windows will connect to the network automatically

## Supported Security Types

- **WPA/WPA2**: Most common modern networks
- **WEP**: Legacy networks (older security)
- **Open**: No password required
- **Hidden Networks**: Networks that don't broadcast their name

## Requirements for WiFi Connection

- **Administrator Privileges**: May be required for network profile creation
- **Windows 7 or higher**: Uses Windows `netsh` command
- **Valid WiFi Adapter**: Must have working WiFi hardware

## Creating WiFi QR Codes

You can create WiFi QR codes using:

### Online Generators
- QiFi.org
- WiFi QR Code Generator websites

### Manual Format
Use the format: `WIFI:T:WPA;S:YourNetworkName;P:YourPassword;H:false;;`

### Using Our Test Generator
Run `python create_test_qr.py` to create sample WiFi QR codes for testing.

## Troubleshooting

### Connection Fails
- Check if you have administrator privileges
- Verify the WiFi password is correct
- Ensure WiFi adapter is enabled
- Check if the network is in range

### QR Code Not Detected as WiFi
- Ensure the QR code follows the correct format
- Check for typos in the WiFi string
- Verify the QR code is clear and readable

### Profile Already Exists
- Windows may have an existing profile for the network
- The app will update the existing profile
- Manual deletion: `netsh wlan delete profile name="NetworkName"`

## Security Considerations

- ✅ **Passwords are secure**: Only used for connection, not stored
- ✅ **Local processing**: No data sent to external servers
- ✅ **Temporary files**: Profile files are automatically cleaned up
- ⚠️ **QR Code visibility**: Anyone who can see the QR code can access the network

## Example WiFi QR Codes

The test generator creates these examples:

1. **WPA2 Network**: `WIFI:T:WPA;S:TestNetwork;P:MyPassword123;H:false;;`
2. **Open Network**: `WIFI:T:;S:OpenNetwork;P:;H:false;;`
3. **Hidden Network**: `WIFI:T:WPA;S:HiddenNetwork;P:SecretPassword;H:true;;`
4. **WEP Network**: `WIFI:T:WEP;S:OldNetwork;P:1234567890;H:false;;`

## Tips for Best Results

- 📱 **Share Networks Easily**: Create QR codes for guest networks
- 🖥️ **Screenshot Sharing**: Share network access via screen sharing
- 📄 **Print QR Codes**: Create physical QR codes for easy sharing
- 🔄 **Test First**: Use test QR codes to verify functionality

---

**Note**: This feature requires Windows and appropriate permissions for network management.