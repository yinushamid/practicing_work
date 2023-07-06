def pi_terms(nth_terms):
    series = 3
    pi = 4
    nth_series = 0
    for denominator in range(3, nth_terms + 3):
        pi_series = ((-1)**series)*(4/denominator)
        if denominator % 2 == 1:
            series += 1
            pi += pi_series
        
            if round(pi, 2) == 3.14:
                print(pi, ' is in ', denominator, 'terms', sep='' )
pi_terms(10000)         