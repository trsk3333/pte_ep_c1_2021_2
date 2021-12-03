def bekeres() -> str:
    return input("Hogy hívnak?\n")

def koszon(nev="") -> None:
    print(f"Szia {nev}")


koszon()
koszon(bekeres())
