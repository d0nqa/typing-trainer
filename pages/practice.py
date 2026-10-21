import time
from nicegui import ui
from html import escape
from text_manager import get_random_text


def create_practice_page():
    
    selected_text = get_random_text()
    practice_text = selected_text['text']
    current_position = 0
    typing_results = []
    start_time = None
    keyboard_keys = {}
    
    left_hand_keys = {
        'Ё', '1', '2', '3', '4', '5',
        'Й', 'Ц', 'У', 'К', 'Е',
        'Ф', 'Ы', 'В', 'А', 'П',
        'Я', 'Ч', 'С', 'М', 'И'
    }
                
    right_hand_keys = {
        '6', '7', '8', '9', '0', '-', '=', '⌫',
        'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ',
        'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Enter',
        'Т', 'Ь', 'Б', 'Ю', '.'
    }
    
    def handle_key(event):
        nonlocal current_position, start_time
        
        if not event.action.keydown:
            return
        
        key_name = event.key.name
        
        if len(key_name) != 1:
            return
        
        if current_position >= len(practice_text):
            return
        
        if start_time is None:
            start_time = time.monotonic()
        
        expected_char = practice_text[current_position]
        
        is_correct = key_name.lower() == expected_char.lower()
        
        typing_results.append(is_correct)
        
        current_position += 1
        
        update_text()
        update_finger_hint()
        
        if current_position == len(practice_text):
            elapsed_time = time.monotonic() - start_time
            
            characters_count = len(typing_results)
            
            speed = characters_count / max(elapsed_time, 0.001) * 60
            
            errors_count = typing_results.count(False)
            correct_count = typing_results.count(True)
            accuracy = correct_count / characters_count * 100
            
            speed_label.text = f'{speed:.0f}'
            accuracy_label.text = f'{accuracy:.1f}%'
            errors_label.text = str(errors_count)
            
            text_element.set_visibility(False)
            results_container.set_visibility(True)

    def restart_practice():
        nonlocal current_position, start_time
        
        current_position = 0
        start_time = None
        typing_results.clear()
        
        text_element.set_visibility(True)
        results_container.set_visibility(False)
        
        update_text()
        update_finger_hint()
        
    def next_practice():
        nonlocal practice_text

        selected_text = get_random_text()
        practice_text = selected_text['text']

        restart_practice()

    ui.keyboard(on_key=handle_key)

    with ui.column().classes('practice-page'):

        with ui.row().classes('practice-navbar'):
            with ui.row().classes('items-center'):
                ui.icon('keyboard').classes('practice-logo')
                ui.label('typing trainer').classes('practice-logo-text')

            ui.button('На главную',icon='arrow_back',
                on_click=lambda: ui.navigate.to('/')
            ).props('flat color=none no-caps').classes('practice-back-button')
        with ui.column().classes('practice-text-container'):
            ui.label('ТЕКСТ ДЛЯ ПЕЧАТИ')
            
            text_element = ui.html('', sanitize=False).classes('practice-text w-full')
            
            def update_text():
                characters_html = ''
                
                for i, char in enumerate(practice_text):
                    if i == current_position:
                        char_class = 'practice-current'
                    
                    elif i < current_position:
                        if typing_results[i]:
                            char_class = 'practice-correct'
                        else:
                            char_class = 'practice-error'
                    else:
                        char_class = ''

                    characters_html += (
                        f'<span class="practice-character {char_class}">'
                        f'{escape(char)}''</span>'
                        )

                text_element.content = characters_html
                update_keyboard()
            
            
            def update_finger_hint():   #функция определения пальца для подсказки
                if current_position >= len(practice_text):
                    finger_hint.text = ''
                    return
                
                char = practice_text[current_position].upper()
                
                if char == ' ':
                    hand_hint.text = 'Обе руки'
                    finger_hint.text = 'Большой палец'
                    return
                
                if char == ',':
                    hand_hint.text = 'Правая рука + левая рука'
                    finger_hint.text = 'Мизинец (.) + мищинец (Shift)'
                    return
                
                if char in left_hand_keys:
                    hand = 'Левая рука'
                
                elif char in right_hand_keys:
                    hand = 'Правая рука'
                
                else:
                    hand_hint.text = ''
                    finger_hint.text = ''
                    return
                
                for finger_class, keys in finger_map.items():
                    if char in keys:
                        hand_hint.text = hand
                        finger_hint.text = finger_names[finger_class]
                        return
                
                finger_hint.text = ''
            
            def update_keyboard():
                for elements in keyboard_keys.values():
                    for element in elements:
                        element.classes(remove='keyboard-active')
                
                if current_position >= len(practice_text):
                    return
                
                current_char = practice_text[current_position]
                
                if current_char == ',':
                    key_name = '.'
                    
                    for element in keyboard_keys.get('Shift', []):
                        element.classes(add='keyboard-active')
                
                
                elif current_char.isalpha() and current_char.isupper():
                    key_name = current_char.upper()
                    
                    shift_keys = keyboard_keys.get('Shift', [])
                    
                    if current_char in left_hand_keys:
                        shift_index = 1
                    
                    else:
                        shift_index = 0
                    
                    if len(shift_keys) > shift_index:
                        shift_keys[shift_index].classes(add='keyboard-active')
                
                elif current_char == ' ':
                    key_name = 'Пробел'
                    
                else:
                    key_name = current_char.upper()
                
                for element in keyboard_keys.get(key_name, []):
                    element.classes(add='keyboard-active')
            
            update_text()
            
            results_container = ui.column().classes('practice-results')
            results_container.set_visibility(False)
            
            with results_container:
                ui.icon('check_circle').classes('practice-results-icon')
                ui.label('Тренировка завершена!').classes('practice-results-text')
                
                with ui.row().classes('practice-stats'):
                    with ui.column().classes('practice-stat'):
                        speed_label = ui.label('0').classes('practice-stat-value')
                        ui.label('Символов/мин').classes('practice-stat-name')

                    with ui.column().classes('practice-stat'):
                        accuracy_label = ui.label('0%').classes('practice-stat-value')
                        ui.label('Точность').classes('practice-stat-name')

                    with ui.column().classes('practice-stat'):
                        errors_label = ui.label('0').classes('practice-stat-value')
                        ui.label('Ошибки').classes('practice-stat-name')
                
                ui.button(
                    'Следующая тренировка',
                    on_click=next_practice
                ).props('color=none no-caps unelevated').classes('practice-next-button')

                ui.button(
                    'Начать заново',
                    on_click=restart_practice
                    ).props('color=none no-caps unelevated').classes('practice-restart-button')
             
        
        with ui.column().classes('practice-keyboard-container'):
            ui.label('КЛАВИАТУРА')

            
            keyboard_rows = [
                ['Ё', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '0', '-', '=', '⌫'],

                ['Й', 'Ц', 'У', 'К', 'Е', 'Н',
                 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],

                ['Ф', 'Ы', 'В', 'А', 'П', 'Р',
                 'О', 'Л', 'Д', 'Ж', 'Э', 'Enter'],

                ['Я', 'Ч', 'С', 'М', 'И', 'Т',
                 'Ь', 'Б', 'Ю', '.'],

                ['Shift', 'Пробел', 'Shift']
            ]
            
            finger_map = {
                'key-pinky': [
                    'Ё', '1', '0', '-', '=', '⌫',
                    'Й', 'З', 'Х', 'Ъ',
                    'Ф', 'Ж', 'Э', 'Enter',
                    'Я', '.', 'Shift'
                ],'key-ring': [
                    '2', '9', 'Ц', 'Щ',
                    'Ы', 'Д', 'Ч', 'Ю'
                ],'key-middle': [
                    '3', '8', 'У', 'Ш',
                    'В', 'Л', 'С', 'Б'
                ],'key-index': [
                    '4', '5', '6', '7',
                    'К', 'Е', 'Н', 'Г',
                    'А', 'П', 'Р', 'О',
                    'М', 'И', 'Т', 'Ь'
                ],'key-thumb': ['Пробел']
            }
            
            finger_names = {
                'key-pinky': 'Мизинец',
                'key-ring': 'Безымянный палец',
                'key-middle': 'Средний палец',
                'key-index': 'Указательный палец',
                'key-thumb': 'Большой палец',
            }
            
            for row in keyboard_rows:
                with ui.row().classes('keyboard-row'):
                    for key in row:
                        key_classes = 'keyboard-key'

                        for finger_class, keys in finger_map.items():
                            if key in keys:
                                key_classes += f' {finger_class}'
                                break
                        
                        if key == 'Пробел':
                            key_classes += ' keyboard-space'

                        elif key == 'Shift':
                            key_classes += ' keyboard-shift'

                        elif key in ['Enter', '⌫']:
                            key_classes += ' keyboard-wide'
                        
                        key_element = ui.label(key).classes(key_classes)

                        keyboard_keys.setdefault(key, []).append(key_element)
            
            finger_legend = [
                ('Мизинец', '#F26D6D'),
                ('Безымянный', '#F4A261'),
                ('Средний', '#EDC66E'),
                ('Указательный', '#7BA9ED'),
                ('Большой', '#A78BFA'),
            ]
            
            with ui.column().classes('keyboard-finger-hint'):
                hand_hint = ui.label('')
                finger_hint = ui.label('')
            
            with ui.row().classes('keyboard-legend'):
                for finger_name, finger_color in finger_legend:
                    with ui.row().classes('keyboard-legend-item'):
                        ui.element('div').classes(
                            'keyboard-legend-dot'
                        ).style(f'background-color: {finger_color}')

                        ui.label(finger_name)
      
    update_keyboard()
    update_finger_hint()