# как-то получить оценку от пользователя
rate_as_str = input("Оцените работу оператора от 1 до 5:") # str
rate = int(rate_as_str) # int

# проверить, что оценка от 1 до 5
if(rate < 1):
    rate = 1

if(rate > 5):
    rate = 5

# в зависимости от оценки, предложить дать обратную связь

feedback = ""

if rate == 1:
    feedback = input("Расскажите, что нам улучшить: ")
elif rate == 2:
    feedback = input("Расскажите, что вас смутило: ")
elif rate == 3:
    feedback = input("Расскажите, как нам стать лучше: ")
elif rate == 4:
    feedback = input("Расскажите, почему не 5: ")
else:
    feedback = input("Расскажите, за что похвалить оператора: ")

print(feedback)
