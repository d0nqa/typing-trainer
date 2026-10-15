from nicegui import ui


def create_settings_page():
    ui.label('Настройки')
    ui.button('На главную', on_click=lambda: ui.navigate.to('/'))