def nom_input():
    nom =float(input("nominal dimension "))
    if nom <0:
        print("nominal must be a positive number")
        nom_input() 
    return nom

def tol_input():
    tol=float(input("tolerance "))
    if tol<0:
        print("tolerance must be a positive number")
        tol_input()
    return tol

def in_tol(reading,nom,tol):
    return reading <= (nom + tol) and reading >= (nom - tol)

def out_of_tol(readings,nom,tol):
    bad = []
    for reading in readings:
        if not in_tol(reading,nom,tol):
            bad.append(reading)
    return bad

print(nom_input())
#print(out_of_tol([10.005,10.02,10.0,9.99,9.75]))
#[10.02,9.75]
#print(nominal_tol_input([10.005,10.02,9.99,9.75]))
