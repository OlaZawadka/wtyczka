# Wtyczka do QGIS - PyQGIS
Wtyczka użwana w programie QGIS pozwala na obliczenie przewyższenia pomiędzy dwoma wybranymi punktami oraz obliczenie pola powierzchni na podstawie współrzędnych wybranych trzech lub czterech punktów. Obliczdenia wykonywane są przy wykorzystaniu metody Gaussa.
## Minimalne wymagania sprzętowe 
- Windows 10
- QGIS 3.24
## Wymagania techniczne
Aby wtyczka była w stanie dokonać obliczeń, należy wgrać do programu plik w formacie csv ze współrzędnymi punktów. 
Kolejność danych: ```Nr   X    Y    Z```
## Opis pracy wtyczki
Użytkownik musi zainstalować wtyczkę w swoiej wersji QGISa.
#### Oblicznie przewyższenia
- wybieramy dwa dowolne punkty na jednej warstwie
- otwieramy pobraną wtyczkę
- wybieramy przycisk
```
Oblicz przewyższenie
```
- otrzymujemy wynik obliczeń
#### Obliczenie pola powierzchni
- wybieramy trzy lub cztery dowolne punkty na jednej warstwie 
- otwieramy pobraną wtyczkę 
- wynieramy przycisk 
```
Oblicz pole powierzchni
```
- otrzymujemy wynik obliczeń
## Przykładowe wyniki
#### Przewyższenie
```
coś
```
#### Pole powierzchni
```
coś
```
## Reakcja wtyczki na błędy
#### Użytkownik wybrał mniej punktów niż jest wymagane
Program odpowiada ```Wybrano za mało punktów```
#### Użytkownik wybrał więcej punktów niż jest wymagane 
Program odpowiada ```Wybrano za dużo punktów```

