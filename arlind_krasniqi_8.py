#1
fibo_seq_plus = [0, 1, 1, 2, 3, 5, 8, 12, 20, [3.14, 1.618, 2.71]]
sub_list=fibo_seq_plus[9][1:]
fibo_seq_plus[7]=13
fibo_seq_plus[8]=21
print(sub_list)
print(fibo_seq_plus)


#2
my_str = "Mirë*se*vjen, *me*krahë*te*letë,"
word=my_str.split("*")
my_str=' '.join(word)


#3
def lista(a):
    total = 1
    for x in a:
        total = total * x
    return total

print(lista([1,2,3,4]))

#4

def lisst(b):
    small=min(b)
    return small

print(lisst([2,3,4]))

#5
def my_lst(a,b):
        if len(a) >len(b):
            c=a+b
            print(c)
        elif len(b)>len(a):
            print("lista b eshte me e gjate")
        elif len(a)==len(b):
            print("keto lista kane gjatesi te njejt")

my_lst([1,2,3],[1,2,3,4])

#6
def ls(a):
    total=0
    for i in a:
        total=total+i
    print(total)

ls([1,2,3,4,5,6,7,8,9,10])


lst=[1,2,3,4,56,7,9,98,78,4,512,11,2,332,1213,454,1269]
lst2=['a','b','c','d','e','f','g','h']
a=sum(lst)
print(a)
print(lst.sort())
print(lst[3:8])#slices
lst.append(123)
lst.remove(11)#remove ne baze te vleres
lst.pop(6)#pop ne baze te indexit
print(lst.count(2))#tregon sa numra me vler 2 i kemi ne list
lst.reverse()
lst.extend(lst2)#i kemi bashku listat
lst.append(lst2)
print(lst)
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)#concatenate elementet e listes
print(s)

def lss(a):#shuma e elementit ne indexin1 dhe te fundir
    for i in a:
        l=[a[1]+len(a)-1]
        print(l)
        break

lss([1,2,3,4,5])

def chop(a):#kemi fshi elentin e pare dhe te fundit ne list
    del a[0]
    del a[len(a)-1]
    print(a)
chop([9,8,7,6,5])

