from random import randrange
def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i<=pivot]
        katta = [i for i in array if i>pivot]
        print(f'{kichik} + {pivot} + {katta}')
        return qsort(kichik) + [pivot] + qsort(katta)

if __name__ == "__main__":
    array1 = [5, 2, 3, 1, 5, 4, 7, 8, 9, 6, 26, 30, 15, 45, 84, 564, 156]
    print(array1)
    print(qsort(array1))
