def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
        
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
                
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr_size = int(input("Enter size of array: "))
arr = []

for i in range(arr_size):
    take_user = int(input("Enter value: "))
    arr.append(take_user)

print("\nUnsorted array is: {}".format(arr))
size = len(arr)
selectionSort(arr, size)
print("\nSorted array is: {}".format(arr))
