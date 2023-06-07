# Просто, учитывая строку слов, вернуть длину кратчайшего слова (слов).
# Строка никогда не будет пустой, и вам не нужно учитывать разные типы данных.
s = "bitcoin take over the world maybe who knows perhaps"


def find_short(s):
    l = min(map(len, s.split()))
    return l


print(find_short(s))
