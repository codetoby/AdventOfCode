lines = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line)

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
sum = 0
for line in lines:
    digits = []
    value = 0
    min = -1
    max = -1
    for key in numbers:
        pos = line.find(key)
        if (pos != -1):
            digit = numbers[key]
            if (min == -1):
                min = pos
                digits.append(digit)
            elif (pos < min):
                min = pos
                if (len(digits) == 1):
                    digits.append(digit)
                    digits[0], digits[1] = digit, digits[0]
                else:
                    digits[0] = digit
                
            elif (max == -1):
                max = pos
                if (len(digits) == 2):
                    digits[1] = digit
                else:
                    digits.append(digit)
            elif (pos > max):
                max = pos
                digits[1] = digit
                   
    # print(digits)
    
    for char in line:
        if char.isdigit():
            digit = int(char)
            pos = line.find(char)

              # if (min == -1):
            #     digits.append(digit)
            # el
            if (pos < min):
                if (len(digits) == 1):
                    digits.append(digit)
                    digits[0], digits[1] = digit, digits[0]
                else:
                    digits[0] = digit
                
            elif (max == -1):
                if (len(digits) == 2):
                    digits[1] = digit
                else:
                    digits.append(digit)
                max = pos
            elif (pos > max):
                digits[1] = digit


    value += digits[0] * 10
    if (len(digits) == 1):
        value += digits[0]
    else:
        value += digits[1]

    print(digits)
    sum += value

print(sum)