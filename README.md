# 🧠 Quiz-App "Pflegekonzepte für Praxisanleiter:innen"

Eine interaktive Quiz-App mit Streamlit für Pflegefachpersonen in der Weiterbildung zur Praxisanleitung, die auf Fragen zu pflegerischen Konzepten basiert.

## 📋 Funktionen

- Multiple-Choice-Fragen zu verschiedenen pflegerischen Konzepten
- Sofortiges Feedback nach jeder Antwort
- Fortschrittsanzeige
- Zufällige Reihenfolge der Fragen
- Ergebnisübersicht am Ende des Quiz
- Möglichkeit, das Quiz neu zu starten

## 🚀 Schnellstart

### Lokale Installation

1. Stellen Sie sicher, dass Python 3.7+ installiert ist
2. Klonen Sie dieses Repository
3. Installieren Sie die erforderlichen Pakete:
   ```
   pip install streamlit
   ```
4. Starten Sie die App:
   ```
   streamlit run app.py
   ```

### Online-Deployment

Die App kann einfach auf Streamlit Cloud oder anderen Plattformen wie Heroku, Render oder Netlify deployed werden.

#### Streamlit Cloud Deployment:

1. Erstellen Sie ein GitHub-Repository mit diesem Code
2. Melden Sie sich bei [Streamlit Cloud](https://streamlit.io/cloud) an
3. Wählen Sie "New app" und verbinden Sie Ihr Repository
4. Wählen Sie `app.py` als Hauptdatei und klicken Sie auf "Deploy"

## 📚 Inhalte

Die App enthält Fragen zu folgenden pflegerischen Konzepten:

- Basale Stimulation
- Pflegeplanung nach Regelkreis Fichter und Maier
- Problemformulierung nach PERS-Formel
- Zielformulierung nach SMART
- Validation nach Naomi Feil
- 10-Minuten-Aktivierung
- Palliative Care
- Kinaesthetics
- Realitätsorientierung (ROT)
- Pflege mit Humor
- Aromapflege
- Affolter-Modell

## 🔧 Anpassung

Sie können eigene Fragen hinzufügen, indem Sie die `questions.py` Datei bearbeiten. Jede Frage folgt diesem Format:

```python
{
    "id": "qX",
    "frage": "<Fragetext>",
    "optionen": {
        "A": "...",
        "B": "...",
        "C": "...",
        "D": "..."
    },
    "loesung": "<Buchstabe>",
    "erklaerung": "<kurze Begründung>"
}
```

## 📱 Responsive Design

Die App ist für die Nutzung auf verschiedenen Geräten optimiert, einschließlich Smartphones und Tablets.

## 🤝 Mitwirken

Beiträge, Fehlermeldungen und Verbesserungsvorschläge sind willkommen!

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
