from nicegui import ui

def create_home_page():
    with ui.column().classes('home-page items-center justify-center w-full'):        
        with ui.card().classes('home-card'):
                       
            ui.icon('keyboard').classes('home-icon')
            
            ui.label('Тренажёр слепой печати').classes('home-title')

            ui.button('Начать обучение', on_click=lambda: ui.navigate.to('/lessons')
                      ).props('unelevated color=none').classes('home-button-primary')
            
            ui.button('Тренировка',on_click=lambda: ui.navigate.to('/practice')
                ).props('unelevated color=none').classes('home-button-secondary')
            
            ui.button('Настройки',on_click=lambda: ui.navigate.to('/settings')
                ).props('unelevated color=none').classes('home-button-secondary')