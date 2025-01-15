import qrcode # pip install qrcode



def generar_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("codigo_qr.png")


data = input("Introduce la URL o texto para generar el QR: ")
generar_qr(data)
print("Código QR generado y guardado como 'codigo_qr.png'")
