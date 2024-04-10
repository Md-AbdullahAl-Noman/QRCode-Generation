import qrcode
from PIL import Image

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://github.com/Md-AbdullahAl-Noman")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue").convert('RGB')

# Load logo
logo_image = Image.open("noman.jpg").convert("RGBA")
logo_size = 55  
logo_image = logo_image.resize((logo_size, logo_size))

alpha_mask = Image.new("L", logo_image.size, 250)  #opacity
logo_image.putalpha(alpha_mask)


qr_size = img.size
logo_pos = ((qr_size[0] - logo_size) // 2, (qr_size[1] - logo_size) // 2)

img = img.convert("RGBA")


img.paste(logo_image, logo_pos, logo_image)

img = img.convert("RGB")


img.save("GithubLinkWithLogo.png")
