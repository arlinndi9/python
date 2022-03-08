def is_odd(num):
    if num%2==1:
        print("True")
    else:
        print("False")

is_odd(7)

def one_to_fifty(num):
    for fizzbuzz in range(1,num+1):
     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
     elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
     elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
     print(fizzbuzz)

one_to_fifty(50)


def except_3_and_6():
    for num in range(0,10+1):
        if num!=3 and num!=6:
            print(num)



except_3_and_6()