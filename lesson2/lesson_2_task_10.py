# #x = int(input("Сумма вклада: "))
# #y = int(input ("Количество лет: "))
# def bank(x, y):
#     for year in range (1,y+1): 
#         x=(x*1,1)
#         return x
# bank(500, 2)
def bank(x, y):
    for i in range (1,y+1): 
        input=x+(x/10)
        x=input
    print(round (input,4))
bank(1000, 10)
