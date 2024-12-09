def sequence_letter():
    for i in "ABCDE":
        yield i
        a  = 4
        b = 4

        yield i


for x in sequence_letter():
    print(x)