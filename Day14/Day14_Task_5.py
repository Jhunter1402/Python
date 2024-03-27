class Custom_list:
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, other):
        return self.lst + other.lst

lst1 = [1,2,3]
lst2 = [6,5,4]
l1 = Custom_list(lst1)
l2 = Custom_list(lst2)
print(l1 + l2)