month_to_season = input("Напишите номер месяца: ")
month = int(month_to_season)
def month_to_season(month):
    if (month in [1,2,12]):
        print("Зима")
    elif (month in [3,4,5]):
        print("Весна")
    elif (month in [6,7,8]):
        print("Лето")
    elif (month in [9,10,11]):
        print("Осень") 
    else:
        print("вы ввели число не входящее в диапазон")   
month_to_season(month)

    