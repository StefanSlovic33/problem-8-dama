#Python program za rješavanje problema N kraljica koristeći bektreking

k = 1
 
# Funkcija za stampanje rjesenja
def stampajResenje(tabla,n): 
 
    global k
    print(k,"Solucija")
    k = k + 1
    for i in range(n): 
        for j in range(n):
            print(tabla[i][j], end = " ")
        print()
    print()

# Funkcija koja provjerava da li kraljica
# moze biti smjestena na tabla[red][kol].
# Primijetimo da se ova funkcija poziva kada
# je vec ukupno “kol” kraljica smjesteno u kolone,
# od 0 do kol-1 pa moramo provjeriti samo
# da li je lijeva strana kraljice napadnuta
def Sigurno(tabla, red, kol,n) :
     
    # Provjeri tekucu vrstu sa lijeve strane 
    for i in range(kol): 
        if (tabla[red][i]): 
            return False
 
    # Provjeri gornju dijagonalu s lijeve strane
    i = red
    j = kol
    while i >= 0 and j >= 0:
        if(tabla[i][j]):
            return False
        i -= 1
        j -= 1
 
    # Provjeri donju dijagonalu s lijeve strane 
    i = red
    j = kol
    while j >= 0 and i < n:
        if(tabla[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True
 
# Rekurzivna pomocna funkcija za rjesavanje problema N kraljica 
def rijesiNKpom(tabla, kol,n) :
     
    # Bazni slucaj: ako su sve kolone popunjene, sve kraljice smjestene
    if (kol == n): 
        stampajResenje(tabla,n) 
        return True
 
    # razmotri ovu kolonu i pokusaj smjestiti ovu kraljicu u svim vrstama redom(pocevsi od nulte) u  koloni kol
    res = False
    for i in range(n):
     
        # provjeri da li kraljica moze biti smjestena u i-tu vrstu,tj. na tabla[i][kol]
        if (Sigurno(tabla, i, kol,n)): 
         
            #  Smjesti ovu kraljicu na tabla[i][kol]
            tabla[i][kol] = "K"
 
            # Provjeri da li postoji moguce rjesenje ako kraljicu stavimo na 
            # tekucu poziciju u koloni kol neka onda res(enje) bude True
            res = rijesiNKpom(tabla, kol + 1,n) or res
 
            #Ako smjestanje kraljice na tabla[i][kol] ne vodi 
            #do rjesenja,onda skloni kraljicu sa tabla[i][kol]
            tabla[i][kol] = 0 # BACKTRACK 
         
    # ako kraljica ne moze biti smjestena ni u 
    # jednoj vrsti u ovoj koloni, onda vrati False
    return res
 
# Ova funkcija rjesava problem N kraljica koristeci  
# backtracking. Uglavnom koristi rijesiNKpom() kako
# bi rijesila problem. Vraca False ako kraljice ne
# mogu biti smjestene, u suprotnom vraca True i 
# stampa raspored kraljica u obliku matrica.
def rijesiNK(n) :
 
    tabla = [[0 for j in range(n)] 
                for i in range(n)]
 
    if (rijesiNKpom(tabla, 0,n) == False): 
     
        print("Solution does not exist") 
        return
    return
 
#  Poziv funkcije da nadje rjesenja
rijesiNK(8) 
 
# PERMUTACIJA
'''from itertools import permutations
#N = int(input("unesi te broj dama : "))
N = 8
sol=0
cols = range(N)
for combo in permutations(cols):                      
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        print('Solution '+str(sol)+': '+str(combo))  
        print("\n".join(' O ' * i + ' K ' + ' O ' * (N-i-1) for i in combo) + "\n\n")'''

