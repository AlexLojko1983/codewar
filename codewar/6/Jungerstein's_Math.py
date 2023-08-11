
def count_zeros_n_double_fact(n):
    if not n%2:
        number_list = [i for i in range(1, n + 1) if not i % 2]
    else:
        number_list = [i for i in range(1,n+1) if i%2]
    number_f = 1
    for i in number_list:
        number_f *= i

    number_len_old = len(str(number_f))
    number_len_new = len(str(int(str(number_f)[::-1])))
    return (number_len_old - number_len_new)

print(count_zeros_n_double_fact(158))

