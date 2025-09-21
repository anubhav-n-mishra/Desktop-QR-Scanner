import qrcode
from PIL import Image

def create_wifi_qr_codes():
    """Create test WiFi QR codes for testing the scanner"""
    
    # WiFi configurations to test
    wifi_configs = [
        {
            'name': 'test_wifi_wpa2',
            'data': 'WIFI:T:WPA;S:TestNetwork;P:MyPassword123;H:false;;',
            'description': 'WPA2 Network'
        },
        {
            'name': 'test_wifi_open',
            'data': 'WIFI:T:;S:OpenNetwork;P:;H:false;;',
            'description': 'Open Network (No Password)'
        },
        {
            'name': 'test_wifi_hidden',
            'data': 'WIFI:T:WPA;S:HiddenNetwork;P:SecretPassword;H:true;;',
            'description': 'Hidden WPA Network'
        },
        {
            'name': 'test_wifi_wep',
            'data': 'WIFI:T:WEP;S:OldNetwork;P:1234567890;H:false;;',
            'description': 'WEP Network'
        }
    ]
    
    print("Creating WiFi QR codes for testing...")
    
    for config in wifi_configs:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(config['data'])
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        filename = f"{config['name']}.png"
        img.save(filename)
        print(f"✓ Created {filename}: {config['description']}")
        print(f"   Data: {config['data']}")
        print()

def create_mixed_test_qr_codes():
    """Create various types of QR codes for comprehensive testing"""
    
    test_data = [
        {
            'name': 'test_url',
            'data': 'https://github.com/microsoft/vscode',
            'description': 'GitHub URL'
        },
        {
            'name': 'test_email',
            'data': 'mailto:test@example.com?subject=QR%20Code%20Test&body=Hello%20from%20QR%20scanner!',
            'description': 'Email with subject and body'
        },
        {
            'name': 'test_phone',
            'data': 'tel:+1234567890',
            'description': 'Phone number'
        },
        {
            'name': 'test_text',
            'data': 'Hello World! This is a test QR code for our scanner application. It contains multiple lines of text to test the display functionality.',
            'description': 'Multi-line text'
        },
        {
            'name': 'test_location',
            'data': 'geo:37.7749,-122.4194?q=San%20Francisco',
            'description': 'Geographic location'
        }
    ]
    
    print("\nCreating mixed QR codes for testing...")
    
    for config in test_data:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(config['data'])
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        filename = f"{config['name']}.png"
        img.save(filename)
        print(f"✓ Created {filename}: {config['description']}")

if __name__ == "__main__":
    try:
        create_wifi_qr_codes()
        create_mixed_test_qr_codes()
        print("\n🎉 All test QR codes created successfully!")
        print("\nYou can now test the scanner application with these files:")
        print("- WiFi QR codes will show a 'Connect WiFi' button")
        print("- URL QR codes will show an 'Open URL' button")
        print("- All QR codes can be copied to clipboard")
        print("\nStart the scanner with: python qr_scanner.py")
        
    except ImportError:
        print("❌ qrcode library not installed.")
        print("Install with: pip install qrcode[pil]")
    except Exception as e:
        print(f"❌ Error creating test QR codes: {e}")