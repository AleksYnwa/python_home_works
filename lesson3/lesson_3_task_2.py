from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79121234567"),
    Smartphone("Samsung", "Galaxy S24+", "+79123452463"),
    Smartphone("Huawei", "Mate XT", "+79127653827"),
    Smartphone("Xiaomi", "15 Ultra", "+79128431010"),
    Smartphone("Apple", "iPhone 16 PRO MAX", "+79129876543"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")
