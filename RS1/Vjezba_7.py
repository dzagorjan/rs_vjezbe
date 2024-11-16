lozinka = input("Unesi lozinku:")

def provjera_rijec(rijec, lozinka):
    return rijec.lower() in lozinka.lower()


def provjera_lozinke(lozinka):  
    
    if len(lozinka) < 8 or len(lozinka) > 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova"
    elif lozinka.islower() or lozinka.isupper() or lozinka.isdigit():
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    elif provjera_rijec("lozinka", lozinka) or provjera_rijec("password", lozinka):
        return "Lozinka ne smije sadržavati riječ 'lozinka' ili 'password'."
    else:
        return "Lozinka je jaka."
    

print (provjera_lozinke(lozinka))
    
    

     