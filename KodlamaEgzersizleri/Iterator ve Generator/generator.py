def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for sayi in fibonacci():
    if(sayi > 100000):
        break
    print(sayi)