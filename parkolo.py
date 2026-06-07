import os

FAJLNEV = "parkolo.txt"

if not os.path.exists(FAJLNEV):
    with open(FAJLNEV, "w", encoding="utf-8") as f:
        for szektor in ["A", "B", "C"]:
            for i in range(1, 21):
                tipus = "VIP" if szektor == "A" and i <= 5 else "Normal"
                f.write(f"{szektor}{i};szabad;0;{tipus}\n")

helyek = {}
with open(FAJLNEV, "r", encoding="utf-8") as f:
    for sor in f:
        id, statusz, orak, tipus = sor.strip().split(";")
        helyek[id] = {"statusz": statusz, "orak": int(orak), "tipus": tipus}


def dijat_szamol(ora):
    return max(0, (ora - 1) * 500)

while True:
    print("\n--- PARKOLÓ --- | 1: Állapot | 2: Foglalás | 3: Távozás | 4: Mentés/Kilépés")
    valasztas = input("Válassz: ")

    if valasztas == "1":
        for id, adat in helyek.items():
            print(f"{id}: {adat['statusz']} ({adat['tipus']})")

    elif valasztas == "2":
        hely = input("Melyik hely? ").upper()
        if hely in helyek and helyek[hely]["statusz"] == "szabad":
            if helyek[hely]["tipus"] == "VIP" and input("VIP engedély (I/N)? ").upper() != "I":
                print("Nincs jogosultság!")
            else:
                ora = int(input("Hány óra (max 168)? "))
                helyek[hely].update({"statusz": "foglalt", "orak": ora})
                print(f"Fizetendő: {dijat_szamol(ora)} Ft")
        else:
            print("Hibás vagy foglalt hely!")

    elif valasztas == "3":
        hely = input("Távozás helye: ").upper()
        if hely in helyek:
            helyek[hely].update({"statusz": "szabad", "orak": 0})
            print("Felszabadítva.")

    elif valasztas == "4":
        with open(FAJLNEV, "w", encoding="utf-8") as f:
            for id, adat in helyek.items():
                f.write(f"{id};{adat['statusz']};{adat['orak']};{adat['tipus']}\n")
        break