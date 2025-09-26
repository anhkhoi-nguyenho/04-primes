from math import sqrt

#### Fonction secondaire


def isprime(p):
    assert p >= 0, "Le nombre doit être positif"
    premier = True
    if p < 2:
        premier = False
    # La boucle ne tournera pas pour p = 2 et p = 3  car
    # sqrt(2) < 2
    # sqrt(3) < 2
    for d in range(2, int(sqrt(p)) + 1): # exclure 0 et 1 pour exclure p = p x 1
        premier = bool(p%d)
        if not premier:
            break
    return premier

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
