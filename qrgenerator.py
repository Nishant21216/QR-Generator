import pyqrcode

content="we love python"

url= pyqrcode.create(content)

url.png("myqr1.png",scale=5)

print("my qr code is generated successfully")