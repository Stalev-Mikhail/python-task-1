import time as t

def to_Cels(txt):
    number = ""
    temp_type = ""

    for i in range(len(txt)):
        if txt[i].isdigit() or (txt[i] == '-' and not number):
            number += txt[i]
        else:
            temp_type += txt[i]

    if not number:
        raise ValueError("Температура не вказана.")
    
    number = int(number)

    perenosy = {
        "C": number,
        "K": number + 273.15,
        "F": (number - 32) * (5 / 9)
    }

    temp_type = temp_type.upper()
    if temp_type not in perenosy:
        raise ValueError(f"Неправильний тип температури: '{temp_type}'. Має бути 'C', 'K' або 'F'.")
    
    res = perenosy[temp_type]
    return round(res, 11)

def calculate_time(rezhim, temperature, speed):
    if speed <= 0:
        raise ValueError("Швидкість обертів пральної машини має бути більше 0.")
    
    rezhimi = {
        "синтетика": (temperature - 30) * 0.7 + 65,
        "бавовна": (temperature - 30) + 79,
        "швидке прання": temperature,
        "делікатна": (temperature - 30) * 0.8 + 55,
        "полоскання": 20,
        "віджим": 0.02 * speed
    }
    
    if rezhim in rezhimi:
        ret = rezhimi[rezhim]
    else:
        raise ValueError(f"{rezhim} is not supported")
        
    return ret

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        t.sleep(1)
        seconds -= 1
        
    input("Стирка закінчилася. Натисніть Enter, щоб розпочати нову стирку")

while True:
    rezhim = input("Оберіть режим прання: синтетика, бавовна, делікатна, швидке прання, полоскання, віджим  ").lower()
    temp_input = input("На якій темературі ви будете стирати "+
    "(за форматом (число + тип, напр. '30C', '300K', '86F'))?:  ")
    
    try:
        obert_speed = int(input(
            "На якій швидкості ви будете стирати?:  ")
            )
    except ValueError:
        print("Будь ласка, введіть числове значення для швидкості.")
        continue

    try:
        temp = to_Cels(temp_input)
        time = int(round(calculate_time(rezhim, temp, obert_speed)))
        input("Стирка займе " + str(time) + " секунд" + 
              ". Натисніть Enter щоб розпочати стирку")
        countdown(time)
    except ValueError:
        print(ValueError)

