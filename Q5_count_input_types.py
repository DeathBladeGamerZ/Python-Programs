positive = negative = zero = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeroes:", zero)
