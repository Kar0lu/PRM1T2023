# Porównanie algorytmów przeszukiwania grafów
## Cel projektu
Projekt ma na celu zobrazowanie oraz porównanie następujących algorytmów przeszukiwania grafów:
- Depth-first search (DFS)
- Breadth-first search (BFS)
## Wymagania
```
matplotlib==3.7.1
networkx==3.1
```
## Sposób porównania
Program tworzy animację obrazującą działanie powyższych algorytmów na (pseudo)losowo generowanym grafie. Animacja przechodzi krok po kroku przez algorytm, kolorując odpowiednie węzły w zależności od tego, co się aktualnie z nimi dzieje. Ponad to na wykresie przedstawione są informacje:
- liczba nieodkrytych węzłów
- liczba węzłów znajdujących się na stosie (do odkrycia)
- liczba węzłów odkrytych
- krok działania algorytmu (w ilu krokach znaleziono szukany element)
- dystans szukanego węzła od węzła startowego
## Porównanie
<table width="100%" >
  <thead>
    <tr>
      <th width="20%"></th>
      <th width="40%">Depth-first search (DFS)</th>
      <th width="40%">Breadth-first search (BFS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="20%">Animacja</td>
      <td width="40%"><img src="https://github.com/Kar0lu/PP/blob/main/dfs.gif"/></td>
      <td width="40%"><img src="https://github.com/Kar0lu/PP/blob/main/bfs.gif"/></td>
    </tr>
    <tr>
      <td width="20%">Złożoność czasowa (V - liczba węzłów, E - liczba krawędzi)</td>
      <td width="40%">O(V + E)</td>
      <td width="40%">O(V + E)</td>
    </tr>
    <tr>
      <td width="20%">Złożoność pamięciowa (V - liczba węzłów, E - liczba krawędzi, H - długość najdłuższej prostej ścieżki)</td>
      <td width="40%">O(H)</td>
      <td width="40%">O(V + E) - jeżeli graf wejściowy jest reprezentowany za pomocą listy sąsiedztwa, O(V^2) - jeżeli graf wejśiowy jest reprezentowany za pomocą macierzy sąsiedztwa</td>
    </tr>
    <tr>
      <td width="20%">Zupełność</td>
      <td width="40%">Tylko dla grafów skończonych (bez pętli)</td>
      <td width="40%">Kompletny</td>
    </tr>
  </tbody>
</table>

## Opis szczegółowy
Warto zauważyć że przedstawiony program nie służy jedynie do znajdowania szukanych elementów w grafie, więc posiada wiele kodu który byłby nadmiarowy gdyby chodziło nam o samą efektywność korzystania. Przechowuje on informacje o kolejnych krokach działania algorytmów, oraz co się dzieje z różnymi listami w trakcie ich wykonywania.
### W programie występują 3 moduły pomocnicze:
<details>
<summary>generate_graph.py</summary>
  <br/>W tym module znajduje się funkcja generująca (pseudo)losowy graf. Nie ma w nim zapętleń.<br/><br/>

  **Dane wejściowe:**
  
  - liczba węzłów
  - maksymalna liczba krawędzi wychodzących z jednego węzła
  - seed

  **Dane wyjściowe:**

  - (pseudo)losowy graf

</details>
<details>
<summary>search_algorthms.py</summary>
  <br/>W tym module znajdują się dwie funkcje przeszukiwania grafu (BFS i DFS)<br/><br/>
  
  **Dane wejściowe:**
  
  - graf
  - węzeł szukany
  - węzeł startowy

  **Dane wyjściowe:**

  - zapis kroków wykorzystywanego algorytmu
  - ścieżka powrotna z węzła końcowego do startowego

</details>
<details>
<summary>my_animations.py</summary>
  
  <br/>W tym module znajduje się funkcja rysująca graf oraz tworząca animację przy wykorzystaniu bibliotek takich jak networkx i matplotlib.<br/>
  
  **Dane wejściowe:**
  
  - graf
  - zapis kroków wykorzystywanego algorytmu
  - ścieżka powrotna z węzła końcowego do startowego
  - prędkość animacji

  **Dane wyjściowe:**

  - brak

</details>

### Program wykonuje się przez main.py, który działa w następujący sposób:
<ol>
  <li>
    Deklaruje i waliduje stałe globalne:
  </li><br/>
  <ul>
    <li>liczba węzłów w grafie</li>
    <li>maksymalna liczba nowych rozgałęzień z jednego węzła</li>
    <li>węzeł startowy</li>
    <li>węzeł szukany</li>
    <li>prędkość animacji</li>
    <li>seed</li>
  </ul><br/>
  <li>Generuje losowy graf</li>
  <li>Przeszukuje graf za pomocą dostępnych funkcji, po czym otrzymuje od nich zapis działania algorytmu krok po kroku, oraz ścieżkę powrotną od szukanego węzła do startu, jeżeli znaleziono węzeł</li>
  <li>Tworzy animację na podstawie zapisu działania algorytmu</li>
  <li>Wyświetla użytkownikowi animację działania algorytmów DFS i BFS na tym samym grafie i w tym samym czasie</li>
</ol>


## Literatura
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=lbp
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=lbp
- https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
