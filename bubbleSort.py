def bubbleSort(lst):
    size = len(lst) # To store the size of list
    for i in range(size):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] # Swapping

# To take the user inputs
lst = [int(num) for num in input('enter the list: ').split()]
bubbleSort(lst)

print('='*50)
print('After Bubble Sorting List is:')

# TO print the sorted list
for i in lst:
    print(i, end=' ')