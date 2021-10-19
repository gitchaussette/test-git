liste2 = [45,34,21,14,98]

def moy_liste() : 
    v=0
    r=len(liste2)
    for all_values in liste2 : 
        v=v+all_values/r
    return v 

print(moy_liste())

def maxi_liste(list) :

    maxi = list[0]

    for maxi_values in list :

        if maxi_values >= maxi :

            maxi_values = maxi

        return maxi_values 

print(maxi_liste(liste2))



phrase = "Vous etes beau"
def carac() :
    for m in phrase : 
        while m == "e" :
            return(m)

print(carac())

def positif () : 
    for n in liste2 : 
        if n < 0 : 
            return "Négatif"
        elif n == 0 : 
            return "Nul"
        else : 
            return "positif"

print(positif())