sum = int(input("Сумма вклада: "))
year = int(input ("Количество лет: "))

def bank(x, y):
     for year in range (1,y+1): 
         x *= 1.1
     print(f'Вы получите {round(x,2)}')
     
bank(sum,year)