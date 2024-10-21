def ajandekcsomagolo():
    hossz = float(input("Add meg az ajándék hosszát (cm-ben): "))
    szelesseg = float(input("Add meg az ajándék szélességét (cm-ben): "))
    magassag = float(input("Add meg az ajándék magasságát (cm-ben): "))
    ajandekok_szama = int(input("Add meg az ajándékok számát: "))
    szalag_hossz = float(input("Add meg a rendelkezésre álló szalag hosszát (méterben): "))

    # A szalag hossza
    kerulet1 = 2 * (hossz + szelesseg)
    kerulet2 = 2 * (hossz + magassag)

    # A teljes szalag hossza egy ajándékra (a két kerület plusz 50 cm a masnihoz)
    szalag_egy_ajandekra = kerulet1 + kerulet2 + 50

    # A szalag teljes hossza az ajándékok számának megfelelően
    szukseges_szalag_cm = szalag_egy_ajandekra * ajandekok_szama
    szukseges_szalag_meter = szukseges_szalag_cm / 100              # Átváltás méterbe

    print(f"Az ajándékok csomagolásához szükséges szalag: {szukseges_szalag_meter:.2f} méter")

    # Ellenőrizzük, hogy elég-e a rendelkezésre álló szalag
    if szalag_hossz >= szukseges_szalag_meter:
        print("Elég szalag áll rendelkezésre.")
    else:
        print("Nincs elég szalag a művelethez, további szalag szükséges.")

ajandekcsomagolo()                # A program futtatása
