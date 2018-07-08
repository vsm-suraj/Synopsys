def insertionSort(lst):
    size = len(lst)
    for i in range(1, size):
        val = lst[i]
        j = i-1
        
        # Shifting the element by one position if val i small
        while j>=0 and val<lst[j]:
            lst[j+1] = lst[j] # changing position till val is greater
            j -= 1
        lst[j+1] = val # After shifting assigning the val

# To take the user inputs
lst = [int(num) for num in input('enter the list: ').split()]

# Calling insertionSort function
insertionSort(lst)

print('='*50)
print('After insertion Sorting List is:')

# TO print the sorted list
for i in lst:
    print(i, end=' ')
