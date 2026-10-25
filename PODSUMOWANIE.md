# Podsumowanie prac: PS-redesign-test

Stan na 25.10.2026. Zebrane z 12 rozmów w projekcie.

## Co zostało zrobione

### Strategia
- [PRODUCT.md](PRODUCT.md) opisuje:
  - odbiorców: dorosłych w wieku 25–50 lat, którzy zmieniają zawód;
  - cel: zapisy;
  - wyróżniki szkoły: 28 lat w rejestrze, dyplom PL/EN, dofinansowanie;
  - zakaz zmyślania opinii i liczb.

### Strona statyczna `site/` (Tailwind, generowana przez `build.py`)
- Makiety lo-fi i 13 podstron, w tym kursy, zapisy i kontakt.
- Przebudowane hero strony głównej, pasek zaufania i karty kursów. Te zmiany są w commitach.
- Sekcja CTA nad stopką ma kolory marki (magenta `#b04090`).
- Stopka ma nazwy elementów (`data-name`) zgodne z Figmą.
- Powstał podgląd nowego pierwszego ekranu w kierunku „stół przeglądowy”: [site/_podglad-ekran-1.html](site/_podglad-ekran-1.html).

### Figma (sekcja `PS lo-fi`, 7 stron)
- Warstwy i sekcje mają nazwy według roli. Stopka jest wspólnym komponentem.
- Jest krytyka hero podstrony Web Designer z propozycją skrócenia go o połowę.

### Aplikacja `app/` (Next.js i shadcn)
- Jest skonfigurowana i ma stronę Kontakt z formularzem w kolorach marki, z walidacją i zgodą RODO.

### Narzędzia
- Zainstalowane są pluginy frontend-design, Superpowers, Figma i Design oraz dashboard `/cco`.

## Co czeka
1. **Commit:** od 10.10 nic nie zostało zapisane w gicie.
2. **Decyzja o `app/.git`:** usunąć je czy zostawić osobne repozytorium.
3. **Wybór wersji docelowej:** `site/` czy `app/`.
4. **Poprawki z audytu:** wersja mobilna, kontrast i obsługa klawiatury.
5. **Hero:** wdrożyć skrócenie na stronach kierunków, a na stronie Kontakt przenieść formularz wyżej.
6. **Materiały od Ciebie:** zdjęcia prac, kolory z księgi znaku i daty naboru.
