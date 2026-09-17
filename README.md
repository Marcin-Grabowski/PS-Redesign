# Publishing School — redesign strony

Prototyp nowej strony szkoły grafiki komputerowej Publishing School.

## Struktura

| Ścieżka | Zawartość |
|---|---|
| `site/` | Implementacja desktop na podstawie makiet (Tailwind CSS) |
| `site/build.py` | Generator stron: komponenty wielokrotnego użytku + składanie podstron |
| `site/assets/tailwind.config.js` | Konfiguracja Tailwinda (font, promienie, cień) |
| `site/assets/app.js` | Interakcje: menu, przełącznik ceny, filtry, zakładki, karuzela, galeria |
| `*.html` w katalogu głównym | Wcześniejsze makiety lo-fi |
| `copy-deck.md` | Teksty na strony |

## Uruchomienie

```bash
cd site && python3 build.py          # przebudowanie stron po zmianach w komponentach
python3 -m http.server 8765          # z katalogu głównego repozytorium
```

Strona: http://localhost:8765/site/index.html
