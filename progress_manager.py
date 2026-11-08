from nicegui import app

def complete_level(lesson, level):    #Сохраняет прохождение уровня
    progress = app.storage.user.get('lesson_progress', {})
    lesson_key = str(lesson)
    completed_levels = progress.get(lesson_key, [])
    
    if level not in completed_levels:
        completed_levels.append(level)
    
    progress[lesson_key] = completed_levels
    app.storage.user['lesson_progress'] = progress
    

def get_next_level(lesson):    #Возвращает первый незавершённый уровень урока
    
    progress = app.storage.user.get('lesson_progress', {})
    completed_levels = progress.get(str(lesson), [])
    
    for level in range(1, 6):
        if level not in completed_levels:
            return level
    
    return 5


def reset_progress():   #сбрасывает прогресс
    app.storage.user['lesson_progress'] = {}
    
    app.storage.user['review_progress'] = {}
    


def complete_review(number, review_type):   #Сохраняет успешное прохождение повторения
    
    progress = app.storage.user.get('review_progress', {})
    
    review_key = f'{review_type}_{number}'
    
    progress[review_key] = True
    
    app.storage.user['review_progress'] = progress