d=int(input("Donnez l'heure de début de la location (en heures) : "))
f=int(input("Donnez l'heure de fin de la location (en heures ) : "))
if d == f :
    print("Attention ! l'heure de fin est identique à l'heure de début.\n")
elif d > f :
        print("Attention ! le début de la location est après la fin...\n")
elif (d < 0 or d > 24) or (f < 0 or f> 24) :
    print("Les heures doivent êtres comprises entre 0 et 24 !\n")
