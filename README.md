# Wtyczka do QGIS - PyQGIS
Wtyczka użwana w programie QGIS pozwala na obliczenie przewyższenia pomiędzy dwoma wybranymi punktami oraz obliczenie pola powierzchni na podstawie współrzędnych wybranych trzech. Obliczenia wykonywane są przy wykorzystaniu metody Gaussa.
## Minimalne wymagania sprzętowe 
- Windows 10
- QGIS 3.22
## Wymagania techniczne
Aby wtyczka była w stanie dokonać obliczeń, należy wgrać do programu plik w formacie csv ze współrzędnymi punktów. 
Kolejność danych: ```Nr   X    Y    Z```
Dane w pliku csv powinny być rodzielone punktorem "." oraz mieć dokładność conajmniej 3 miejsca po przecinku, aby program zadziałał prawidłowo.
## Opis pracy wtyczki
Użytkownik musi zainstalować wtyczkę w swojej wersji QGISa.
#### Oblicznie przewyższenia
- wybieramy dwa dowolne punkty na jednej warstwie
- otwieramy pobraną wtyczkę
- z rozwijanej listy wybieramy warstwę aktywną, na której znajduja się punkty 
- wybieramy przycisk 
```
Przewyższenie
```
- otrzymujemy wynik obliczeń, z dokładnością milimetrową
#### Obliczenie pola powierzchni
- wybieramy trzy dowolne punkty na jednej warstwie 
- otwieramy pobraną wtyczkę 
- z rozwijanej listy wybieramy warstwę aktywną, na której znajduja się punkty 
- wybieramy przycisk 
```
Pole powierzchni
```
- otrzymujemy wynik obliczeń
## Przykładowe wyniki
#### Przewyższenie między punktami 10004.0 i 10005.0 wynosi:
```
-0.071 m
```
#### Pole powierzchni między punktami:
```
coś m^2
```
## Reakcja wtyczki na błędy
#### Użytkownik wybrał mniej lub więcej punktów niż jest wymagane.
Program odpowiada ```Nieodpowiednia liczba punktów```


