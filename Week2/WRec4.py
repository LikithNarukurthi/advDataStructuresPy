def bs(data, key):
    low = 0
    high = len(data) - 1
    while low <= high:                  # 221910307033 (Likith Narukurthi)
        mid = (low + high) // 2
        if key == data[mid]:
            return True
        elif key < data[mid]:           # 221910307033 (Likith Narukurthi)
            high = mid - 1
        else:
            low = mid + 1
    return False


seq = [int(i) for i in input("Enter the list elements:").split()]
print(seq)
print(bs(seq, int(input("Enter number to be searched: "))))
