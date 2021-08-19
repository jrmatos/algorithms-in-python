from data import average, best, worst

# TODO: improvements
def bubble_sort(arr):
    for i in range(len(arr)):
        print("===")
        for j in range(len(arr)):
            print("i: {} arr[i]: {}".format(i, arr[i]))
            print("j: {} arr[j]: {}".format(j, arr[j]))

            if arr[j] > arr[i]:
                print("trocou")
                arr[i], arr[j] = arr[j], arr[i]

            print("___")
    
    return arr

print(worst[:3])
print(bubble_sort(worst[:3]))