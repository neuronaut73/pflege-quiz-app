import qrcode

# URL der App (ersetzen Sie dies durch die tatsächliche URL Ihrer App)
app_url = "https://github.com/neuronaut73/pflege-quiz-app"

# QR-Code erstellen
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(app_url)
qr.make(fit=True)

# QR-Code als Bild speichern
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR-Code wurde als 'qr_code.png' gespeichert.")
