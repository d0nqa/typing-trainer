from nicegui import ui


LESSONS = [
    ['а', 'о'],
    ['в', 'л'],
    ['ы', 'д'],
    ['ф', 'ж', 'э'],
    ['п', 'р'],
    ['к', 'г'],
    ['у', 'ш'],
    ['ц', 'щ'],
    ['й', 'з'],
    ['е', 'н'],
    ['х', 'ъ'],
    ['м', 'ь'],
    ['с', 'б'],
    ['я', 'ч', 'ю'],
    ['и', 'т'],
]


def create_review(title, review_type, number):
    
    review_mode = 'all' if review_type == 'lesson-review-all' else 'pair'
    
    with ui.column().classes(f'lesson-item {review_type}').on(
        'click', lambda: ui.navigate.to(f'/practice?review={number}&type={review_mode}')
        ):
        with ui.row().classes('lesson-header'):
            
            ui.label(title)
            
            ui.icon('refresh')

        with ui.row().classes('lesson-progress'):
            for i in range(5):
                ui.element('div').classes('lesson-progress-bar')


def create_lessons_page():
    with ui.column().classes('lessons-page'):
        with ui.row().classes('lessons-navbar'):
            ui.button('На главную',icon='arrow_back',
                      on_click=lambda: ui.navigate.to('/')
            ).props('flat color=none no-caps').classes('lessons-back-button')

            
        ui.label('Выбор урока').classes('lessons-title')

        ui.label('Изучай буквы, проходи уровни и закрепляй навыки.').classes('lessons-description')

        with ui.column().classes('lessons-container'):
            for number, letters in enumerate(LESSONS, start=1):
                with ui.column().classes('lesson-item').on(
                    'click', lambda number=number: ui.navigate.to(f'/practice?lesson={number}')
                    ):
                    with ui.row().classes('lesson-header'):
                        
                        title = f'Урок {number} — {", ".join(letters).upper()}'
                        
                        ui.label(title)
                        
                        ui.icon('play_arrow')

                    with ui.row().classes('lesson-progress'):
                        for i in range(5):
                            ui.element('div').classes('lesson-progress-bar')
                    
                    
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