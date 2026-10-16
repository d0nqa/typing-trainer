from nicegui import ui

def create_home_page():
    with ui.column(
        ).classes(
            'items-center justify-center w-full min-h-screen'
                  ):        
        with ui.card(
            ).classes(
                'home-card'
                ):
                       
            ui.icon(
                'keyboard'
                ).classes(
                    'home-icon'
                    )
            
            ui.label(
                'Тренажёр слепой печати'
                ).classes(
                    'home-title'
                    )
            
            ui.label(
                'Научись печатать быстро и без ошибок, не глядя на клавиатуру.'
            ).classes(
                'home-description'
                )

            ui.button(
                'Начать обучение',
                on_click=lambda: ui.navigate.to('/lessons')
                ).props(
                    'unelevated color=none'
                    ).classes(
                        'home-button-primary'
                        )
            
            ui.button(
                'Тренировка',
                on_click=lambda: ui.navigate.to('/practice')
                ).props(
                    'unelevated color=none'
                    ).classes(
                        'home-button-secondary'
                        )
            
            ui.button(
                'Настройки',
                on_click=lambda: ui.navigate.to('/settings')
                ).props(
                    'unelevated color=none'
                    ).classes(
                        'home-button-secondary'
                        )