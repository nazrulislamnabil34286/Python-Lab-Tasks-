
def count_elements(lst):
    for i in set(lst):
        print(i, "=>", lst.count(i))

lst = [10,20,30,30,30,30,20,40]
count_elements(lst)