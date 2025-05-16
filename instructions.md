# 🧠 Quiz-App "Pflegekonzepte für Praxisanleiter:innen" mit Streamlit & Augment

## ✅ Ziel
Eine interaktive Quiz-App mit Streamlit für Praxisanleiter:innen, die auf Fragen zu pflegerischen Konzepten basiert (inkl. Lösungen). Die Fragen werden aus einem Prompt über Augment (z. B. GPT-4 Turbo oder Claude) generiert.

---

## 🚀 Prompt für Augment (GPT-4 / Claude)

```
Du bist ein Experte für Pflegepädagogik und entwickelst Quizfragen für eine digitale Lernplattform. Zielgruppe sind ausgebildete Pflegefachkräfte, die sich zur Praxisanleitung weiterbilden. Erstelle für mich 10 Quizfragen im Multiple-Choice-Stil zu folgenden Konzepten:

- Basale Stimulation
- Pflegeplanung nach Regelkreis Fichter und Maier
- Problemformulierung nach PERS-Formel
- Zielformulierung nach SMART
- Validation nach Naomi Feil
- 10-Minuten-Aktivierung
- Palliative Care
- Kinaesthetics
- ROT (Realitätsorientierung)
- Pflege mit Humor
- Aromapflege
- Affolter-Modell

Bitte formatiere jede Frage wie folgt:

**Frage:** <Fragetext>
A) Antwort A  
B) Antwort B  
C) Antwort C  
D) Antwort D  
**Lösung:** <Buchstabe der richtigen Antwort>
**Erklärung:** <Kurze Begründung für die richtige Antwort>

Füge keine Einleitungen oder Erklärungen hinzu. Nur die 10 Fragen im oben genannten Format.
```

---

## 📋 To Do Liste – Umsetzung in Streamlit

### 🗂️ Projektstruktur
```
quiz_app/
├── app.py
├── questions.json  # exportierte Augment-Output als JSON oder manuell übertragen
├── utils.py        # Hilfsfunktionen (z. B. zum Einlesen von Fragen)
├── style.css       # optionales Design
└── README.md
```

### ✅ Aufgabenübersicht

- [ ] 🔁 Fragen mit Prompt in Augment generieren
- [ ] 📥 Fragen in `questions.json` oder als Python-Dict speichern
- [ ] 🧠 `utils.py`: Funktion zum Einlesen & Parsen der Fragen
- [ ] 🎨 `app.py`: Streamlit-Frontend
  - [ ] Titel & Beschreibung
  - [ ] Navigation durch Fragen (eine nach der anderen)
  - [ ] Auswahloptionen (Radiobuttons)
  - [ ] Feedback nach Auswahl (richtig/falsch + Erklärung)
  - [ ] Fortschrittsbalken / Punktestand
- [ ] ✅ Ergebnisanzeige (Ende: Score + Wiederholung)
- [ ] (Optional) 🧪 Fragen randomisieren / mischen

---

## 💡 Erweiterungsideen
- Frageneditor im Frontend
- Exportierbare Ergebnisübersicht (PDF/CSV)
- Einbindung von Bildern oder Audios

Wenn du möchtest, kann ich dir beim nächsten Schritt (z. B. `questions.json` vorbereiten oder `app.py` Grundgerüst) sofort helfen.
