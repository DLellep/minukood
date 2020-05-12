tehe = input("Sisesta millist tehet tahad ")

arv1 = float(input("Sisesta mingi arv "))
arv2 = float(input("Sisesta teine arv "))

if tehe == "liitmine":
    vastus = arv1 + arv2
else:
    vastus = arv1 - arv2
    
print("Vastus on " + str(vastus))