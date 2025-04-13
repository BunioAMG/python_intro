# Raport – Lab 4: Wprowadzenie do biblioteki pymcdm
## 1. Opis analizy

Celem tej analizy było porównanie czterech modeli laptopów (A1–A4) z perspektywy użytkownika biznesowego. Do oceny wykorzystano pięć praktycznych kryteriów:

| Kryterium       | Typ           |
|------------------|----------------|
| Cena (zł)        | Minimalizuj    |
| Wydajność        | Maksymalizuj   |
| Bateria (h)      | Maksymalizuj   |
| Waga (kg)        | Minimalizuj    |
| Pamięć (GB SSD)  | Maksymalizuj   |

Typy kryteriów zostały określone w kodzie jako:
```python
types = np.array([-1, 1, 1, -1, 1])

2. Macierz decyzyjna
Laptopy zostały ocenione na podstawie następujących danych:

        Cena	Wydajność	Bateria	    Waga	Pamięć
A1	3400	3200	        8	    1.4	        512
A2	4200	3600	        12	    1.7	        1024
A3	3900	3100	        9	    1.5	        512
A4	4600	4000	        11	    1.8	        2048

Wagi zostały wyznaczone automatycznie metodą entropii:
[0.0296, 0.0257, 0.0623, 0.0242, 0.8582]
Jak widać, największą wagę otrzymało kryterium pojemności dysku

3. Zastosowane metody
Do oceny zastosowałem trzy popularne metody wielokryterialne:

TOPSIS – wybór oparty na odległości od ideału,

SPOTIS – stabilny porządek preferencji,

VIKOR – metoda kompromisowa.

Wszystkie dane zostały znormalizowane metodą min-max. Wagi zostały policzone automatycznie, co zapewnia obiektywną ocenę każdego kryterium.

4. Wyniki
Poniżej znajdują się końcowe wyniki oraz miejsca w rankingu dla każdej metody:

Alternatywa	TOPSIS	SPOTIS	VIKOR	    Rank_TOPSIS	    Rank_SPOTIS	    Rank_VIKOR
A1	        0.0427	0.9433	0.9968	         3	        3	        3
A2	        0.3386	0.6215	0.6412	         2	        2	        2
A3	        0.0332	0.9490	1.0000	         4	        4	        4
A4	        0.9542	0.0694	0.0000	         1	        1	        1

5. Wnioski
Wszystkie trzy metody były zgodne – najlepszy okazał się laptop A4.

A4 zdobył najwyższe noty za wydajność, baterię i (co najważniejsze) pojemność dysku – co było też najmocniej punktowane przez wagę entropii.

Najsłabiej wypadł A3 – miał najniższą wydajność i pojemność, co go zepchnęło na ostatnie miejsce.

Spójność między rankingami świadczy o tym, że analiza była solidna i dobrze skonfigurowana.

Autor: Patryk Buńkowski
