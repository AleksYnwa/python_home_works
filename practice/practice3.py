from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.sayAge()
alex.setAge(33)
alex.sayAge()

card = Card("1234 1234 1234 1234", "11/28", "Alex F")
alex.addCard(card)
alex.getCard().pay(2000)




