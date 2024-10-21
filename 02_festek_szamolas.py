def festek_szamito():
    szelesseg = float(input("Add meg a szoba szélességét (méterben): "))
    hossz = float(input("Add meg a szoba hosszát (méterben): "))
    magassag = float(input("Add meg a szoba magasságát (méterben): "))
    megvasarolt_festek = float(input("Add meg a megvásárolt festék mennyiségét (literben): "))


    fal1_terulet = 2 * (szelesseg * magassag)       # Két fal területe szélesség * magasság alapján
    fal2_terulet = 2 * (hossz * magassag)           # Két fal területe hossz * magasság alapján

    teljes_falak_terulete = fal1_terulet + fal2_terulet     # A teljes falak területének kiszámítása

    # A szükséges festékmennyiség kiszámítása (1 liter = 10 négyzetméter)
    szukseges_festek = teljes_falak_terulete / 10
    print(f"A festéshez szükséges festékmennyiség: {szukseges_festek:.2f} liter")

    # Ellenőrizzük, hogy elég-e a megvásárolt festék
    if megvasarolt_festek >= szukseges_festek:
        print("Elég festék áll rendelkezésre.")
    else:
        hianyzo_festek = szukseges_festek - megvasarolt_festek
        print(f"További {hianyzo_festek:.2f} liter festék szükséges.")

festek_szamito()        # A program futtatása

