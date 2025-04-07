import qrcode

data = "D'ont forget to subscribe to my channel!"
# img = qrcode.make(data)
qr = qrcode.QRCode(version= 1,box_size= 10,border= 5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "green", back_color = "white")


img.save("E:/Assighment-4/online-projects/QRcode2.png")




