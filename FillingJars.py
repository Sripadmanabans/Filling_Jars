def filling_jars(n, m):
    total = 0
    for i in range(m):
        temp2 = raw_input()
        abk = [int(j) for j in temp2.split()]
        if abk[1] > abk[0]:
            total += abk[2] * (abk[1] - abk[0] +1)
        else:
            total += abk[2] * (abk[0] - abk[1] +1)

    average = total / n

    print average    

temp = raw_input()
nm = [int(i) for i in temp.split()]

filling_jars(nm[0], nm[1])
