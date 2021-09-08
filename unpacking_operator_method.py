# python unpacking_operator_method.py

if __name__ == '__main__':

    lst = [12, 33, 45, 56,47]
    val = 1
    print(*lst)
    lst = [val, *lst]
    print(lst)  # prints [1, 12, 33, 45, 56, 47]

