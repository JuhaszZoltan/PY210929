# \\pdc\Diakkaptar\Juhász Zoltán\

# 1/16
homerseklet = int(input('kinti homerseklet: '))
if homerseklet < 0: print('odakint fagy')
else: print('nem fagy')

#1/17
szam = int(input('irj be egy szamot: '))
if szam % 2 == 0: print('páros')
else: print('páratlan')

#1/18
szam = int(input('irj be egy szamot: '))

if szam == 0: print('egyik sem')
elif szam < 0: print('a szam negativ')
else: print('a szam pozitiv')

szam1 = int(input('ird be az elso szamot: '))
szam2 = int(input('ird be az masodik szamot: '))

if szam1 == szam2: print(f'{szam1} = {szam2}')
elif szam1 > szam2: print(f'{szam1} > {szam2}')
else: print(f'{szam1} < {szam2}')