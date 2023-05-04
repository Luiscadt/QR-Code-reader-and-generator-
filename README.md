# QR Code Generator using Python

This Python code generates a QR code for the user input data using the qrcode and PIL libraries. The QR code contains the data entered by the user and is saved as an image file in a specified directory.

The qrcode.QRCode() function is used to create a QR code instance with the desired configuration, such as version, error correction level, box size, and border size. The user is prompted to enter the data they want to generate in the QR code.

Then, the qr.clear() method clears the QR code instance, qr.add_data() method adds the user input data, and qr.make(fit=True) method generates the QR code. The make_image() method creates a PIL image of the QR code with black fill and white background colors.

Finally, the img.save() method saves the QR code image file in the specified directory with the user input data as the file name. This code is an excellent example of how Python can be used to generate QR codes for various purposes, such as marketing, advertising, and inventory management.

## Generador de código QR con Python

Este código de Python genera un código QR para los datos ingresados por el usuario utilizando las bibliotecas qrcode y PIL. El código QR contiene los datos ingresados por el usuario y se guarda como un archivo de imagen en un directorio específico.

El código utiliza la función qrcode.QRCode() para crear una instancia de código QR con la configuración deseada, como la versión, el nivel de corrección de errores, el tamaño de la caja y el tamaño del borde. El usuario es solicitado para ingresar los datos que desea generar en el código QR.

Luego, se utiliza el método qr.clear() para borrar la instancia de código QR, el método qr.add_data() para agregar los datos ingresados por el usuario y el método qr.make(fit=True) para generar el código QR. El método make_image() crea una imagen PIL del código QR con relleno negro y fondo blanco.

Finalmente, el método img.save() guarda el archivo de imagen del código QR en el directorio especificado con los datos ingresados por el usuario como nombre del archivo. Este código es un excelente ejemplo de cómo Python se puede utilizar para generar códigos QR para diversos fines, como marketing, publicidad y gestión de inventarios.


# QR Code Reader using Python

his Python code reads a QR code image file and extracts the data encoded in it using the pyzbar and PIL libraries. The user is prompted to enter the file name of the QR code image they want to read.

Then, the Image.open() method opens the specified image file as a PIL image, and the pyzbar.decode() method decodes the QR code data from the image. The decoded data is stored in a variable qr_code.

Finally, the qr_code.data.decode() method converts the decoded data into a readable string format and prints it as output to the user. This code is an excellent example of how Python can be used to read QR codes and extract data from them. It can be useful for various applications, such as inventory management, logistics, and data tracking.

## Lector QR utilizando Python

Este código de Python utiliza las bibliotecas pyzbar y PIL para leer el contenido de un código QR en una imagen. El usuario es solicitado para ingresar el nombre del archivo de imagen QR que desea leer.

Luego, se utiliza la función Image.open() para abrir la imagen QR en formato PIL. Después, la función pyzbar.decode() se utiliza para decodificar la información del código QR desde la imagen.

El contenido decodificado del código QR se almacena en una variable, y luego se utiliza el método qr_code.data.decode() para convertir el contenido en una cadena de caracteres legible por el usuario.

Finalmente, se imprime el mensaje decodificado en la consola para que el usuario pueda leerlo.

Este código es un ejemplo práctico de cómo Python puede ser utilizado para leer y procesar códigos QR. Puede ser utilizado en una variedad de aplicaciones, como control de inventario, logística y seguimiento de datos.
