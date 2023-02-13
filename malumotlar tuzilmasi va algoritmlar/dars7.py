#SELECTION SORT
mylist = [100,500,5,600,5,15,9,7,8,56,5,3,4,1,8,9,7,1,1515,151530,65,35,89,61,21,564,15,1000,1546,1,0,16]
big_o = len(mylist)**2
def selection_sort(array):
    sorted_list = []
    while array:
        max_list = max(array)
        sorted_list.append(max_list)
        array.remove(max_list)
    print(sorted_list)

selection_sort(mylist)
print(f"Big O: {big_o}")