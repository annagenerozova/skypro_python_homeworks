from address import Address
from mailing import Mailing

to_address = Address("193230", "Санкт-Петербург", "Дыбенко", "5к1", "81")
from_address = Address ("160000", "Вологда", "Герцена", "76", "55")
cost = 350
track = ("1234567")
mailing = Mailing (to_address,from_address, cost, track )

print(f"Отправление {track} из {to_address} в {from_address}. Стоимость {cost} рублей.")

