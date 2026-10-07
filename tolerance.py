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
    assert out_of_tol([10.005,10.02,10.0,9.99,9.75],10,.01)==[10.02,9.75]
    return "this is a test" 
    

def main(readings):
    nom,tol= nom_tol_input()
    bad = out_of_tol(readings,nom,tol)
    return bad

print(main([10.005,10.02,10.0,9.99,9.75]))
print(testing_out_of_tol())
print(out_of_tol([10.005,10.02,10,9.99,9.75],-10,.01))
print(out_of_tol([10.005,9.99,9.75],10,-.01))

