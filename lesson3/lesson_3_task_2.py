from smartphone import Smartphone

catalog = [ ]

n1= Smartphone ("iPhone" , '15 Pro' , "+79218525252")
n2= Smartphone ("Samsung" , 'Galaxy S21' , "+79218523636")
n3= Smartphone ("Huawei" , 'nova 11 Pro' , "+79219639696")
n4= Smartphone ("Xiaomi" , '13 Pro' , "+79218523636")
n5= Smartphone ("ASUS" , 'Zenfone 10' , "+79218523636")

catalog.append(n1)
catalog.append(n2)
catalog.append(n3)
catalog.append(n4)
catalog.append(n5)


for n in catalog:
    print(f"{n.stamp}-{n.model}. {n.number}")