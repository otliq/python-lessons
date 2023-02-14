def sum(array):
    if len(array)==1:
        return array[0]
    elif len(array)==0:
        return
    else:
        array_first = array.pop(0)
        array_first += sum(array)
        return array_first
# def summa(array):
#     if array == []:
#         return 0
#     return array[0]+summa(array[1:])
# mylist = [1,2,3,4,5,6,7,8,9,10]
# print(sum(mylist))

def evklid(num1,num2):
    if num1==0:
        return num2
    else:
        print(evklid(num2%num1,num1))

evklid(18,5)
