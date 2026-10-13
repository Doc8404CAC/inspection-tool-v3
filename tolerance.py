 

def nom_tol_input():
    while True:
        try:
            nom=float(input("nominal dimension "))
        except ValueError:
            print("must be a number")
            continue
        if  nom<0:
            print("nominal dimension must be a positive number")
            continue
        break
    while True:
        try:
            tol=float(input("tolerance "))
        except ValueError:
            print("must be a number")
            continue
        if tol<0:
            print("tolerance must be a positive number ")
            continue
        break 
    return nom,tol

def in_tol(reading,nom,tol):
    return reading <= (nom + tol) and reading >= (nom - tol)

def out_of_tol(readings,nom,tol):
    bad = [] 
    assert nom >=0  and tol >=0, "values must be positive numbers"
    for reading in readings:
        if not in_tol(reading,nom,tol):
            bad.append(reading)
    return bad
    
def testing_out_of_tol():
    assert out_of_tol([10.005,10.02,10.0,9.99,9.75],10,.01)==[10.02,9.75], "out_of_tol faided to reurn proper valuess"
    return  
    

def main(readings):
    nom,tol= nom_tol_input()
    bad = out_of_tol(readings,nom,tol)
    return bad

def testing_stats():
    assert stats([1,7,3,5])==(1,7,6), "stats failed"
    assert stats([1.02,7.0003,5.001,3.1])==(1.02,7.0003,5.9803), "rounding in stats failed"
    return

def stats(readings):
    sort =  sorted(readings)
    if readings == []:
        raise ValueError("no readings present")
    if sort[0]<0:
        raise ValueError("values must be positive")
    low = sort[0]
    high = sort[-1]
    spread =  high - low
    return low,high,round(spread,4)

testing_out_of_tol()
#print(main([10.005,10.02,10.0,9.99,9.75]))
testing_stats()
print(stats([1.02,7.0003,5.001,3.1]))
