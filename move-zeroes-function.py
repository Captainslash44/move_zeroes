def Move_zeroes(numbers):
    index = 0
    # In this function we will be moving all numbers that are not 0
    # to the beginning instead of actually moving the zeros
    for i in range(len(numbers)):

        if numbers[i] != 0:
            # if the number is not zero, swap it with the element at count.
            numbers[index], numbers[i] = numbers[i], numbers[index]
            index += 1

    return numbers


#I've used this tedious method to enter the array
#yet it ensures that all values are valid.
numbers = []

while True:
    n = input("Please enter a number to add to list, or press 'N' to continue: ")

    if n.upper() == "N":
        break

    elif n.isdigit():
        numbers.append(int(n))

    else:
        print("Please enter a valid value.")


print(f"Original list: {numbers}")
print(Move_zeroes(numbers))