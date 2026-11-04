def mediane(valeurs):
    if not valeurs:
        raise ValueError("mediane() a besoin d'au moins une valeur")
    triees = sorted(valeurs)
    n = len(triees)
    milieu = n // 2
    if n % 2 == 1:
        return triees[milieu]
    return (triees[milieu - 1] + triees[milieu]) / 2
