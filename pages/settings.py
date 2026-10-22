from nicegui import ui, app


def create_settings_page():
    
    keyboard_enabled = app.storage.user.get(
        'show_keyboard', True
    )
    
    def save_keyboard_setting(event): #сохранение состояния переключателя клавиатуры
        app.storage.user['show_keyboard'] = event.value
    
    with ui.column().classes('settings-page'):
        
        with ui.row().classes('settings-navbar'):
            ui.button(
                'На главную',
                icon='arrow_back',
                on_click=lambda: ui.navigate.to('/')
            ).props('flat color=none no-caps').classes('settings-back-button')
        
        ui.label('Настройки').classes('settings-title')
        
        with ui.column().classes('settings-card'):
            with ui.row().classes('settings-card-header'):
                ui.icon('language')
                ui.label('Раскладка клавиатуры')

            ui.label('Выбери язык клавиатуры').classes('settings-description')
            
            with ui.row().classes('settings-language-options'):
                with ui.row().classes('settings-language-active'):
                    ui.icon('check')
                    ui.label('Русская')
                
                with ui.column().classes('settings-language-disabled'):
                    with ui.row().classes('items-center'):
                        ui.label('Английская')
                    
                    ui.label('Скоро').classes('settings-soon')
        
        with ui.column().classes('settings-card'):
            with ui.row().classes('settings-card-header'):
                ui.icon('visibility')
                ui.label('Виртуальная клавиатура')
            
            with ui.column().classes('settings-toggle-content'):
                with ui.row().classes('settings-toggle-row'):
                    ui.label('Показывать клавиатуру')
                    
                    ui.switch(
                        value=keyboard_enabled, on_change=save_keyboard_setting
                        ).props('color="purple-3"').classes('settings-keyboard-switch')
                                        
                ui.label(
                    'Отображать клавиатуру и подсказки '
                    'пальцев во время тренировки.'
                ).classes('settings-description')