olom_area = 18
rez_area = 23

olom_suruseg = 11.34
rez_suruseg = 8.69

olom_m = olom_suruseg * olom_area
rez_m = rez_suruseg * rez_area

if olom_m<rez_m:
    print("A réz a nehezebb")
else:
    print("Az ólom a nehezebb")