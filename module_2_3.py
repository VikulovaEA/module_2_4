list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(list):
    if list[index] < 0:
        break
    if list[index] > 0:
        print(list[index])
    index += 1