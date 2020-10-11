def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i]>b[i]:
            alice += 1 
        elif  a[i]<b[i]:
            bob +=1
        elif a[i]==b[i]:
            pass
    return [alice,bob]    
     
    
    '''a_score, b_score = 0, 0
    for i in range(3):
        a_score += a[i] > b[i]
        b_score += b[i] > a[i]
    return [a_score, b_score]'''

if __name__ == "__main__":

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
    