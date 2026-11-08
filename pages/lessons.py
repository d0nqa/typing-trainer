from nicegui import ui, app
from lesson_data import LESSONS
from progress_manager import get_next_level, reset_progress

def create_review(title, review_type, number):
    
    review_mode = 'all' if review_type == 'lesson-review-all' else 'pair'
    
    review_progress = app.storage.user.get('review_progress', {})
    
    review_key = f'{review_mode}_{number}'
    
    is_completed = review_progress.get(review_key, False)
    
    with ui.column().classes(f'lesson-item {review_type}').on(
        'click', lambda: ui.navigate.to(f'/practice?review={number}&type={review_mode}')
        ):
        with ui.row().classes('lesson-header'):
            
            ui.label(title)
            
            ui.icon('refresh')

        with ui.row().classes('lesson-progress'):
            bar = ui.element('div').classes('lesson-progress-bar review-progress-bar')
                
            if is_completed:
                bar.classes(add='lesson-progress-completed')


def create_lessons_page():  #создает страницу с уроками
    progress = app.storage.user.get('lesson_progress', {})
    with ui.column().classes('lessons-page'):
        with ui.row().classes('lessons-navbar'):
            ui.button('На главную',icon='arrow_back',
                      on_click=lambda: ui.navigate.to('/')
            ).props('flat color=none no-caps').classes('lessons-back-button')

            
        ui.label('Выбор урока').classes('lessons-title')
        
        ui.button('Сбросить', on_click=lambda: (reset_progress(), ui.navigate.to('/lessons')))

        ui.label('Изучай буквы, проходи уровни и закрепляй навыки.').classes('lessons-description')

        with ui.column().classes('lessons-container'):
            for number, letters in enumerate(LESSONS, start=1):
                with ui.column().classes('lesson-item').on(
                    'click', lambda number=number: ui.navigate.to(
                        f'/practice?lesson={number}&level={get_next_level(number)}'
                        )
                    ):
                    with ui.row().classes('lesson-header'):
                        
                        title = f'Урок {number} — {", ".join(letters).upper()}'
                        
                        ui.label(title)
                        
                        ui.icon('play_arrow')
                    
                    completed_levels = progress.get(str(number), [])
                    
                    with ui.row().classes('lesson-progress'):
                        for i in range(1, 6):
                            bar = ui.element('div').classes('lesson-progress-bar')
                            
                            if i in completed_levels:
                                bar.classes(add='lesson-progress-completed')
                    
                    
                if number % 5 == 0:
                        create_review(f'Большое повторение — уроки 1–{number}',
                                      'lesson-review-all',
                                      number
                                      )

                elif number % 2 == 0:
                        create_review(f'Повторение — уроки {number - 1}–{number}',
                                      'lesson-review',
                                      number
                                      )