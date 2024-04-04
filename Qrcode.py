
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr=qrcode.make("https://github.com/Yash-vardhan3/Python-projects/upload")
myqr.save("myqr.png",sacle=5)
b=decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
