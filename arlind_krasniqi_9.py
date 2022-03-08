#1
numbers={"one":1,"two":2,"three":3}
print(len(numbers))
print(numbers.get("two"))

#2

mapping={"ar":2.1,"ks":3.12,"alb":3.14,"pse":1.1}
print("pse"in mapping)
print(3.14 in mapping.values())

#3
def add_item(d,key,values):
    if key not in d:
        d.update({key:values})
        print(d)
    else:
        print("key existt")

add_item({1:"one",2:"two",3:"three",4:"four"},0,"zero")

#4
def check_key(d,value):
    if value not in d.values():
        return False
    else:
        return True

check_key({1:2,2:3,3:4},4)

#5
def mydct(d):
    total=0
    for i in d.values():
        total=total+i
    return total
mydct({"4": 3, 'po': 6, 1: 1})

#6
def mydct(d):
    total=1
    for i in d.keys():
        total=total*i
    return total
mydct({10: 'a', 3: 20, 2: 'ani'})