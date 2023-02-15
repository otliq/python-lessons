from colorama import Fore,Back,Style
#python program for implementation of Mergesort
def mergesort(arr):
    if len(arr)>1:

        #finding th mid of the array
        mid = len(arr)//2

        #dividing the array elements
        L = arr[:mid]
        print(Back.GREEN + str(L))

        #into 2 halves
        R = arr[mid:]
        print(Back.RED + str(R))
        mergesort(L)
        mergesort(R)

        i=j=k=0
        #Copy data to temp arrays L[] and R[]
        while i <len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        #Cheking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        print(Back.CYAN + str(L))
        print(Back.BLUE + str(R))

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")


# Driver Code
if __name__ == '__main__':
	arr = [34, 25, 20, 5, 44, 12,9]
	print("Tartibsiz array:")
	printList(arr)
	mergesort(arr)
	print(Style.RESET_ALL + "Tartibli array: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna