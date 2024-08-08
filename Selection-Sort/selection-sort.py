
# display list value
def display(lis,size):
    for i in range(size):
        print(lis[i],end=" ")
    print("\n")

# Selection Sort the list
def selection_sort(arr,size):
    for i in range(size):
        temp = i
        for j in range(i+1,size):
            if arr[temp] > arr[j]:
                temp = j
        if temp != i:
            test = arr[i]
            arr[i] = arr[temp]
            arr[temp] = test

li = [9,8,7,6,5,4,3,2,1]
size = len(li)
selection_sort(li,size)
display(li,size)