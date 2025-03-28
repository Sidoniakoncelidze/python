word = input("enetr word: ")
reversed_string = " "

count = 0
for i in word:
    count += 1
if count == 3:
    for i in word:
        reversed_string = i + reversed_string
    print(reversed_string == word)
else:
    print("უნდა შემოიტანო სამ სიმბოლოიანი სიტყვა")
  