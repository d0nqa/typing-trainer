import os
from nicegui import ui
from pathlib import Path
from pages.home import create_home_page
from pages.lessons import create_lessons_page
from pages.practice import create_practice_page
from pages.settings import create_settings_page


css_path = Path(__file__).parent / 'static' / 'style.css'

ui.add_css(css_path.read_text(encoding='utf-8'), shared=True)


@ui.page('/')
def home():
    create_home_page()

@ui.page('/lessons')
def lessons():
    create_lessons_page()

@ui.page('/practice')
def practice():
    create_practice_page()

@ui.page('/settings')
def settings():
    create_settings_page()


ui.run(storage_secret=os.environ.get(
    'STORAGE_SECRET', 'typing-trainer-local-dev'
    ))