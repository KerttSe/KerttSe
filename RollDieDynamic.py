"""построения гистограммы частот бросков кубика """
from matplotlib import animation
import matplotlib.pyplot as plt 
import random 
import seaborn as sns
import sys 

def update(frame_number, rolls,faces, frequencies):
     """ НАстраивает содержимое  диаграмы для каждого кадра анимации."""
     # бросок кубика  и обновление частот
     for i in range(rolls):
         frequencies[random.randrange(1,7) - 1] += 1

    #настройка диаграммы  для обнов. частот 
     plt.cla('') 
     axes = sns.barplot(faces, frequencies, palette='bright')
     axes.set_title(f'Die Frequencies for {sum(fraquencies):,} Rolls')
     axes.set(xlabel='Die Value', ylabel='Frequency')
     axes.set_ylim(top=max(frequencies) * 1.10)#маштабирование оси у  на 10 % 

    #  вывод частоты и процента  над каждым  столбцом
     for bar, frequency in zip(axes.patches, frequencies):
         text_x = bar.get_x() + bar.get_width() / 2.0
         text_y = bar.get_height()
         text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
         axes.text(text_x, text_y, text, ha='center', va='bottom')
#получение аргументов  ком.строки  для количества кадров  и бросков на кадр 
 

number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])


sns.set_style('whitegrid') #белый фон с белыми линиями 
figure = plt.figure('Rolling a Six-Side Die')#рисунок для анимации
values = list(range(1, 7))# грани для вывода на оси х 
frequencies = [0] * 6 # список  частот  из шести элементов
# Настройка и запуск анимации...вызывающий  функцию update 
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, values, frequencies))

plt.show
