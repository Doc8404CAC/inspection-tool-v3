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
    nom,tol = nom_tol_input() 
    for reading in readings:
        if not in_tol(reading,nom,tol):
            bad.append(reading)
    return bad


def main():
    nom,tol= nom_tol_input()
    out_of_tol(radings,nom,tol)

print(out_of_tol([10.005,10.02,10.0,9.99,9.75]))
#[10.02,9.75]

