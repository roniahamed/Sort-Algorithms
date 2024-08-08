# display list value
def display(lis,size):
    for i in range(size):
        print(lis[i],end=" ")
    print("\n")

# Bubble_sort algorithms
def bubble_sort(arr, size):
    for i in range(size):
        swapped = True
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = False
        display(arr,size)
        if swapped:
            break

li = [9,8,7,6,5,4,3,2,1]
size = len(li)
bubble_sort(li,size)
display(li,size)