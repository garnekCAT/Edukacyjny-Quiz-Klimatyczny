# Ten projek jest edukacyjnym quizem klimatycznym, zapraszam do dokumentacji !

## Spis treści

## O projekcie
Projek ten został stworzony jako projekt kmońcowy na kursie Kodland i nazewnictwo niektórych elementów może być sprzeczne z ich funkcją, niektóre części kodu też mogą być zbędne do normalnej operacji kodu.
Jest tak dlatego, że ten projekt bazuje na innym projekcie z odmienną funkcją od tego i jest jego bardzo mocno zmodyfikowaną wersją tamtego projektu.

## Jak zainstalować
1. Pobierz wszystkie pliki z folderu Quiz
2. Otwórz ten plik w swoim IDE (np. Visual Studio Code)
3. Zainstaluj Flask wpisując w terminal ```pip install flask```
4. Uruchom plik main.py
​
## Jak dostosować do swoich potrzeb
- zawiera wybrane informacje dotyczące edytowania quizu
### Aby dodawać pytania
1. Znajdź podstronę, w której chcesz dodać pytanie
2. Zlokalizuj to pytanie
3. Skopiuj kod odpowiedzialny za pytanie (patrz poniżej)
```html
      <li class="list__item">
        <form action="/pyt11" method="POST">
            <input type="hidden" name="score" value="{{ score }}">
            <button type="submit" class="list__item"><span> TWOJE PYTANIE TU </span></button>
        </form>
      </li>
```
- Mała uwaga - jak chcesz, by to pytanie dodawało punkty, to musisz w ```value="{{ score }}``` zmienić ```{{ score }}``` na ```{{ score | int + 10}}```. To doda graczowi 10 punktów.

### Aby zmienić tło
- Mała uwaga - po zmianie tła w ```style.css``` tło nie będzie takie same jak w ```style1.css``` i ```sytle2.css```, ale wszystko jest tam w niemal identycznych miejscach.
1. Znajdź w ```style.css``` linijkę nr. 10
2. Znajdź sobie zdjęcie / kolory do gradientu / kolor tła, dodatkowo możesz dodać swój obrazek.
(opcjonalne) 3. Jeśli nie masz żadnego zdjęcia na tło to usuń ```url("../img/Ziemia.png"),```. Przecinek też trzeba usunąć !
4. Zastąp *Ziemia.png* swoją nazwą zdjęcia jeśli je masz, pamiętając o jego rozszeżeniu (np .jpg)
5. Zmień faktyczne tło na obraz korzystając z ```url("../img/ OBRAZEK ")``` lub na pojedyńczy kolor używając ```background-color: #KOLOR;```i zastępując *KOLOR* kolorem



























































































