#5) გამოიტანეთ ჯერ False, შემდეგ True, შემდეგ False, True, False... და ასე 1000-ჯერ
for i in range(1000):
    print(False if i % 2 == 0 else True)