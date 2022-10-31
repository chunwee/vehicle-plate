# Libraries
import re

### Regex script

# text = ["EP2349Z","SPA234A","SDS3928M","PB982K","FZ1982L","ES12K","YP92G","XE2912N","GQ492P","SLN1377P","SCS12P", "Test123"]


def car(text):
        
    # List of matches
    matchesS = []
    matchesE = []
    matches_none = []

    # Regex
    S = "^S[A-Z]{0,2}[\d]{1,4}[A-Z]{1}$"    # S Cars
    E = "^E[A-Z]{0,1}[\d]{1,4}[A-Z]{1}$"    # E Cars

    for texts in text:
        s = re.search(S, texts)
        e = re.search(E, texts)

        if s:
            matchesS.append(texts)
                
        elif e:
            matchesE.append(texts)
        
        else:
            matches_none.append(texts)

    print("S-Plate Cars:", *matchesS)
    print("E-Plate Cars:", *matchesE)
    print("Not a car:", *matches_none)


# car(text)

def all_vehicles(text):
    # List of matches
    matchesS = []
    matchesE = []
    matchesF = []
    matchesG = []
    matchesP = []
    matchesY = []
    matchesX = []
    matches_none = []

    # Regex
    S = "^S[A-Z]{0,2}[\d]{1,4}[A-Z]{1}$"    # S Cars
    E = "^E[A-Z]{0,1}[\d]{1,4}[A-Z]{1}$"    # E Cars
    F = "^F[A-Z]{1,2}\d{1,4}[A-Z]{1}$"      # Motorcycles
    G = "^G[A-Z]{1,2}\d{1,4}[A-Z]{1}$"      # Light Goods Vehicles
    P = "^P[A-Z]{1}[\d]{1,4}[A-Z]$"         # Private Hires
    Y = "^Y[A-Z]{1}[\d]{1,4}[A-Z]$"         # Heavy Goods - Class 3
    X = "^X[A-Z]{1}[\d]{1,4}[A-Z]$"         # Heavy Goods - Class 4/5

    for texts in text:
        # Magic
        s = re.search(S, texts)
        e = re.search(E, texts)
        f = re.search(F, texts)
        g = re.search(G, texts)
        p = re.search(P, texts)
        y = re.search(Y, texts)
        x = re.search(X, texts)

        if s:
            matchesS.append(texts)

        elif e:
            matchesE.append(texts)

        elif f:
            matchesF.append(texts)

        elif g:
            matchesG.append(texts)

        elif p:
            matchesP.append(texts)

        elif y:
            matchesY.append(texts)

        elif x:
            matchesX.append(texts)

        else:
            matches_none.append(texts)
    

    print("S-Plate Cars:", *matchesS)
    print("E-Plate Cars:", *matchesE)
    print("Motorcycles:", *matchesF)
    print("Light Goods Vehicles:", *matchesG)
    print("Private Hires:", *matchesP)
    print("Heavy Goods Vehicles (Class 3/4):", *matchesY)
    print("Heavy Goods Vehicles (Class 5):", *matchesX)
    print("Not a Vehicle Plate:", *matches_none)



# car(text)
# all_vehicles(text)
