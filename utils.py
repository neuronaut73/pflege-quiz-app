import json
import random
from typing import List, Dict, Any

def load_questions_from_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Lädt Fragen aus einer Python-Datei.
    
    Args:
        file_path: Pfad zur Python-Datei mit den Fragen
        
    Returns:
        Liste von Fragen-Dictionaries
    """
    try:
        # Importiere die questions-Variable aus der Datei
        import importlib.util
        spec = importlib.util.spec_from_file_location("questions_module", file_path)
        questions_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(questions_module)
        
        return questions_module.questions
    except Exception as e:
        print(f"Fehler beim Laden der Fragen aus {file_path}: {e}")
        return []

def load_answers_from_json(file_path: str) -> Dict[str, Dict[str, str]]:
    """
    Lädt Antworten aus einer JSON-Datei.
    
    Args:
        file_path: Pfad zur JSON-Datei mit den Antworten
        
    Returns:
        Dictionary mit Antworten
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden der Antworten aus {file_path}: {e}")
        return {}

def shuffle_questions(questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Mischt die Reihenfolge der Fragen.
    
    Args:
        questions: Liste von Fragen-Dictionaries
        
    Returns:
        Gemischte Liste von Fragen-Dictionaries
    """
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    return shuffled_questions

def calculate_score_percentage(score: int, total: int) -> float:
    """
    Berechnet den Prozentsatz der korrekten Antworten.
    
    Args:
        score: Anzahl der korrekten Antworten
        total: Gesamtanzahl der Fragen
        
    Returns:
        Prozentsatz als Dezimalzahl
    """
    if total == 0:
        return 0.0
    return (score / total) * 100

def get_feedback_message(percentage: float) -> str:
    """
    Gibt eine Feedback-Nachricht basierend auf dem erreichten Prozentsatz zurück.
    
    Args:
        percentage: Prozentsatz der korrekten Antworten
        
    Returns:
        Feedback-Nachricht
    """
    if percentage >= 90:
        return "Hervorragend! Sie beherrschen die pflegerischen Konzepte ausgezeichnet!"
    elif percentage >= 75:
        return "Sehr gut! Sie haben ein solides Verständnis der pflegerischen Konzepte."
    elif percentage >= 60:
        return "Gut gemacht! Mit etwas mehr Übung werden Sie noch besser."
    else:
        return "Weiter üben! Einige Konzepte benötigen noch Ihre Aufmerksamkeit."
