import math

haromszog_egyik = int(input("Kérem a háromszög egyik oldalát: "))
haromszog_masik = int(input("Kérem a háromszög másik oldalát: "))
haromszog_harmadik = int(input("Kérem a háromszög harmadik oldalát: "))
kerulet = haromszog_harmadik + haromszog_masik + haromszog_egyik
d = (haromszog_masik + haromszog_harmadik + haromszog_egyik) / 2
e = (d * (d - haromszog_egyik) * (d - haromszog_masik) * (d - haromszog_harmadik))
print("Kerület:", kerulet)
print("Terület:", math.sqrt(e))
