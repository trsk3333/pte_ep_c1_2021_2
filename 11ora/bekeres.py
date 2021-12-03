input_ertekek = []
while len(input_ertekek) == 0 or input_ertekek[-1] != "":
    input_ertekek.append(input())
input_ertekek.remove("")
print(input_ertekek)
