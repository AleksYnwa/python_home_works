from address import Address
from mailing import Mailing

from_address = Address("333444", "Ижевск", "Ленина", "18", "66")
to_address = Address("123456", "Казань", "Декабристов", "79", "1")

mailing = Mailing(to_address, from_address, 600, 123456789)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")