import requests
from PIL import Image
from io import BytesIO
import base64
import os

# Hinweis: Da wir das Bild nicht direkt aus dem Chat herunterladen können,
# müssen wir einen Platzhalter erstellen und den Benutzer anweisen,
# das Bild manuell zu ersetzen.

print("Bitte speichern Sie den neuen QR-Code als 'qr_code.png' im Hauptverzeichnis.")
print("Der vorhandene QR-Code wird durch den neuen ersetzt, wenn Sie ihn manuell speichern.")

# Überprüfen, ob der QR-Code bereits existiert
if os.path.exists("qr_code.png"):
    print("Die Datei 'qr_code.png' existiert bereits.")
    print("Bitte ersetzen Sie diese Datei manuell mit dem neuen QR-Code.")
else:
    print("Die Datei 'qr_code.png' existiert nicht.")
    print("Bitte speichern Sie den neuen QR-Code als 'qr_code.png' im Hauptverzeichnis.")
