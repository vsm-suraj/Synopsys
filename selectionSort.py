def selectionSort(lst):
    size = len(lst)
    for i in range(size):
        index = i #To store the index of minimum value
        for j in range(i,size):
            if lst[index] > lst[j]:
                index = j
        lst[i], lst[index] = lst[index], lst[i] # Swapping

# To take the user inputs
lst = [int(num) for num in input('enter the list: ').split()]

# Calling selectionSort function
selectionSort(lst)

print('='*50)
print('After Selection Sorting List is:')

# TO print the sorted list
for i in lst:
    print(i, end=' ')