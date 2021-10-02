#!/usr/bin/env python
print('hoi')
print('ik ben python')
print('hoe heet jij?')
naam = input()

if naam == 'nils':
    print('hallo baas')
else:
     print('hoi',naam)
print('wat kan ik voor je doen')
while True:
    doen = input()
    if doen == '':
        print('dit is geen optie')
        print('probeer iets anders')
    elif doen == 'eet een blokje kaas':
        print('chomp chomp')
    elif doen == 'niks':
        exit()
   
