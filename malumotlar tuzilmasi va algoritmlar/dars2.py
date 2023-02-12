
def find_linear_search(t=100):
    for i in range(0,t):
        answer = input(f"siz {i}-oyladingizm? (y/n)")
        if answer =="y":
            print("yutdim!")
            print(i)

def find_binary_search(list,item):
    lbound = 0
    ubound = len(list)-1
    while lbound<=ubound:
        mid = (lbound+ubound)//2
        guess = list[mid]
        if guess == item:
            print(mid)
        if guess > item:
            ubound = mid - 1
        else:
            lbound = mid + 1
    return None
# my_list = [x for x in range(1,100)]
# find_binary_search(my_list,50)