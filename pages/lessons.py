from nicegui import ui


def create_lessons_page():
    ui.label('Выбор урока')
    ui.button('На главную', on_click=lambda: ui.navigate.to('/'))