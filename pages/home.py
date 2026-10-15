from nicegui import ui

def create_home_page():
    ui.label('Тренажёр слепой печати')
    ui.button('Начать обучение', on_click=lambda: ui.navigate.to('/lessons'))
    ui.button('Тренировка', on_click=lambda: ui.navigate.to('/practice'))
    ui.button('Настройки', on_click=lambda: ui.navigate.to('/settings'))