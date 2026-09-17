valid = []
while True:
    try:
        num = int(input("Enter a number: "))
        if num == -999:
            if len(valid) < 10:
                print("need at least 10 valid ranks, keep entering")
                continue
            else:
                break
        if num < 1 or num > 5:
            print("not in range skip")
        else:
            valid.append(num)
    except ValueError:
        print("invalid input, skip")

print('number of valid ranks:', len(valid))
print(f'average ranks:' f'{sum(valid)/len(valid):.2f}')
print('highest rank:', max(valid))





