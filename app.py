import streamlit as st
import random
from questions import questions
import json

# Seitenkonfiguration
st.set_page_config(
    page_title="Pflegekonzepte Quiz",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",  # Seitenleiste standardmäßig geschlossen
    menu_items={
        'About': "Quiz-App für Pflegefachpersonen in der Weiterbildung zur Praxisanleitung"
    }
)

# Keine Seitenleiste mehr für den QR-Code

# CSS für besseres Aussehen
st.markdown("""
<style>
    body {
        color: white;
        background-color: #1a1a1a;
    }
    .main {
        padding: 2rem;
        background-color: #121212;
    }
    .stButton button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-size: 16px;
    }
    .option-box {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        cursor: pointer;
    }
    .correct-answer {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
    }
    .wrong-answer {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
    }
    .neutral {
        background-color: #34495e;
        border: 1px solid #2c3e50;
        color: white;
    }
    .feedback-box {
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .progress-container {
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .question-container {
        background-color: #2c3e50;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .result-container {
        text-align: center;
        padding: 20px;
        background-color: #2c3e50;
        color: white;
        border-radius: 10px;
        margin: 20px 0;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
    .stMarkdown {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialisierung der Session State Variablen
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'questions_order' not in st.session_state:
    # Zufällige Reihenfolge der Fragen
    st.session_state.questions_order = list(range(len(questions)))
    random.shuffle(st.session_state.questions_order)

# Funktion zum Zurücksetzen des Quiz
def reset_quiz():
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_completed = False
    st.session_state.questions_order = list(range(len(questions)))
    random.shuffle(st.session_state.questions_order)

# Funktion zum Überprüfen der Antwort
def check_answer(option):
    if st.session_state.answered:
        return

    current_q_idx = st.session_state.questions_order[st.session_state.current_question_index]
    current_question = questions[current_q_idx]

    st.session_state.selected_option = option
    st.session_state.answered = True

    if option == current_question["loesung"]:
        st.session_state.score += 1

# Funktion zur nächsten Frage
def next_question():
    if st.session_state.current_question_index < len(questions) - 1:
        st.session_state.current_question_index += 1
        st.session_state.answered = False
        st.session_state.selected_option = None
    else:
        st.session_state.quiz_completed = True

# Header mit Titel, Credits und Reset-Button
st.markdown(
    '<div style="text-align: center; color: #888; font-size: 0.9em; margin-bottom: 10px;">'
    'Quiz-App designed von <a href="http://www.patrec.eu" style="color: #4a86e8;">www.patrec.eu</a> für Märkisches Seniorenzentrum'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.title("🧠 Pflegekonzepte Quiz")
if st.button("Quiz neu starten"):
    reset_quiz()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Testen Sie Ihr Wissen zu Pflegekonzepten!")

# Fortschrittsbalken
progress = (st.session_state.current_question_index) / len(questions)
st.markdown('<div class="progress-container">', unsafe_allow_html=True)
st.progress(progress)

# Fortschrittsanzeige mit Frage-Nummer und Prozent-Counter
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"Frage {st.session_state.current_question_index + 1} von {len(questions)}")

# Berechne Prozentsatz der richtigen Antworten
if st.session_state.current_question_index > 0:
    correct_percentage = (st.session_state.score / st.session_state.current_question_index) * 100
    percentage_color = "#4caf50" if correct_percentage >= 60 else "#ff9800" if correct_percentage >= 40 else "#f44336"

    with col2:
        # Erstelle ein Mini-Diagramm mit dem Prozentsatz
        st.markdown(
            f'<div style="text-align: right;">'
            f'<div style="display: inline-block; width: 50px; height: 10px; background-color: #333; border-radius: 5px; margin-right: 10px;">'
            f'<div style="width: {correct_percentage}%; height: 100%; background-color: {percentage_color}; border-radius: 5px;"></div>'
            f'</div>'
            f'<span style="color: {percentage_color}; font-weight: bold;">{int(correct_percentage)}%</span> richtig'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# Wenn das Quiz noch nicht abgeschlossen ist, zeige die aktuelle Frage an
if not st.session_state.quiz_completed:
    current_q_idx = st.session_state.questions_order[st.session_state.current_question_index]
    current_question = questions[current_q_idx]

    # Frage anzeigen
    st.markdown(f'<div class="question-container"><h3 style="color: white;">{current_question["frage"]}</h3></div>', unsafe_allow_html=True)

    # Optionen anzeigen
    for option_key, option_text in current_question["optionen"].items():
        # Bestimme die CSS-Klasse basierend auf dem Status
        css_class = "neutral"
        if st.session_state.answered:
            if option_key == current_question["loesung"]:
                css_class = "correct-answer"
            elif option_key == st.session_state.selected_option:
                css_class = "wrong-answer"

        # Erstelle einen klickbaren Button für jede Option
        if st.button(
            f"{option_key}: {option_text}",
            key=f"option_{option_key}",
            on_click=check_answer,
            args=(option_key,),
            disabled=st.session_state.answered
        ):
            pass

    # Feedback anzeigen, wenn eine Antwort ausgewählt wurde
    if st.session_state.answered:
        if st.session_state.selected_option == current_question["loesung"]:
            st.markdown(
                f'<div class="feedback-box correct-answer" style="background-color: #1e4620; color: white; border: 1px solid #2a623d;"><strong>Richtig!</strong> {current_question["erklaerung"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="feedback-box wrong-answer" style="background-color: #5c1a1a; color: white; border: 1px solid #7d2a2a;"><strong>Leider falsch.</strong> Die richtige Antwort ist {current_question["loesung"]}. {current_question["erklaerung"]}</div>',
                unsafe_allow_html=True
            )

        # Button zur nächsten Frage
        st.button("Nächste Frage", on_click=next_question)

# Wenn das Quiz abgeschlossen ist, zeige das Ergebnis an
else:
    # Berechne Prozentsatz
    final_percentage = int(st.session_state.score/len(questions)*100)

    # Bestimme Farbe basierend auf Prozentsatz
    if final_percentage >= 80:
        percentage_color = "#4caf50"  # Grün
    elif final_percentage >= 60:
        percentage_color = "#8bc34a"  # Hellgrün
    elif final_percentage >= 40:
        percentage_color = "#ff9800"  # Orange
    else:
        percentage_color = "#f44336"  # Rot

    st.markdown(
        f'<div class="result-container">'
        f'<h2>Quiz abgeschlossen!</h2>'
        f'<h3>Ihr Ergebnis: {st.session_state.score} von {len(questions)} Punkten</h3>'
        f'<div style="font-size: 48px; font-weight: bold; margin: 20px 0; color: {percentage_color};">{final_percentage}%</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Bewertung basierend auf dem Ergebnis
    percentage = st.session_state.score / len(questions) * 100
    if percentage >= 90:
        st.markdown(
            f'<div style="background-color: #1e4620; color: white; padding: 15px; border-radius: 5px; border: 1px solid #2a623d;">'
            f'<strong>Hervorragend!</strong> Sie beherrschen die pflegerischen Konzepte ausgezeichnet!'
            f'</div>',
            unsafe_allow_html=True
        )
    elif percentage >= 75:
        st.markdown(
            f'<div style="background-color: #1e4620; color: white; padding: 15px; border-radius: 5px; border: 1px solid #2a623d;">'
            f'<strong>Sehr gut!</strong> Sie haben ein solides Verständnis der pflegerischen Konzepte.'
            f'</div>',
            unsafe_allow_html=True
        )
    elif percentage >= 60:
        st.markdown(
            f'<div style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; border: 1px solid #34495e;">'
            f'<strong>Gut gemacht!</strong> Mit etwas mehr Übung werden Sie noch besser.'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div style="background-color: #5c1a1a; color: white; padding: 15px; border-radius: 5px; border: 1px solid #7d2a2a;">'
            f'<strong>Weiter üben!</strong> Einige Konzepte benötigen noch Ihre Aufmerksamkeit.'
            f'</div>',
            unsafe_allow_html=True
        )

    # Button zum Neustart des Quiz
    if st.button("Quiz erneut starten"):
        reset_quiz()

# Footer
st.markdown("---")

# Footer mit Text und QR-Code
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(
        '<div style="color: #aaa; padding: 10px;">'
        '📚 Quiz für Pflegefachpersonen in der Weiterbildung zur Praxisanleitung'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    # QR-Code anzeigen
    st.image("qr-code (2).png", width=150)

# Copyright und zusätzliche Informationen
st.markdown(
    '<div style="text-align: center; color: #888; font-size: 0.8em; margin-top: 20px;">'
    '© 2025 PatRec Pflege-Quiz-App | Entwickelt mit Streamlit'
    '</div>',
    unsafe_allow_html=True
)
