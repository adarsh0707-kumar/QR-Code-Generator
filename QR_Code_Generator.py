import qrcode 
from PIL import Image



qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, 
                   border = 4,
                   )

qr.add_data("https://www.linkedin.com/in/adarsh-kumar-657315251/")
qr.make(fit=True)

img = qr.make_image(fill_color = "#ff3", back_color="#000")


img.save("linkedin_adarsh.png")