def range0(end, start=0, step=1):
    while start < end:
        yield start
        start += step


for i in range0(8):
    print(i)
