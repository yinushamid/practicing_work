def sum_exponiential():
    e = 1
    n = 1
    factorial= 1
    for terms in range(1, n+1):
        factorial *= terms
        n += 1
        e += (1/factorial)
        print(e)
sum_exponiential()



