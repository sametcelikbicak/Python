import sys

#print(dir(sys))

# a = int(input("a:"))
# b = int(input("b:"))
# sys.exit()
# c = int(input("c:"))

# sys.stderr.write("bu bir hata mesajıdır\n")
# sys.stderr.flush()
# sys.stdout.write("bu normal bir yazıdır\n")
# print(sys.argv)
# for i in sys.argv:
#     print(i)

def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        print("Reel kök yok")
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (x1,x2)


if len(sys.argv) == 4:
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin\n")
    sys.stderr.flush()
