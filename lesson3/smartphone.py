class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

phone = Smartphone("Apple", "iPhone 13", "+79121234567")

print(phone.brand)
print(phone.model)
print(phone.phone_number)