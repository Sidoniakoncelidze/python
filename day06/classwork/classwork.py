number = int(input("enter your number: "))

if number >= 2:
    for num in range(2, number):
        print("არ არის ეს მარტივი რიცხვი")
        break
    else:
        print("მარტივი რიცხვი")
else:
    print("არ არის მარტივი")
