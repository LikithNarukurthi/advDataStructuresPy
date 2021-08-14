def factorial(n):
    if n == 0:
        return 1
    else:                                           # 221910307033 (Likith Narukurthi)
        return n * factorial(n - 1)


print(factorial(int(input("Enter the desired num: "))))
