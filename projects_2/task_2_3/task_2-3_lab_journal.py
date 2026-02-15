researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату исследования: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Напишите вывод эксперимента: ")


with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+--------------------------------------------------+\n")
    file.write("|  Электронный лабораторный журнал                 |\n") 
    file.write("+--------------------------------------------------+\n")
    file.write(f"|  ФИО исследователя: {researcher_name} {(50-22-len(researcher_name)) * " "}|\n")
    file.write(f"|  Дата: {date} {(50-9-len(date)) * " "}|\n")
    file.write(f"|  Эксперимент: {experiment_name} {(50-16-len(experiment_name)) * " "}|\n")
    file.write("+--------------------------------------------------+\n")
    file.write(f"|  Вывод:                                          |\n")
    file.write(f"|  {conclusion} {(50-3-len(conclusion)) * " "}|\n")
    file.write("+--------------------------------------------------+")

print("Данные успешно сохранены в journal.txt")
