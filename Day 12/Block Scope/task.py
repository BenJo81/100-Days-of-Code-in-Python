numb = int(input(""))


def is_prime(num):
    num_list = []
    for check in range(num):
        print(check)
        if num % (check + 1) == 0:
            num_list.append(check)

    if len(num_list) <= 2:
        return True
    else:
        return False


boo = is_prime(numb)
print(boo)
