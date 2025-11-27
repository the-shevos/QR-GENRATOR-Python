import qrcode

def main():
    url_or_text = input("Enter the URL or text for the QR code: ").strip()
    if not url_or_text:
        print("Error: Input cannot be empty!")
        return

    file_path = input("Enter filename (with .png, default 'qrcode.png'): ").strip() or "qrcode.png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url_or_text)
    qr.make(fit=True)

    fill_color = input("Enter QR code color (default 'black'): ").strip() or "black"
    back_color = input("Enter background color (default 'white'): ").strip() or "white"

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    try:
        img.save(file_path)
        print(f"QR Code successfully generated and saved as '{file_path}'!")
    except Exception as e:
        print(f"Error saving QR code: {e}")

if __name__ == "__main__":
    main()
