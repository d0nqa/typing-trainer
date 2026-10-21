import json
import random
from pathlib import Path
from nicegui import app

file_path = Path(__file__).parent / 'data' / 'texts.json'

with open(file_path, 'r', encoding='utf-8') as file:
    texts = json.load(file)


def get_random_text():
    
    recent_texts = app.storage.user.get('recent_texts', [])
    
    available_texts = [
        text for text in texts
        if text['id'] not in recent_texts
    ]

    selected_text = random.choice(available_texts)

    recent_texts = recent_texts + [selected_text['id']]
    recent_texts = recent_texts[-10:]

    app.storage.user['recent_texts'] = recent_texts

    return selected_text