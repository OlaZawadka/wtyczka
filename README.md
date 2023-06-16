# Wtyczka do QGIS - PyQGIS
Wtyczka użwana w programie QGIS pozwala na obliczenie przewyższenia pomiędzy dwoma wybranymi punktami oraz obliczenie pola powierzchni na podstawie współrzędnych pobranych z geometrii wybranych conajmniej trzech punktów. Obliczenia wykonywane są przy wykorzystaniu metody Gaussa.
## Minimalne wymagania sprzętowe 
- Windows 10
- QGIS 3.22
## Wymagania techniczne
Aby wtyczka była w stanie dokonać obliczeń, należy wgrać do programu "przykładowy_plik" w formacie shp ze współrzędnymi geocentrycznymi punktów, najprościej przenieść plik na pole warstw (jest to plik z wartościami atrybutów w tabeli: --> wartość tabelaryczna przedstawiona poniżej). 
## Tabela atrybutów
Jeśli dane znajdują się w pliku csv to wartości powinny być rodzielone punktorem "." oraz mieć dokładność conajmniej 3 miejsca po przecinku. Kolejność tabelaryczna danych powinna być następująca: 
```| Nr | X [m] | Y [m] | Z [m] |```
## Opis pracy wtyczki
Użytkownik musi zainstalować wtyczkę w swojej wersji QGISa.
Folder z wtyczką, po pobraniu powinien zostać przeniesiony do folderu "plugins", utworzonego automatycznie przez program QGIS ( w wyznaczonej ścieżce ) podczas instalowania aplikacji.
Warstwa z punktami powinna zostać zimportowana do programu QGIS w rozszerzeniu shp, z pliku "przykładowy_plik".
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
- wybieramy minimum trzy dowolne punkty na jednej warstwie 
- otwieramy pobraną wtyczkę 
- z rozwijanej listy wybieramy warstwę aktywną, na której znajduja się punkty 
- wybieramy przycisk 
```
Pole powierzchni
```
- otrzymujemy wynik obliczeń, z dokładnością milimetrową

## Reakcja wtyczki na błędy
#### Użytkownik wybrał mniej lub więcej punktów niż jest wymagane.
Program odpowiada: ```Nieodpowiednia liczba punktów```


