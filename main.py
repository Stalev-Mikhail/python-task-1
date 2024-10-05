#Запускати тільки у консолі Windows

import time as t

def to_temp(number):
    return number*30
def to_speed(number):
    return number*200

def calculate_time(rezhim, temperature, speed):
    if speed <= 0:
        raise ValueError("Швидкiсть обертів пральноi машини має бути більше 0.")
    
    rezhimi = [
        (temperature - 30) * 0.7 + 65,
        (temperature - 30) + 79,
         temperature,
        (temperature - 30) * 0.8 + 55,
        20,
        0.02 * speed
    ]
    
    if rezhim < 7:
        ret = rezhimi[rezhim-1]
    else:
        raise ValueError(f"{rezhim} is not supported")
        
    return ret

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        print( end='')
        t.sleep(.1)
        seconds -= 1
    print("00:00")
    print("\n")
    

prev_mode = 6
while True:
    if prev_mode == 6:
        rezhim = int(input("Оберiть режим прання: 1-синтетика, 2-бавовна, 3-делiкатна, 4-швидке прання, 5-полоскання, 6-вiджим  "))
        temp_input = int(input("Оберiть температуру прання: 1-30; 2-60; 3-90?:  "))
        obert_speed = to_speed(int(input("Оберiть швидкiсть машинки для вiджиму: 1-200, 2-400, 3-600, 4-800, 5-1000, 6-1200 ")))
        temp = to_temp(temp_input)
        time = int(round(calculate_time(rezhim, temp, obert_speed)))
        input("Прання займе " + str(time+calculate_time(5, temp, obert_speed)+calculate_time(6, temp, obert_speed)) + " секунд. Натиснiть Enter щоб розпочати його")
        countdown(time)
        prev_mode = rezhim
    if prev_mode in [1,2,3,4]:
        print("Починаю полоскання")
        time = int(round(calculate_time(5, temp, obert_speed)))
        countdown(time)
        prev_mode = 5
    if prev_mode == 5:
        print("Починаю вiджим")
        time = int(round(calculate_time(6, temp, obert_speed)))
        countdown(time)
        prev_mode = 6
        input("Прання закiнчено. Натиснiть Enter щоб розпочати нове прання.")
