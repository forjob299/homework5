
immutable_var = (1, 'apple', 2.5, True)
print('Immutable tuple:', immutable_var)
# immutable_var[0] == 0:
# print(immutable_var)
# Невозможно изменить кортеж
mutable_list = [1, 'apple', 2.5, True]
mutable_list[0] = mutable_list[0] + mutable_list[2]
print('Mutable list:', mutable_list)




