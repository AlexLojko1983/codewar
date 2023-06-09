# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
# name + " plays banjo"
# name + " does not play banjo"
# Указанные имена всегда являются допустимыми строками.

def are_you_playing_banjo(name: str):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"

print(are_you_playing_banjo('robert'))