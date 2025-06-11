def merge_sort(list):
    """
    sorts a list in ascending order.
    returns a new sorted list.

    divide: find a midpoint of the list and divide into sublists.
    conquer: recursively sort the sublists created in previous step.
    combine: merge the sorted sublists created in previous step.
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):

    """
    divide the unsorted list at midpoint into sublists.
    returns two sublists - left and right. 
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    merges two list(arrays), sorting them in the process 
    returns a new merged list.
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1

        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])

    while j < len(right):
        l.append(right[j])

    return l


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
z = merge_sort(alist)
print(z)