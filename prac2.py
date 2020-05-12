
def õigekiri(lause):
    õigetekst = ""
    for koma in lause:
        if koma in "et" "sest" "aga" "kuid" "vaid" "siis":
            õigetekst = õigetekst + ","
        else:
            õigetekst = õigetekst + koma
    return õigetekst

print(õigekiri(input("Sisesta tekst : ")))