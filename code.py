import qrcode

data = "codeveilstudio.vercel.app"

qr = qrcode.make(data)
qr.save("qr_codeveil.png")
