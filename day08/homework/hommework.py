number = int(input(" enter num: "))
if 1 < number and number <= 50:
    for i in range(number, 101, number):
        print(i)
else:
    print("სცადე თავიდან")