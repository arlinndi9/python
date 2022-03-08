def step_sum(num, step):
    if step <= 0:
        print("step should be greater than zero")
    else:
        sum = 0
        while (num > 0):
            sum += num
            num -= step
        return sum


step_sum(3, 1)


def until():
    while True:
        number = int(input("type an integer: "))
        if number % 2 == 0 and (number % 4) != 0:
            break
        print(number)


until()