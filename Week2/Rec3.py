def binary_search(data, key, low, high):
    if low > high:
        return False
    else:                                                               # 221910307033 (Likith Narukurthi)
        mid = (low + high) // 2
        if key == data[mid]:
            return True
        elif key < data[mid]:
            return binary_search(data, key, low, mid - 1)               # 221910307033 (Likith Narukurthi)
        elif key > data[mid]:
            return binary_search(data, key, mid + 1, high)
        else:
            return False


seq = [int(i) for i in input("Enter the list elements:").split()]
print(seq)
print(binary_search(seq, int(input("Enter number to be searched: ")), 0, len(seq) - 1))



