# python slice_method.py

if __name__ == '__main__':

    lst = [12, 33, 45, 56,47]
    val = 1
    print(lst[:0])
    lst[:0] = [val]
    print(lst)  # prints [1, 12, 33, 45, 56, 47]
