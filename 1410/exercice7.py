n = 12

# partie 1

# Lire N (N est un entier)
# Si N >= 5 alors
# P <- 700 + 170*N
# FIN
# Si sinon P <- 700 + 210*N
# FIN
# Afficher P, Afficher N


# partie 2

# Lire N (N est un entier)
# Si N >= 5 alors
# P <- 700 + 170*N
# FIN
# Si sinon P <- 700 + 210*N
# FIN
# Afficher P / N


# partie 3

print()

if n >= 5:
    p = 700 + 170*n
else :
    p = 700 + 210*n
print("Prix par personne : " + str((p/n)) + " €, pour un groupe de " + str(n) + " personnes.")

print()