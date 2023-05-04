import qrcode

from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


datos = input('Que quiere generar en qr: ')
qr.clear()
qr.add_data(datos)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f'11. Crear y leer QR/CodigosQR/{datos}.png')












