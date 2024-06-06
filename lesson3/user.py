class User:

    def __init__(self,first_name,last_name):
        self.userFirst = first_name
        self.userLast = last_name

    def sayFirst (self):
        print ("Мое имя: ", self.userFirst)

    def sayLast (self):
        print ("Моя Фамилия: ", self.userLast)

    def sayFL (self):
        print ("Имя и фамилия: ", self.userFirst , self.userLast)



    