import random
def ran_gen(x,y):
    numbers=[]
    while len(numbers) < 10:
        num=random.randint(x,y)
        if num not in numbers:
            numbers.append(num)
    print("10 Ramdom numbers between ",x ,",",y,": ")
    for i in sorted(numbers):
        print(i,end=" ")

