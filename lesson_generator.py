import random
from lesson_data import LESSONS


def generate_lesson_text(letters, level=3): #Создаёт упражнение из заданных букв с учётом уровня.
    combinations = []
    
    for i in range(10):
        
        if level == 1:
            length = 1
        
        elif level == 2:
            length = 2
        
        elif level == 3:
            length = 3
        
        elif level == 4:
            length = random.randint(4, 5)
        
        else:
            length = random.randint(1, 5)
        
        combination = ''.join(random.choices(letters, k=length))
        combinations.append(combination)
        
    return ' '.join(combinations)


def generate_review_text(number, review_type):  #Создаёт упражнение для повторения изученных букв
    
    if review_type == 'all':
        selected_lessons = LESSONS[:number]
    
    elif review_type == 'pair':
        selected_lessons = LESSONS[number - 2:number]
    
    else:
        raise ValueError('Неизвестный тип повторения')
    
    letters = []
    
    for lesson_letters in selected_lessons:
        letters.extend(lesson_letters)
    
    return generate_lesson_text(letters, level=5)