new_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while True:
    name = new_list.pop()
    if name == "Валера":
        print("Валера нашелся")
        break
    else:
        print(name)
