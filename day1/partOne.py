lines = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line)

sum = 0

for line in lines:
    digits = []
    value = 0
    for char in line:
        if char.isdigit():
            digit = int(char)
            if (len(digits) == 0):
                digits.append(digit)
                value += digit * 10
            elif (len(digits) == 1):
                digits.append(digit)
            else:
                digits[1] = digit

    if (len(digits) == 1):
        value += digits[0]
    else:
        value += digits[1]

    sum += value

print(sum)
