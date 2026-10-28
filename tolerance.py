def nom_tol_input():
    while True:
        try:
            nom = float(input("nominal dimension "))
        except ValueError:
            print("must be a number")
            continue
        if nom < 0:
            print("nominal dimension must be a positive number")
            continue
        break
    while True:
        try:
            plus_tol = float(input("plus tolerance "))
        except ValueError:
            print("must be a number ")
            continue
        if plus_tol < 0:
            print("tolerance must be a positive number ")
            continue
        break

    while True:
        try:
            minus_tol = float(input("minus tolerance "))
        except ValueError:
            print("must be a number ")
            continue
        if minus_tol < 0:
            print("tolerance must be a positie number ")
            continue
        break
    return nom, plus_tol, minus_tol


def in_tol(reading, nom, plus_tol, minus_tol):
    return reading <= (nom + plus_tol) and reading >= (nom - minus_tol)


def out_of_tol(readings, nom, plus_tol, minus_tol):
    bad = []
    assert nom >= 0 and plus_tol >= 0 and minus_tol >= 0, (
        "values must be positive numbers"
    )
    for reading in readings:
        if not in_tol(reading, nom, plus_tol, minus_tol):
            bad.append(reading)
    return bad


def testing_out_of_tol():
    assert out_of_tol([10.005, 10.02, 10.0, 9.993, 9.75, 9.995], 10, 0.01, 0.005) == [
        10.02,
        9.993,
        9.75,
    ], "out_of_tol faided to reurn proper valuess"


def main(readings):
    nom, plus_tol, minus_tol = nom_tol_input()
    bad = out_of_tol(readings, nom, plus_tol, minus_tol)
    return bad


def testing_stats():
    assert stats([1, 7, 3, 5]) == (1, 7, 6), "stats failed"
    assert stats([10.01, 4.38962]) == (4.38962, 10.01, 5.6204), (
        "rounding in stats failed"
    )


def stats(readings):
    sort = sorted(readings)
    if readings == []:
        raise ValueError("no readings present")
    if sort[0] < 0:
        raise ValueError("values must be positive")
    low = sort[0]
    high = sort[-1]
    spread = high - low
    return low, high, round(spread, 4)


testing_out_of_tol()
print(main([10.005, 10.02, 10.0, 9.99, 9.75]))
testing_stats()
# print(stats([1.02,7.0003,5.001,3.1]))
