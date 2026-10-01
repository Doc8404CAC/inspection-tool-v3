
nom =float(input("nominal dimentsion "))

tol= float(input("tolerance?"))

def in_tol(reading,nom,tol):
    if nom <=0:
        raise Exception("Nominal measurement must be a positive number")
    if tol < 0:
        raise Exception("Tolerance must be a positie number")
    return reading <= (nom + tol) and reading >= (nom - tol)


def out_of_tol(readings,nom,tol):
    bad = []
    for reading in readings:
        if not in_tol(reading,nom,tol):
            bad.append(reading)
    return bad

print(out_of_tol([10.005,10.02,10.0,9.99,9.75],nom,tol))
# [10.02,9.75]
