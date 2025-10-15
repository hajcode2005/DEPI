sum = 0
count = 0
while True:
    select = input("1 to enter a number and 'done' to stop: ")
    if select == 'done':
        break
    elif select == '1':
        number = input("Enter a number: ")
        if number.isdigit():
            sum += int(number)
            count += 1
        else:
            print("Invalid input")
            continue
    else:
        print("Invalid input")
        continue
if count > 0:
    print("The sum is:", sum)
    print("The average is:", sum / count)
else:
    print("No numbers entered.")