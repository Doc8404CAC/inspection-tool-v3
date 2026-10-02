while True:
    nom =float(input("nominal dimentsion "))          
    if nom <0:
        print("nominal must be a positive number")
        continue
    tol= float(input("tolerance?"))
    if tol <0:
        continue
        print("tolrance must be a positie number")
    break



def in_tol(reading,nom,tol):
    return reading <= (nom + tol) and reading >= (nom - tol)

def out_of_tol(readings,nom,tol):
    bad = []
    for reading in readings:
        if not in_tol(reading,nom,tol):
            bad.append(reading)
    return bad

print(out_of_tol([10.005,10.02,10.0,9.99,9.75],nom,tol))
# [10.02,9.75]
