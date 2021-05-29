# For sorted, nearly sorted or reversed sorted cases quicksort takes n^2 comparions
# For average cases it takes nlogn comparisons

# average case O(nlogn)
# worst case O(n^2)

def quick_sort(array):
    print('calling quick_sort function...')

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smallers_than_pivot = [i for i in array[1:] if i <= pivot]
        biggers_than_pivot = [i for i in array[1:] if i > pivot]

        return quick_sort(smallers_than_pivot) + [pivot] + quick_sort(biggers_than_pivot)

print(quick_sort([0,1,5,8,7,20,1,90,0])) # average case: 11 recursions
print(quick_sort([9,8,7,6,5,4,3,2,1])) # wrost case: 17 recursions
print(quick_sort([1,2,3,4,5,6,7,8,9])) # best case: 17 recursions
