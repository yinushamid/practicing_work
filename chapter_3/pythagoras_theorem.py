def find_pythagoras(num):
    #finding the adjacent, opposite of  hypotenus
    '''let adj, opp, and hypo, represent adjcent, opposite and hypotenus respectively'''
    for adj in range(1, num):
        for opp in range(adj, num):
            for hypo in range(opp, num):
                if (hypo*hypo) == (adj*adj) + (opp*opp):
                    print(hypo,    opp,    adj)

find_pythagoras(20)

