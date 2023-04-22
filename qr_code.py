import qrcode

# Get user data
user_data = input("Enter data to encode as QR code: ")

# Create a QR code object
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Add user data to the QR code object
qr.add_data(user_data)
qr.make(fit=True)

# Create an image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save(f"{user_data}.png")

# Print a message to the console
print(f"QR code for '{user_data}' saved to '{user_data}.png'")
