import qrcode 

# Create a QR Code object 
qr = qrcode.QRCode( 
                   version=1, 
                   box_size=10, 
                   border=5
                   )
# Set the data to encode 
data = input("Enter the URL you want as a QR code: ") 

# Add the data to the QR Code object 
qr.add_data(data) 

# Generate the QR Code 
qr.make(fit=True) 

# Add an image file extension 
img = qr.make_image(fill_color="black", back_color="white") 

# Save the image 
img.save("qrcode.png")