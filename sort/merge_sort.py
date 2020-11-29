def merge_sort(l: list):
    """
    In place depth first search sort with O(n) extra space since slicing object takes extra memory
    Time Complexity is O(nlogn)
    """
    if len(l) <= 1:
        return

    # Round-down strategy when splitting list
    mid_index = len(l) // 2
    list1 = l[:mid_index]
    list2 = l[mid_index:]
    merge_sort(list1)
    merge_sort(list2)

    i1 = 0
    i2 = 0
    l1 = len(list1)
    l2 = len(list2)
    i_sum = 0
    while i_sum < l1 + l2:
        if i1 >= l1:
            l[i_sum] = list2[i2]
            i2 += 1
        elif i2 >= l2:
            l[i_sum] = list1[i1]
            i1 += 1
        else:
            if list1[i1] < list2[i2]:
                l[i_sum] = list1[i1]
                i1 += 1
            else:
                l[i_sum] = list2[i2]
                i2 += 1
        i_sum = i1 + i2
