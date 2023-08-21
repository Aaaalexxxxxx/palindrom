text = input("введите строку:")
line = ''.join(reversed(text))
if text == line:
    print("True")
else:
    print("False")