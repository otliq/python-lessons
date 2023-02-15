def bubleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
            print(array)

if __name__ =='__main__':
    massiv = [5,2,3,8,0,4,6,7,1,5,15,20,5,3,1]
    print(massiv)
    bubleSort(massiv)