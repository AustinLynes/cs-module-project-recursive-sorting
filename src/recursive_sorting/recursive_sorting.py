# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # find the total length of both lists
    elements = len(arrA) + len(arrB)
    # allocate a list with the total length of the lists
    merged_arr = []

    # if the length of arrA is 0 then just return it...
    if len(arrA) == 0:
        return arrA
    # same with arrB
    elif len(arrB) == 0:
        return arrB

    index_left = index_right = 0

    while len(merged_arr) < elements:
        if arrA[index_left] <= arrB[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            merged_arr.append(arrA[index_left])
            index_left += 1
        else:
            # Right value bigger
            merged_arr.append(arrB[index_right])
            index_right += 1

        # If we are at the end of one of the lists we need to finish looking at the other side

        # Reached the end of right
        if index_right == len(arrB):
            # Append the remainder of left and break
            merged_arr += arrA[index_left:]
            break

        # Reached the end of left
        elif index_left == len(arrA):
            # Append the remainder of right and break
            merged_arr += arrB[index_right:]
            break

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort(arr):
    # check to make sure that there is a valid length to sort > 1
    if len(arr) <= 1:
        # if there isnt a valid length we will just return the array as is... because
        # [ 4 ] is technically sorted already

        return arr
    else:
        # saying i get a length of at least 2 [5, 9]
        # we take the length of the list and divid it by 2 rounded up to get the middle
        middle = len(arr)//2
        # seperate the left half of the list
        # everything up to the middle
        left = arr[:middle]
        # everything after the found middle
        right = arr[middle:]
        # then we call the merge function while recursivly calling either side
        return merge(merge_sort(left), merge_sort(right))

# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    arr2_start = mid + 1 
  
    if (arr[mid] <= arr[arr2_start]): 
        return 

    while (start <= mid and arr2_start <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[arr2_start]): 
            start += 1 
        else: 
            value = arr[arr2_start] 
            index = arr2_start 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1] 
                index -= 1 
              
            arr[start] = value 
  
            # Update all the pointers 
            start += 1 
            mid += 1 
            arr2_start += 1 


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 

        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        mid = l + (r - l) // 2 

        merge_sort_in_place(arr, l, mid) 
        merge_sort_in_place(arr, mid + 1, r) 

        merge_in_place(arr, l, mid, r) 
      
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
