"""Игра угадай число.
Компьютер сам загадывает и угадывает число за наименьшее число попыток
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0   # Задаем счетчик числа попыток
    low = 1     # Задаем нижнюю границу диапазона поиска 
    high = 100  # Задаем верхнюю границу диапазона поиска 
    
    while True:
        count += 1
        predict_number = (low + high) // 2  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            low = predict_number + 1  # сдвигаем нижнюю границу
        else:
            high = predict_number - 1  # сдвигаем верхнюю границу
            
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    count = 0
   

    for number in random_array: # цикл для последовательного угадывания чисел в списке 
         count += random_predict(number) # добавляем число попыток, которое потребовалось угадать текущее число

    score = int(count / 1000) # находим среднее количество попыток


    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN

if __name__ == '__main__':
    score_game(random_predict)