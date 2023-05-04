
from pyzbar import pyzbar
from PIL import Image

name = input('Que quiere leer en qr: ')

image = Image.open(f'11. Crear y leer QR/CodigosQR/{name}.png')
qr_code = pyzbar.decode(image)[0]

#Convert into string

data = qr_code.data.decode('utf8').encode('shif-jis').decode('utf-8')
print('El mensaje es: ', data)