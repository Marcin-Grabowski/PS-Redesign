"""Generator stron Publishing School (desktop).

Każda funkcja w sekcji KOMPONENTY zwraca fragment HTML z klasami Tailwinda.
Strony są składane z komponentów w sekcji STRONY i zapisywane obok tego pliku.
Uruchom:  python3 build.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = '+48 504 068 626'
PHONE_HREF = 'tel:+48504068626'

# Wspólne klasy komponentów (@apply). Kolory wyłącznie z palety Tailwinda.
COMPONENT_CSS = """
@layer components {
  .container-page { @apply mx-auto w-full max-w-7xl px-10; }
  .section { @apply py-20; }
  .h1 { @apply text-5xl font-semibold leading-tight tracking-tight text-gray-900; }
  .h2 { @apply text-4xl font-medium tracking-tight text-gray-900; }
  .h3 { @apply text-2xl font-medium text-gray-900; }
  .lead { @apply text-base leading-relaxed text-gray-600; }
  .btn { @apply inline-flex min-h-11 items-center justify-center gap-2 whitespace-nowrap rounded-full px-5 text-sm font-medium transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-900 focus-visible:ring-offset-2; }
  .btn-primary { @apply bg-gray-500 text-white hover:bg-gray-600; }
  .btn-secondary { @apply border border-gray-400 bg-white text-gray-900 hover:border-gray-900; }
  .btn-brand { @apply bg-fuchsia-700 text-white hover:bg-fuchsia-800; }
  .btn-brand-outline { @apply border border-fuchsia-700 bg-white text-fuchsia-700 hover:bg-fuchsia-50; }
  .btn-on-dark { @apply border border-white bg-white text-gray-900 hover:bg-gray-100; }
  .badge { @apply inline-flex items-center rounded-full bg-gray-200 px-2.5 py-0.5 text-xs font-medium text-gray-700; }
  .badge-dark { @apply bg-gray-500 text-white; }
  .badge-accent { @apply bg-teal-50 text-teal-700; }
  .card { @apply rounded-card border border-gray-400 bg-gray-50 p-6; }
  .chip { @apply inline-flex min-h-11 items-center gap-2 rounded-full border border-gray-400 bg-white px-4 text-sm text-gray-900 hover:border-gray-900; }
  .chip-active { @apply border-gray-500 bg-gray-500 text-white hover:border-gray-600; }
  .link-arrow { @apply inline-flex min-h-11 items-center gap-2 text-sm font-medium text-gray-900 hover:underline; }
  .ph { background: repeating-linear-gradient(45deg, theme('colors.gray.200') 0 10px, theme('colors.gray.100') 10px 20px); }
  .spy-active { @apply border-gray-900 text-gray-900; }
}
"""

# ---------------------------------------------------------------- ikony
def svg(path, cls='h-5 w-5', stroke=True):
    if stroke:
        return ('<svg class="%s" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">'
                '<path stroke-linecap="round" stroke-linejoin="round" d="%s"/></svg>' % (cls, path))
    return '<svg class="%s" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="%s"/></svg>' % (cls, path)

CHEVRON_DOWN = 'm6 9 6 6 6-6'
CHEVRON_RIGHT = 'm9 6 6 6-6 6'
CHEVRON_LEFT = 'm15 6-6 6 6 6'
ARROW_RIGHT = 'M5 12h14m-6-6 6 6-6 6'
STAR = 'M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8L12 2.5z'
X = 'M6 6l12 12M18 6 6 18'


def icon_placeholder(size='h-10 w-10'):
    """Zaślepka ikony z makiety: szary kwadrat z X."""
    return ('<span class="flex %s shrink-0 items-center justify-center rounded-md bg-gray-500 text-white" aria-hidden="true">%s</span>'
            % (size, svg(X, 'h-3/5 w-3/5')))


def star_item(text):
    return '<li class="flex items-start gap-3">%s<span>%s</span></li>' % (svg(STAR, 'mt-0.5 h-4 w-4 shrink-0 text-gray-900', stroke=False), text)


# ---------------------------------------------------------------- podstawowe
def btn(label, href='#', variant='primary', extra='', arrow=False, attrs=''):
    icon = svg(CHEVRON_RIGHT, 'h-4 w-4') if arrow else ''
    return '<a href="%s" class="btn btn-%s %s" %s>%s%s</a>' % (href, variant, extra, attrs, label, icon)


def badge(label, variant=''):
    return '<span class="badge %s">%s</span>' % (('badge-' + variant) if variant else '', label)


def logo(light=False):
    text = 'text-white' if light else 'text-gray-900'
    return ('<span class="flex items-center gap-1.5" aria-hidden="true">'
            '<svg class="h-9 w-10" viewBox="0 0 40 36"><circle cx="11" cy="11" r="10" fill="#a21caf"/>'
            '<circle cx="27" cy="19" r="7" fill="#a3e635"/><circle cx="13" cy="27" r="6" fill="#22d3ee"/></svg>'
            '<span class="text-lg font-bold leading-[0.95] %s">publishing<br>school</span></span>' % text)


def breadcrumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<li aria-hidden="true">%s</li>' % svg(CHEVRON_RIGHT, 'h-4 w-4 text-gray-500'))
        if i == len(items) - 1:
            parts.append('<li aria-current="page" class="text-gray-900">%s</li>' % label)
        elif href:
            parts.append('<li><a href="%s" class="inline-flex min-h-11 items-center hover:underline">%s</a></li>' % (href, label))
        else:
            parts.append('<li>%s</li>' % label)
    return ('<nav aria-label="Okruszki" class="container-page"><ol class="flex items-center gap-2 text-sm text-gray-600">%s</ol></nav>'
            % ''.join(parts))


# ---------------------------------------------------------------- nagłówek i stopka
NAV = [
    ('Kurs', [('Kursy roczne', [('Grafika 3D', 'kurs-roczny.html'), ('Web Designer UI/UX', 'kurs-roczny.html'),
                                ('Grafika DTP', 'kurs-roczny.html'), ('Graphic Designer', 'kurs-roczny.html')]),
              ('Kursy krótkie', [('Katalog kursów', 'kursy-krotkie.html'), ('Blender 3D od podstaw', 'kurs-krotki.html')])]),
    ('Zapisy', [('Rekrutacja', [('Jak się zapisać', 'jak-sie-zapisac.html'), ('Dofinansowanie', 'dofinansowanie.html')])]),
    ('Dla firm', 'dla-firm.html'),
    ('O nas', [('Szkoła', [('O szkole', 'o-szkole.html'), ('Kadra', 'kadra.html'), ('Prace absolwentów', 'prace-absolwentow.html')])]),
    ('Blog', 'blog.html'),
    ('Kontakt', 'kontakt.html'),
]


def header():
    items = []
    for label, target in NAV:
        if isinstance(target, str):
            items.append('<li><a href="%s" class="inline-flex min-h-11 items-center hover:text-gray-600">%s</a></li>' % (target, label))
            continue
        groups = ''.join(
            '<div><p class="text-xs font-medium uppercase tracking-wide text-gray-500">%s</p><ul class="mt-2 space-y-1">%s</ul></div>'
            % (g, ''.join('<li><a href="%s" class="block rounded-lg px-2 py-2 hover:bg-gray-100">%s</a></li>' % (h, l) for l, h in links))
            for g, links in target)
        items.append(
            '<li class="relative" data-dropdown>'
            '<button type="button" aria-expanded="false" class="inline-flex min-h-11 items-center gap-1 hover:text-gray-600">%s%s</button>'
            '<div data-dropdown-panel hidden class="absolute left-1/2 top-full z-50 flex w-max -translate-x-1/2 gap-8 rounded-card border border-gray-200 bg-white p-5 shadow-lg">%s</div>'
            '</li>' % (label, svg(CHEVRON_DOWN, 'h-4 w-4'), groups))
    return ('<header class="sticky top-0 z-40 border-b border-gray-200 bg-white">'
            '<div class="container-page flex h-20 items-center justify-between">'
            '<a href="index.html" aria-label="Publishing School, strona główna">%s</a>'
            '<nav aria-label="Główna"><ul class="flex items-center gap-7 text-sm text-gray-900">%s</ul></nav>'
            '%s</div></header>' % (logo(), ''.join(items), btn('Zapisz się', 'jak-sie-zapisac.html', 'brand-outline')))


def footer():
    def col(title, links):
        return ('<nav aria-label="%s"><p class="font-medium text-white">%s</p><ul class="mt-3 space-y-2">%s</ul></nav>'
                % (title, title + ':', ''.join('<li><a href="%s" class="hover:text-white hover:underline">%s</a></li>' % (h, l) for l, h in links)))
    fb = svg('M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21a9 9 0 1 1 2.9 0z', 'h-6 w-6', stroke=False)
    return f'''<footer class="bg-gray-500 text-gray-100">
  <div class="container-page py-14">
    <div class="flex items-start justify-between">
      <div><a href="index.html" aria-label="Publishing School, strona główna">{logo(light=True)}</a><p class="mt-2 text-sm">Szkoła grafiki komputerowej</p></div>
      <a href="https://www.facebook.com/" class="flex h-11 w-11 items-center justify-center text-white" aria-label="Facebook">{fb}</a>
    </div>
    <div class="mt-8 flex items-center justify-between border-y border-gray-400 py-5">
      <p class="text-xl text-white">Prowadzisz firmę? Zobacz ofertę szkoleń dla zespołów</p>
      {btn('Dla firm (B2B)', 'dla-firm.html', 'on-dark')}
    </div>
    <div class="mt-8 grid grid-cols-12 gap-8 text-sm">
      <address class="col-span-6 space-y-4 not-italic leading-relaxed">
        <p>„Publishing School” Placówka Kształcenia Ustawicznego<br>31-572 Kraków<br>ul. Kosynierów 15B, II piętro</p>
        <p>Sekretariat czynny:<br>pon–pt, 12:30–18:30</p>
        <p><a href="mailto:sekretariat@publishingschool.pl" class="hover:text-white hover:underline">sekretariat@publishingschool.pl</a></p>
      </address>
      <div class="col-span-2">{col('Kursy', [('Grafika 3D', 'kurs-roczny.html'), ('Web designer UI/UX', 'kurs-roczny.html'), ('Grafika DTP', 'kurs-roczny.html'), ('Grafik reklamy', 'kurs-roczny.html'), ('Kursy krótkie', 'kursy-krotkie.html')])}</div>
      <div class="col-span-2">{col('Rekrutacja', [('Jak się zapisać', 'jak-sie-zapisac.html'), ('Formularz zapisu', 'jak-sie-zapisac.html'), ('Dofinansowanie kursów', 'dofinansowanie.html')])}</div>
      <div class="col-span-2">{col('O nas', [('O szkole', 'o-szkole.html'), ('Kadra', 'kadra.html'), ('Prace absolwentów', 'prace-absolwentow.html'), ('Blog', 'blog.html'), ('Kontakt', 'kontakt.html')])}</div>
    </div>
    <div class="mt-10 flex items-center justify-between border-t border-gray-400 pt-5 text-xs">
      <p>© 2026 Publishing School — Wszystkie prawa zastrzeżone</p>
      <ul class="flex gap-6"><li><a href="#" class="hover:text-white hover:underline">Polityka prywatności</a></li><li><a href="#" class="hover:text-white hover:underline">RODO</a></li><li><a href="#" class="hover:text-white hover:underline">Procedura reklamacyjna</a></li></ul>
    </div>
  </div>
</footer>'''


# ---------------------------------------------------------------- sekcje
def hero_split(title, lead, actions='', badges='', badges_after='', note='', image='Zdjęcie 4:3', top='pt-6'):
    return f'''<section class="container-page grid grid-cols-2 items-center gap-12 pb-16 {top}">
  <div>
    {'<div class="flex gap-2">' + badges + '</div>' if badges else ''}
    <h1 class="h1 mt-4">{title}</h1>
    <p class="lead mt-4 max-w-xl">{lead}</p>
    {'<div class="mt-4 flex flex-wrap gap-2">' + badges_after + '</div>' if badges_after else ''}
    {'<div class="mt-6 flex flex-wrap items-center gap-3">' + actions + '</div>' if actions else ''}
    {'<p class="mt-3 text-xs text-gray-600">' + note + '</p>' if note else ''}
  </div>
  {media(image)}
</section>'''


def hero_center(title, lead):
    return f'''<section class="container-page py-20 text-center">
  <h1 class="h1 mx-auto max-w-3xl">{title}</h1>
  <p class="lead mx-auto mt-4 max-w-2xl">{lead}</p>
</section>'''


def media(label='Zdjęcie 4:3', ratio='aspect-[4/3]', extra=''):
    return ('<div class="ph flex %s items-center justify-center rounded-card border border-gray-200 %s" role="img" aria-label="%s">'
            '<span class="font-mono text-xs uppercase tracking-widest text-gray-500">%s</span></div>' % (ratio, extra, label, label))


def proof_bar(items):
    cells = ''.join('<div class="rounded-xl bg-white px-4 py-5 text-center shadow-proof"><dt class="sr-only">%s</dt>'
                    '<dd class="break-words text-lg font-semibold text-gray-900">%s</dd><dd class="mt-1 text-sm text-gray-600">%s</dd></div>' % (b, a, b)
                    for a, b in items)
    return ('<section aria-label="Najważniejsze informacje" class="container-page pb-6">'
            '<dl class="grid gap-4" style="grid-template-columns:repeat(%d,minmax(0,1fr))">%s</dl></section>' % (len(items), cells))


def anchor_nav(items):
    links = ''.join('<li><a href="#%s" class="inline-flex min-h-11 items-center border-b-2 border-transparent text-gray-600 hover:text-gray-900">%s</a></li>' % (i, l) for l, i in items)
    return ('<nav aria-label="Na tej stronie" data-spy class="sticky top-20 z-30 border-b border-gray-200 bg-white/95 backdrop-blur">'
            '<ul class="container-page flex gap-6 text-sm">%s</ul></nav>' % links)


def section_head(title, lead='', badge_label='', center=False, badge_variant=''):
    align = 'text-center' if center else ''
    return ('<div class="%s">%s<h2 class="h2 %s">%s</h2>%s</div>'
            % (align, (badge(badge_label, badge_variant) + ' ') if badge_label else '', 'mt-3' if badge_label else '', title,
               ('<p class="lead mt-3 %s">%s</p>' % ('mx-auto max-w-2xl' if center else 'max-w-3xl', lead)) if lead else ''))


def course_card(title, text, meta='', link_label='Zobacz program', href='kurs-roczny.html', center_link=False, cat='', extra=''):
    return f'''<article class="card flex flex-col {extra}"{(' data-cat="' + cat + '"') if cat else ''}>
  {icon_placeholder()}
  <h3 class="mt-4 text-xl text-gray-900">{title}</h3>
  <p class="mt-2 text-sm text-gray-600">{text}</p>
  {'<p class="mt-3 text-xs text-gray-600">' + meta + '</p>' if meta else ''}
  <div class="mt-auto pt-6 {'text-center' if center_link else ''}"><a href="{href}" class="link-arrow">{link_label}{svg(CHEVRON_RIGHT, 'h-4 w-4')}</a></div>
</article>'''


def info_card(title, text):
    return ('<article class="card">%s<h3 class="mt-4 font-medium text-gray-900">%s</h3><p class="mt-2 text-sm text-gray-600">%s</p></article>'
            % (icon_placeholder('h-8 w-8'), title, text))


def accordion(items, open_first=False, boxed=False):
    rows = []
    for i, (q, a) in enumerate(items):
        rows.append(
            '<details class="group border-b border-gray-300"%s>'
            '<summary class="flex min-h-14 cursor-pointer list-none items-center justify-between gap-4 px-3 text-sm text-gray-900 [&::-webkit-details-marker]:hidden">'
            '%s%s</summary><div class="px-3 pb-5 text-sm leading-relaxed text-gray-700">%s</div></details>'
            % (' open' if (open_first and i == 0) else '', q, svg(CHEVRON_DOWN, 'h-4 w-4 shrink-0 transition group-open:rotate-180'), a))
    return '<div class="%s">%s</div>' % ('border-t border-gray-300' if boxed else '', ''.join(rows))


def stats(items):
    return ('<dl class="mt-6 grid grid-cols-3 gap-6">%s</dl>'
            % ''.join('<div><dt class="text-xs text-gray-600">%s</dt><dd class="mt-1 text-lg font-semibold text-gray-900">%s</dd></div>' % (a, b) for a, b in items))


def split(content, image_label='Zdjęcie 4:3', image_left=False):
    img = media(image_label)
    left, right = (img, content) if image_left else (content, img)
    return '<div class="grid grid-cols-2 items-center gap-12"><div>%s</div><div>%s</div></div>' % (left, right)


def faq_section(items, lead='', full_link=False, open_first=True):
    link = '<p class="mt-3"><a href="#" class="text-sm text-gray-900 hover:underline">Zobacz pełne FAQ</a></p>' if full_link else ''
    return f'''<section class="container-page section">
  <div class="grid grid-cols-2 gap-12">
    <div>
      <h2 class="h2">Najczęściej zadawane pytania</h2>
      {'<p class="lead mt-3">' + lead + '</p>' if lead else ''}{link}
      <div class="mt-5">{btn('Zadaj pytanie', 'kontakt.html', 'secondary')}</div>
    </div>
    {accordion(items, open_first=open_first, boxed=False)}
  </div>
</section>'''


def cta_card(title, text, actions, phone_line=False):
    phone = ('<p class="mt-3 text-sm text-gray-900">Masz pytania? Zadzwoń: <a href="%s" class="font-semibold hover:underline">%s</a></p>' % (PHONE_HREF, PHONE)) if phone_line else ''
    return f'''<section class="container-page pb-20">
  <div class="rounded-card bg-gray-100 px-10 py-10 text-center">
    <h2 class="text-3xl font-medium text-gray-900">{title}</h2>
    <p class="mt-3 text-sm font-medium text-gray-900">{text}</p>
    {phone}
    <div class="mt-5 flex justify-center gap-3">{actions}</div>
  </div>
</section>'''


def funding_band(title, text, items=None, disclaimer=True, badge_label='Finansowanie nauki'):
    lst = ('<ul class="mt-4 flex flex-wrap gap-x-6 gap-y-2 text-xs text-gray-900">%s</ul>' % ''.join(star_item(i) for i in items)) if items else ''
    note = '<p class="mt-3 text-xs text-gray-600">Informacje ogólne, nie stanowią porady prawnej ani finansowej.</p>' if disclaimer else ''
    return f'''<section class="container-page section" id="dofinansowanie">
  <div class="flex items-center justify-between gap-10 rounded-card bg-gray-100 px-10 py-8">
    <div class="max-w-2xl">
      {badge(badge_label, 'accent')}
      <h2 class="mt-3 text-3xl font-medium text-gray-900">{title}</h2>
      <p class="mt-2 text-sm font-medium text-gray-900">{text}</p>
      {lst}
    </div>
    <div class="flex shrink-0 flex-col items-center gap-2">
      {btn('Sprawdź możliwe dofinansowania', 'dofinansowanie.html', 'primary')}
      <a href="{PHONE_HREF}" class="inline-flex min-h-11 items-center text-xs text-gray-900 hover:underline">lub zadzwoń {PHONE}</a>
    </div>
  </div>
  {note}
</section>'''


def gallery(panels, all_href='prace-absolwentow.html'):
    """panels: (etykieta, podpis) — pierwszy panel jest rozwinięty."""
    items = []
    for i, (label, caption) in enumerate(panels):
        on = i == 0
        items.append(f'''<button type="button" data-gallery-item aria-expanded="{'true' if on else 'false'}" style="flex-grow:{'3' if on else '1'}" class="relative flex min-w-0 basis-0 flex-col justify-between border-r border-gray-400 bg-gray-100 p-6 text-left transition-[flex-grow] duration-300 last:border-r-0">
  <span class="text-lg text-gray-900">{label}</span>
  <span data-gallery-detail {'' if on else 'hidden'} class="flex items-end justify-between gap-4">
    <span class="text-xs text-gray-600">{caption}</span>
    <span class="flex h-9 w-9 items-center justify-center rounded-full bg-fuchsia-700 text-white">{svg(ARROW_RIGHT, 'h-4 w-4')}</span>
  </span>
</button>''')
    return f'''<div data-gallery class="mt-10 flex h-96 overflow-hidden rounded-card border border-gray-400">{''.join(items)}</div>
<div class="mt-6 text-center">{btn('Zobacz wszystkie prace', all_href, 'secondary')}</div>'''


def works_section(panels, side=''):
    head = section_head('Prace naszych słuchaczy', 'Każdy projekt w portfolio powstał na zajęciach — zobacz, co tworzą osoby kończące Publishing School.', center=True)
    if not side:
        return '<section class="container-page section">%s%s</section>' % (head, gallery(panels))
    return ('<section class="container-page section">%s<div class="mt-10 grid grid-cols-12 items-start gap-10">'
            '<div class="col-span-4">%s</div><div class="col-span-8 -mt-10">%s</div></div></section>' % (head, side, gallery(panels)))


def reviews(cards):
    items = ''.join(f'''<article class="card w-[calc((100%-4.5rem)/4)] shrink-0 snap-start">
  <p class="flex gap-1 text-gray-900" aria-label="Ocena 5 na 5">{''.join(svg(STAR, 'h-4 w-4', stroke=False) for _ in range(5))}</p>
  <p class="mt-3 text-sm text-gray-700">{text}</p>
  <p class="mt-3 text-sm font-medium text-gray-900">{name}</p>
  <a href="{href}" class="link-arrow">{course}{svg(CHEVRON_RIGHT, 'h-4 w-4')}</a>
</article>''' for text, name, course, href in cards)
    return f'''<section class="container-page section" data-carousel>
  {section_head('Opinie absolwentów i słuchaczy z Google', badge_label='Opinie')}
  <div data-carousel-track class="mt-8 flex snap-x gap-6 overflow-x-hidden scroll-smooth">{items}</div>
  <div class="mt-6 flex justify-center gap-3">
    <button type="button" data-carousel-step="-1" class="flex h-11 w-11 items-center justify-center rounded-full bg-gray-200 text-gray-900 hover:bg-gray-300" aria-label="Poprzednie opinie">{svg(CHEVRON_LEFT, 'h-4 w-4')}</button>
    <button type="button" data-carousel-step="1" class="flex h-11 w-11 items-center justify-center rounded-full bg-gray-500 text-white hover:bg-gray-600" aria-label="Następne opinie">{svg(CHEVRON_RIGHT, 'h-4 w-4')}</button>
  </div>
</section>'''


def pricing(pay_items, org, included, lead):
    org_dl = ''.join('<div><dt class="text-xs text-gray-600">%s</dt><dd class="mt-0.5 text-sm font-medium text-gray-900">%s</dd></div>' % (a, b) for a, b in org)
    return f'''<section class="container-page section" id="cena" data-price>
  {badge('Cennik')}
  <h2 class="h2 mt-3">Prosta cena</h2>
  <p class="lead mt-3 max-w-2xl">{lead}</p>
  <div class="mt-4 flex items-center gap-3 text-sm">
    <span data-price-label="raty">Raty 0%</span>
    <button type="button" role="switch" aria-checked="false" aria-label="Płatność jednorazowa" class="group relative inline-flex h-6 w-11 items-center rounded-full bg-gray-300 transition-colors after:absolute after:-inset-2.5 aria-checked:bg-gray-500">
      <span class="ml-0.5 h-5 w-5 rounded-full bg-white shadow transition-transform group-aria-checked:translate-x-5"></span>
    </button>
    <span data-price-label="raz">Jednorazowo</span>
    <span data-price-view="raz" class="badge badge-accent">Oszczędzasz [X]%</span>
  </div>
  <div class="mt-6 grid grid-cols-2 gap-6">
    <div class="flex flex-col rounded-card bg-gray-100 p-8">
      <p data-price-view="raty" class="text-sm text-gray-600">Płatność w ratach</p>
      <p data-price-view="raz" class="text-sm text-gray-600">Płatność jednorazowa</p>
      <p data-price-view="raty" class="mt-2"><span class="text-5xl font-medium text-gray-900">[kwota]</span> <span class="text-sm text-gray-600">zł / mies. · 11 rat 0%</span></p>
      <p data-price-view="raz" class="mt-2"><span class="text-5xl font-medium text-gray-900">[kwota]</span> <span class="text-sm text-gray-600">zł za cały kurs</span></p>
      <ul class="mt-6 space-y-3 text-sm text-gray-900">{''.join(star_item(i) for i in pay_items)}</ul>
      <div class="mt-auto pt-8">{btn('Zarezerwuj miejsce', 'jak-sie-zapisac.html', 'primary', 'w-full')}</div>
    </div>
    <div class="rounded-card bg-gray-100 p-8">
      <p class="text-sm font-medium text-gray-900">Organizacja zajęć</p>
      <dl class="mt-4 grid grid-cols-2 gap-x-8 gap-y-4 border-b border-gray-300 pb-6">{org_dl}</dl>
      <p class="mt-6 text-sm font-medium text-gray-900">W cenie kursu</p>
      <ul class="mt-4 grid grid-cols-2 gap-x-8 gap-y-3 text-sm text-gray-900">{''.join(star_item(i) for i in included)}</ul>
    </div>
  </div>
</section>'''


def steps_section(steps):
    cards = ''.join('<li class="rounded-card border border-gray-400 bg-gray-50 p-5">%s<p class="mt-4 text-sm font-medium text-gray-900">%s</p><p class="mt-1 text-sm text-gray-600">%s</p></li>'
                    % (icon_placeholder('h-8 w-8'), a, b) for a, b in steps)
    return ('<section class="container-page section" id="zapisy">%s<ol class="mt-8 grid grid-cols-4 gap-5">%s</ol></section>'
            % (section_head('Jak się zapisać', badge_label='Zapisy'), cards))


def page(filename, title, body, description=''):
    html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Publishing School</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=typography"></script>
<script src="assets/tailwind.config.js"></script>
<style type="text/tailwindcss">{COMPONENT_CSS}</style>
<style>[hidden]{{display:none!important}}</style>
</head>
<body class="min-w-[1280px] bg-white font-sans text-gray-900 antialiased">
{header()}
<main>
{body}
</main>
{footer()}
<script src="assets/app.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, filename), 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('zapisano', filename)


# ================================================================ TREŚCI WSPÓLNE
PROOF_5 = [('28 lat', 'Doświadczenia'), ('Orły Edukacji', '2019–2025'), ('Status słuchacza', 'Honorowany urzędy pracy'),
           ('nr 277460', 'Rejestr MEN'), ('Dyplom PL/EN', 'Legitymacja i zaświadczenia')]
PROOF_4 = PROOF_5[:4]
FAQ_ROCZNY = [
    ('Czy muszę mieć doświadczenie w projektowaniu?', 'Nie. Kurs zaczyna się od podstaw, a prowadzący pokazują każde narzędzie krok po kroku.'),
    ('Jak działają raty 0%?', 'Cenę kursu rozkładasz na 11 miesięcznych rat bez odsetek.'),
    ('Jak działa dofinansowanie z KFS?', 'Krajowy Fundusz Szkoleniowy dla osób zatrudnionych — wniosek składa pracodawca w urzędzie pracy właściwym dla siedziby firmy. <a href="dofinansowanie.html" class="text-fuchsia-700 hover:underline">Zobacz dofinansowanie ›</a>'),
    ('Co jeśli opuszczę zjazd?', 'Każdy zjazd jest nagrywany, a materiały zostają dostępne. Nadrobisz zajęcia w dogodnym terminie.'),
    ('Na jakim komputerze będę pracować?', 'Stacjonarnie na komputerach Mac w pracowni. Online na własnym PC lub Macu z dostępem do internetu.'),
    ('Czy dyplom jest honorowany przez pracodawców?', 'Dostajesz hologramowany dyplom polsko-angielski i zaświadczenie zgodne z MEN.'),
    ('Czy mogę zmienić formę z online na stacjonarną?', 'Tak, jeśli w grupie są wolne miejsca. Napisz do sekretariatu przed kolejnym zjazdem.'),
]
PAY_ITEMS = ['Start: koniec września 2026', 'Zapisy do [data]', 'Zostało [X] miejsc w grupie', 'Ta sama cena online i stacjonarnie',
             'Faktura VAT na firmę', 'Dokumenty do dofinansowania w 24 h']
ORG = [('Forma', 'Online lub Kraków'), ('Czas trwania', 'Wrzesień – czerwiec'), ('Zjazdy', 'Co 2 weekendy'), ('Grupa', '10–12 osób')]
INCLUDED = ['Materiały do zajęć', 'Nagrania zjazdów', 'Dyplom PL/EN', 'Zaświadczenie MEN', 'Status słuchacza', 'Pracownia Mac', 'Konsultacje z prowadzącymi', 'Projekt do portfolio']
FUNDING_ITEMS = ['Urząd pracy (bon szkoleniowy)', 'KFS dla pracowników', 'Nieoprocentowana pożyczka']
CTA_ACTIONS = btn('Zapisz się', 'jak-sie-zapisac.html', 'primary') + btn('Zadaj pytanie', 'kontakt.html', 'secondary')
CTA_2627 = cta_card('Zarezerwuj miejsce w grupie 2026/27', 'Nabór 2026/27: liczba miejsc w grupach jest ograniczona.', CTA_ACTIONS)
WORKS = [('Grafika 3D', 'Sylwia K. · rocznik 2025/26'), ('UX/UI', 'Michał P. · rocznik 2025/26'), ('UX/UI', 'Anna W. · rocznik 2024/25'), ('Grafik DTP', 'Tomasz L. · rocznik 2024/25')]

# ================================================================ STRONY
def home():
    body = hero_split(
        'Zostań grafikiem. Od podstaw do portfolio',
        'Kursy roczne przygotowują do pracy w grafice 3D, DTP, web designie i reklamie. Uczysz się w weekendy, online albo w Krakowie, u praktyków, którzy pracują w zawodzie.',
        badges=badge('Nabór 2026/27', 'dark') + badge('Online / Kraków', 'dark'),
        badges_after=badge('Wrzesień – czerwiec') + badge('Co 2 weekend'),
        actions=btn('Zobacz kierunki roczne', '#kursy-roczne') + btn('Przeglądaj kursy krótkie', 'kursy-krotkie.html', 'secondary'),
        note='Nie wiesz, który kurs wybrać? <a href="kontakt.html" class="underline">Zadzwoń do sekretariatu</a>', top='pt-12')
    body += proof_bar(PROOF_5)

    roczne = [('Grafika 3D', 'Modelowanie, animacja i wizualizacje w Blenderze, Mayi i 3ds Max — kończysz z portfolio realnych projektów.'),
              ('Web Designer UI/UX', 'Badania z użytkownikami, projekt interfejsu w Figmie i strony www — kończysz z case study.'),
              ('Grafika DTP', 'Skład, typografia i przygotowanie plików do druku — kończysz z portfolio realnych materiałów.'),
              ('Graphic Designer', 'Identyfikacja wizualna i reklama do internetu i druku — kończysz z portfolio projektów.')]
    body += f'''<section class="container-page section" id="kursy-roczne">
  {section_head('Zmień zawód, pogłęb konkretną umiejętność', 'Kurs roczny to pełne przygotowanie do pracy jako <strong class="text-gray-900">Grafik 3D, Graphic Designer, Web Designer UI/UX albo Junior UI Designer</strong>. Program prowadzi od podstaw do gotowego portfolio.', 'Kursy roczne')}
  <div class="mt-8 grid grid-cols-2 gap-5">{''.join(course_card(t, d, 'Wrzesień – czerwiec · online / stacjonarnie') for t, d in roczne)}</div>
</section>'''

    body += f'''<section class="container-page section">
  {section_head('Krótkie kursy — pogłęb konkretną umiejętność', 'Nie musisz zapisywać się na cały rok. Wybierz jeden temat lub narzędzie — bez oczekiwania na start roku szkolnego.', 'Kursy krótkie')}
  <div class="mt-8 grid grid-cols-12 gap-5">
    {course_card('Blender 3D od podstaw', 'Modelowanie, teksturowanie i render — kończysz z gotową sceną do portfolio.', '17–24.10.2026 · online · 870 zł', 'Zobacz program', 'kurs-krotki.html', extra='col-span-6')}
    {course_card('Kurs w Twoim terminie', 'Ustal harmonogram dla siebie lub zespołu, bez czekania na start grupy.', '', 'Ustal termin', 'dla-firm.html', True, extra='col-span-3')}
    {course_card('Katalog kursów', 'Ponad 30 tematów, od Canvy po Unreal Engine 5. Wybierz to, czego potrzebujesz w pracy.', '', 'Sprawdź ofertę', 'kursy-krotkie.html', True, extra='col-span-3')}
  </div>
</section>'''

    body += f'''<section class="container-page section">
  <div class="grid grid-cols-2 gap-12">
    <div>
      {section_head('Nie musisz płacić z własnej kieszeni', 'Sprawdź, z jakiego źródła możesz pokryć koszt kursu.', 'Dofinansowanie')}
      <div class="mt-5">{btn('Sprawdź możliwe dofinansowania', 'dofinansowanie.html', 'secondary', arrow=True)}</div>
      <p class="mt-3 text-xs text-gray-600">Informacje ogólne, nie stanowią porady prawnej ani finansowej.</p>
    </div>
    {accordion([('Dofinansowanie przez urząd pracy', 'Bon szkoleniowy albo dofinansowanie dla osób bezrobotnych i szukających pracy. O skierowanie zapytaj w swoim urzędzie pracy.'),
                ('Krajowy Fundusz Szkoleniowy (KFS)', 'Krajowy Fundusz Szkoleniowy dla osób zatrudnionych — wniosek składa pracodawca w urzędzie pracy właściwym dla regionu zarejestrowania siedziby firmy.'),
                ('Nieoprocentowana pożyczka na kształcenie', 'Pożyczka bez odsetek z możliwością częściowego umorzenia, dla każdego, kto podnosi kwalifikacje.')], open_first=True, boxed=True)}
  </div>
</section>'''

    body += f'''<section class="container-page section">
  {split(section_head('Uczymy praktycznie, od pierwszych zajęć', 'Uczą graficy, projektanci, programiści i poligrafowie, którzy na co dzień robią to, czego uczą. Dlatego kończysz kurs z pracami, które możesz pokazać pracodawcy.', 'O szkole')
         + '<div class="mt-6 grid grid-cols-2 gap-4">' + ''.join('<div class="flex items-center gap-3 rounded-card bg-gray-100 p-4"><span class="text-lg font-semibold leading-tight text-gray-900">%s</span><span class="text-xs text-gray-600">%s</span></div>' % (a, b) for a, b in [('Orły Edukacji', 'Wyróżnienie 2019–2025'), ('28 lat', 'Uczymy od 1998 roku')]) + '</div>'
         + '<div class="mt-6">' + btn('Poznaj szkołę', 'o-szkole.html', 'secondary', arrow=True) + '</div>', image_left=True)}
</section>'''

    body += reviews([
        ('Konkretnie i bez lania wody. Po dwóch weekendach sama przygotowuję grafiki do sklepu.', 'Kursantka, Photoshop', 'Zobacz kurs', 'kursy-krotkie.html'),
        ('Najbardziej przydało mi się przygotowanie plików do druku. Drukarnia nie odsyła już poprawek.', 'Absolwent, Grafika DTP', 'Zobacz program', 'kurs-roczny.html'),
        ('Zaczynałam od zera, a na koniec miałam gotowy render do portfolio. Zajęcia online bez problemów.', 'Kursantka, Blender 3D', 'Zobacz kurs', 'kurs-krotki.html'),
        ('Po roku miałam portfolio, z którym dostałam pierwszą pracę jako projektantka UI.', 'Absolwentka, Web Designer UI/UX', 'Zobacz program', 'kurs-roczny.html'),
        ('Małe grupy robią różnicę — prowadzący znał mój projekt i pomagał go dopracować.', 'Absolwent, Graphic Designer', 'Zobacz program', 'kurs-roczny.html'),
    ])
    body += works_section(WORKS)
    body += cta_card('Twój następny zawód zaczyna się tutaj', 'Sprawdź dostępne kierunki lub porozmawiaj z sekretariatem, jeśli potrzebujesz pomocy w wyborze programu.', CTA_ACTIONS, phone_line=True)
    page('index.html', 'Strona główna', body, 'Szkoła grafiki komputerowej w Krakowie: kursy roczne i krótkie, online i stacjonarnie.')


def kurs_roczny():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kursy roczne', ''), ('Web Designer UI/UX', '')])
    body += hero_split(
        'Web Designer UI/UX, kurs roczny od podstaw do portfolio',
        'Nauczysz się projektować strony i aplikacje, z których wygodnie się korzysta. Uczysz się co drugi weekend, online albo w Krakowie, i kończysz z portfolio oraz dyplomem zgodnym z MEN.',
        badges=badge('Nabór 2026/27', 'dark') + badge('Online / Kraków', 'dark'),
        actions=btn('Zapisz się', 'jak-sie-zapisac.html') + btn('Zobacz program', '#program', 'secondary'),
        note='Start: koniec września 2026 · zapisy do [data] · zostało [X] miejsc')
    body += proof_bar(PROOF_4)
    body += anchor_nav([('Program', 'program'), ('Kadra', 'kadra'), ('Cena', 'cena'), ('Zapisy', 'zapisy')])

    dla = [('Chcesz zmienić zawód', 'Przejdziesz od zera do pierwszych projektów w portfolio i pracy w projektowaniu.'),
           ('Zaczynasz od podstaw', 'Nie potrzebujesz doświadczenia ani znajomości programów graficznych.'),
           ('Pracujesz w marketingu lub IT', 'Poszerzysz kompetencje o UX i lepiej dogadasz się z zespołem produktowym.'),
           ('Robisz już grafikę', 'Uporządkujesz wiedzę i nauczysz się projektować interfejsy, nie tylko wizualne materiały.')]
    body += f'''<section class="container-page section" id="dla-kogo">
  {section_head('Ten kurs jest dla Ciebie, jeśli:', center=True)}
  <div class="mt-8 grid grid-cols-4 gap-5">{''.join(info_card(a, b) for a, b in dla)}</div>
</section>'''

    body += f'''<section class="container-page section">
  {split(section_head('Co potrafisz po kursie', 'Kurs przygotowuje do samodzielnej pracy w projektowaniu interfejsów:', 'Efekty')
         + '<ul class="mt-5 space-y-3 text-sm text-gray-900">' + ''.join(star_item(i) for i in ['Badasz potrzeby użytkowników i wyciągasz z nich wnioski', 'Projektujesz makiety i klikalne prototypy w Figmie', 'Znasz podstawy HTML i CSS, więc rozmawiasz z programistami']) + '</ul>', 'Praca absolwenta', image_left=True)}
</section>'''

    mods = [('Moduł 1 · Podstawy UX i heurystyki', 'Czym jest UX, heurystyki Nielsena, persona i scenariusze użytkownika.'),
            ('Moduł 2 · Badania z użytkownikami', 'Wywiady, ankiety i obserwacje. Uczysz się zbierać i porządkować wnioski.'),
            ('Moduł 3 · Architektura informacji', 'Struktura serwisu, ścieżki użytkownika i makiety lo-fi.'),
            ('Moduł 4 · Projektowanie w Figmie', 'Siatki, typografia, kolor i auto layout.'),
            ('Moduł 5 · Design system', 'Biblioteka komponentów, style i warianty.'),
            ('Moduł 6 · Prototyp i testy', 'Klikalny prototyp, testy użyteczności i podstawy HTML/CSS.'),
            ('Moduł 7 · Portfolio i dyplom', 'Case study, prezentacja procesu i obrona projektu.')]
    body += f'''<section class="container-page section" id="program">
  <div class="grid grid-cols-2 gap-12">
    <div>
      {section_head('Program kursu', '7 modułów od końca września do końca czerwca. Każdy moduł kończy się projektem do portfolio.', 'Program')}
      <div class="mt-5">{btn('Pobierz program (PDF)', '#', 'secondary')}</div>
    </div>
    {accordion(mods)}
  </div>
</section>'''

    kadra_side = (section_head('Kadra kursu', 'Uczą praktycy, którzy pracują w zawodzie: UX designerzy, projektanci aplikacji i programiści.')
                  + '<div class="mt-5">' + btn('Zadaj pytanie', 'kontakt.html', 'secondary') + '</div>')
    body += '<div id="kadra" class="scroll-mt-36">' + works_section(WORKS[1:], kadra_side) + '</div>'
    body += pricing(PAY_ITEMS, ORG, INCLUDED, 'Płacisz tyle samo online i stacjonarnie. Wybierz raty albo jedną płatność, a z dofinansowaniem pomoże sekretariat.')
    body += funding_band('Ten kurs może kosztować Cię mniej', 'Sprawdź, czy przysługuje Ci dofinansowanie. Sekretariat pomoże przygotować dokumenty.', FUNDING_ITEMS)
    body += steps_section([('Formularz', 'Wypełniasz formularz zgłoszeniowy'), ('Dokumenty', 'Formularz i 2 zdjęcia paszportowe'),
                           ('Rozmowa wstępna', 'Online przez Jitsi lub stacjonarnie'), ('Pierwsze zajęcia', 'Kontrakt i opłata startowa')])
    body += faq_section(FAQ_ROCZNY, 'Nie ma tu Twojego pytania? Zadzwoń %s, codziennie 9:00–20:00.' % PHONE, open_first=False)
    body += CTA_2627
    page('kurs-roczny.html', 'Web Designer UI/UX — kurs roczny', body, 'Kurs roczny Web Designer UI/UX: od podstaw do portfolio, online lub w Krakowie.')


SHORT_COURSES = [
    ('Blender 3D od podstaw', 'Modelowanie, teksturowanie i render — kończysz z gotową sceną do portfolio.', '17–24.10.2026 · online · 870 zł', '3d soon', 'kurs-krotki.html'),
    ('InDesign dla początkujących', 'Skład publikacji, style i eksport do PDF — przygotujesz pliki gotowe do druku.', '17–28.10.2026 · online · 760 zł', 'adobe soon', 'kurs-krotki.html'),
    ('Kurs UX — User Experience', 'Heurystyki, badania i wireframing — zaprojektujesz lepszą ścieżkę użytkownika.', 'Zapytaj o termin · 530 zł', 'web', 'kurs-krotki.html'),
    ('Photoshop dla początkujących', 'Retusz, maski i warstwy — przygotujesz grafiki do sklepu i social mediów.', '02–05.10.2026 · online', 'adobe soon', 'kurs-krotki.html'),
    ('Canva: grafiki i rolki', 'Grafiki, rolki i animacje do social mediów — bez znajomości programów Adobe.', '23–29.09.2026 · online', 'social soon', 'kurs-krotki.html'),
    ('Typografia w pracy grafika', 'Dobór krojów, hierarchia i skład — Twoje projekty staną się czytelniejsze.', '24–30.09.2026 · online', 'druk soon', 'kurs-krotki.html'),
]


def kursy_krotkie():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kursy krótkie', '')])
    body += hero_center('Kursy krótkie', 'Jeden temat, kilka dni nauki, certyfikat na koniec. Wybierz kategorię i zacznij w najbliższy weekend.')
    body += proof_bar(PROOF_5)
    body += f'''<section class="container-page section">
  {split(section_head('Kurs może opłacić pracodawca albo urząd pracy', 'Kursy krótkie często finansuje KFS albo bon szkoleniowy z urzędu pracy. Dokumenty do wniosku przygotujemy w ciągu 24 h.', 'Dofinansowanie')
         + '<div class="mt-5">' + btn('Sprawdź dofinansowanie', 'dofinansowanie.html', 'secondary', arrow=True) + '</div>')}
</section>'''

    chips = [('all', 'Wszystkie'), ('soon', 'Najbliższe'), ('3d', 'Grafika 3D'), ('adobe', 'Grafika i Adobe'), ('web', 'Web i UX'), ('social', 'Social media'), ('druk', 'Druk i DTP')]
    chip_html = ''.join('<button type="button" role="tab" data-tab="%s" aria-selected="%s" class="chip">%s</button>' % (k, 'true' if k == 'all' else 'false', l) for k, l in chips)
    cards = ''.join(course_card(t, d, m, 'Zobacz program', h, cat=c) for t, d, m, c, h in SHORT_COURSES)
    body += f'''<section class="container-page section">
  {section_head('Wybierz rodzaj kursu', '6 kategorii, ponad 30 tematów.', center=True)}
  <div role="tablist" aria-label="Kategorie kursów" data-tabs data-tabs-mode="filter" data-tabs-target="#course-grid" class="mt-6 flex flex-wrap justify-center gap-2">{chip_html}</div>
  <div class="mt-6 border-t border-gray-400"></div>
  <div id="course-grid" class="mt-8 grid grid-cols-3 gap-5">{cards}</div>
  <div class="mt-8 text-center">{btn('Pokaż kolejne kursy (8)', '#', 'secondary')}</div>
</section>'''
    body += funding_band('Nie mamy teraz potwierdzonego terminu?', 'Ten kurs realizujemy też na zamówienie — indywidualnie i dla zespołów. Możesz też zostawić kontakt i dostać powiadomienie, gdy ruszy najbliższa grupa.', disclaimer=False)
    body += f'''<section class="container-page section">
  {split(section_head('Uczysz się u praktyków, w małych grupach', 'Od 1998 roku szkolimy grafików w Krakowie. Zajęcia prowadzą projektanci, którzy pracują w zawodzie, a każdy kurs kończy się pracą, którą pokażesz w portfolio albo wykorzystasz w firmie.', 'O szkole')
         + stats([('Zjazdy', 'Co 2 weekend'), ('Wyróżnienie', 'Orły Edukacji'), ('Certyfikat', 'Z hologramem')])
         + '<div class="mt-6">' + btn('Poznaj szkołę', 'o-szkole.html', 'secondary', arrow=True) + '</div>', image_left=True)}
</section>'''
    body += CTA_2627
    page('kursy-krotkie.html', 'Kursy krótkie', body, 'Katalog kursów krótkich Publishing School: grafika, 3D, UX, social media i druk.')


def kurs_krotki():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kursy krótkie', 'kursy-krotkie.html'), ('Blender 3D od podstaw', '')])
    body += hero_split(
        'Blender 3D od podstaw',
        'W trzy dni przejdziesz od pierwszego uruchomienia Blendera do gotowego renderu. Wymodelujesz, oteksturujesz i oświetlisz własną scenę, którą dodasz do portfolio.',
        badges=badge('Grafika 3D i animacja', 'dark'),
        badges_after=badge('17, 18 i 24.10.2026') + badge('Online · Jitsi') + badge('9:00–13:30'),
        actions=btn('Zapisz się na kurs', '#cena'))
    body += proof_bar(PROOF_4)
    body += anchor_nav([('Program', 'program'), ('Kadra', 'kadra'), ('Cena', 'cena'), ('Zapisy', 'faq')])

    odb = [('Zaczynasz od zera', 'Nie potrzebujesz doświadczenia w grafice 3D.'), ('Chcesz pokazać produkt w 3D', 'Wizualizacje do sklepu, social mediów i prezentacji.'), ('Myślisz o pracy grafika 3D', 'Kurs to pierwszy krok i pierwsza praca w portfolio.')]
    kom = [('Modelowanie low poly', 'Budujesz obiekty sceny z prostych brył.'), ('Materiały i światło', 'Teksturujesz modele i oświetlasz scenę.'), ('Kamera i render', 'Ustawiasz kadr i eksportujesz gotową pracę.')]
    body += f'''<section class="container-page section" id="dla-kogo">
  {section_head('Dla kogo jest ten kurs i czego się nauczysz', badge_label='Dla kogo')}
  <p class="mt-6 text-sm text-gray-900">Ten kurs jest dla Ciebie, jeśli:</p>
  <div class="mt-3 grid grid-cols-3 gap-5">{''.join(info_card(a, b) for a, b in odb)}</div>
  <p class="mt-8 text-sm text-gray-900">Po kursie potrafisz:</p>
  <div class="mt-3 grid grid-cols-3 gap-5">{''.join(info_card(a, b) for a, b in kom)}</div>
</section>'''
    body += f'''<section class="container-page section" id="program">
  <div class="grid grid-cols-2 gap-12">
    <div>{section_head('Program kursu', '3 moduły · 16 godzin dydaktycznych (po 45 min) · zajęcia online przez Jitsi.', 'Program')}<div class="mt-5">{btn('Pobierz program (PDF)', '#', 'secondary')}</div></div>
    {accordion([('Moduł 1 · Interfejs i modelowanie', 'Poruszanie się po programie i modelowanie low poly.'), ('Moduł 2 · Materiały i światło', 'Teksturowanie, shadery i oświetlenie sceny.'), ('Moduł 3 · Kamera i render', 'Ustawienie kamery, parametry renderu i finalizacja.'), ('Wymagania techniczne', 'Komputer z zainstalowanym Blenderem (program jest darmowy).')])}
  </div>
</section>'''
    side = (section_head('mgr Anastasiia Dudina', 'Graficzka 3D, specjalistka Blendera. Absolwentka grafiki 3D w Publishing School, pracuje jako freelancerka i tworzy modele oraz wizualizacje.', 'Prowadząca')
            + stats([('Specjalizacja', 'Blender 3D'), ('Wyróżnienie', 'Orły Edukacji'), ('Certyfikat', 'Z hologramem')]))
    body += '<div id="kadra" class="scroll-mt-36">' + works_section([('Grafika 3D', 'Praca z kursu Blender 3D od podstaw')], side) + '</div>'
    body += pricing(['Terminy: 17, 18 i 24.10.2026', 'Zapisy do 11.10.2026', 'Zostało [X] miejsc w grupie', 'Zajęcia online przez Jitsi', 'Faktura VAT na firmę', 'Dokumenty do KFS w 24 h'],
                    [('Forma', 'Online · Jitsi'), ('Czas trwania', '3 dni · 16 h'), ('Godziny', '9:00–13:30'), ('Grupa', '10–12 osób')],
                    ['Materiały do zajęć', 'Nagrania zajęć', 'Certyfikat z hologramem', 'Wysyłka certyfikatu', 'Konsultacje', 'Scena do portfolio', 'Status uczestnika', 'Wsparcie sekretariatu'],
                    'Kurs opłacasz z góry, przed startem. Możesz też rozłożyć płatność albo skorzystać z dofinansowania KFS.')
    body += funding_band('Ten kurs może kosztować Cię mniej', 'Sprawdź, czy przysługuje Ci dofinansowanie. Sekretariat pomoże przygotować dokumenty.', FUNDING_ITEMS)
    body += '<div id="faq" class="scroll-mt-36">' + faq_section([
        ('Jak działa dofinansowanie z KFS?', 'Krajowy Fundusz Szkoleniowy dla osób zatrudnionych — wniosek składa pracodawca w urzędzie pracy właściwym dla regionu zarejestrowania siedziby firmy. <a href="dofinansowanie.html" class="text-fuchsia-700 hover:underline">Zobacz dofinansowanie ›</a>'),
        ('Czy potrzebuję własnego laptopa?', 'Tak, z zainstalowanym Blenderem. Program jest darmowy.'),
        ('Jak wyglądają zajęcia online?', 'Łączysz się przez Jitsi i pracujesz w programie razem z prowadzącą. Nie trzeba zakładać konta.'),
        ('Czy dostanę certyfikat?', 'Tak. Po kursie wysyłamy pocztą hologramowany certyfikat w języku polskim.'),
        ('Co jeśli grupa się nie zbierze?', 'Zaproponujemy najbliższy termin tego samego kursu albo zwrot wpłaty.'),
        ('Czy mogę zrezygnować?', 'Napisz do sekretariatu przed startem kursu. Przeniesiemy Cię na inny termin.'),
        ('Kiedy płacę za kurs?', 'Kurs krótki opłacasz z góry, przed pierwszymi zajęciami.'),
    ], 'Nie ma tu Twojego pytania? Zadzwoń %s.' % PHONE) + '</div>'
    body += CTA_2627
    page('kurs-krotki.html', 'Blender 3D od podstaw', body, 'Kurs Blender 3D od podstaw: 16 h online, certyfikat z hologramem.')


def jak_sie_zapisac():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Zapisy', ''), ('Jak się zapisać', '')])
    body += hero_split(
        'Jak się zapisać',
        'Zapis wygląda inaczej na kurs roczny i na kurs krótki. Wybierz, na co się zapisujesz, i sprawdź kolejne kroki.',
        actions=btn('Kurs roczny — 4 kroki', '#przebieg', attrs='data-open-tab="roczne"') + btn('Kurs krótki — 3 kroki', '#przebieg', 'secondary', attrs='data-open-tab="krotkie"'))
    body += proof_bar(PROOF_5)

    roczne = accordion([('Krok 1 · Formularz zgłoszeniowy', 'Pobierz formularz dla swojego kierunku i wypełnij go w czytniku PDF.'),
                        ('Krok 2 · Dokumenty', 'Wyślij formularz i 2 zdjęcia paszportowe na <a href="mailto:krystyna@publishingschool.pl" class="text-fuchsia-700 hover:underline">krystyna@publishingschool.pl</a>.'),
                        ('Krok 3 · Rozmowa wstępna', 'Umów krótką rozmowę online przez Jitsi, mailowo albo telefonicznie.'),
                        ('Krok 4 · Pierwsze zajęcia', 'Podpisujesz kontrakt edukacyjny i wnosisz opłatę startową.')], open_first=True, boxed=True)
    krotkie = accordion([('Krok 1 · Formularz na stronie kursu', 'Wybierasz termin i wypełniasz formularz, ok. 2 minuty.'),
                         ('Krok 2 · Opłata z góry', 'Opłacasz kurs przed startem. Dopiero wtedy miejsce jest Twoje.'),
                         ('Krok 3 · Potwierdzenie', 'Dostajesz e-mail z potwierdzeniem, harmonogramem i linkiem do zajęć online.')], open_first=True, boxed=True)
    body += f'''<section class="container-page section scroll-mt-24" id="przebieg">
  {section_head('Jak przebiega zapis', 'Na kurs roczny zapisujesz się w 4 krokach, na kurs krótki w 3.', center=True)}
  <div role="tablist" aria-label="Rodzaj kursu" data-tabs data-tabs-target="#przebieg-panele" class="mt-6 flex justify-center gap-2">
    <button type="button" role="tab" data-tab="roczne" aria-selected="true" class="chip">Kursy roczne</button>
    <button type="button" role="tab" data-tab="krotkie" aria-selected="false" class="chip">Kursy krótkie</button>
  </div>
  <div id="przebieg-panele" class="mt-8">
    <div data-panel="roczne" role="tabpanel" class="grid grid-cols-2 gap-10">
      <div><h3 class="h3">Kurs roczny</h3><p class="lead mt-2">Dotyczy kursów rocznych. Pobierz formularz dla swojego kierunku, wypełnij go w czytniku PDF i prześlij e-mailem.</p><div class="mt-6">{roczne}</div></div>
      {media('Grafika / zdjęcie', 'aspect-[6/5]')}
    </div>
    <div data-panel="krotkie" role="tabpanel" hidden class="grid grid-cols-2 gap-10">
      <div><h3 class="h3">Kurs krótki</h3><p class="lead mt-2">Bez zdjęć i rozmowy wstępnej. Miejsce rezerwuje opłata wniesiona z góry.</p><div class="mt-6">{krotkie}</div></div>
      {media('Grafika / zdjęcie', 'aspect-[6/5]')}
    </div>
  </div>
</section>'''
    body += faq_section([
        ('Jakie dokumenty są potrzebne?', 'Na kurs roczny: formularz i 2 zdjęcia paszportowe. Na kurs krótki wystarczy formularz. <a href="#przebieg" class="text-fuchsia-700 hover:underline">Zobacz kroki ›</a>'),
        ('Czy mogę zapisać się bez rozmowy?', 'Na kurs krótki tak. Na kurs roczny przeprowadzamy krótką rozmowę wstępną online.'),
        ('Kiedy płacę za kurs?', 'Za kurs krótki płacisz z góry. Za kurs roczny opłatę startową wnosisz na pierwszych zajęciach, po przyjęciu.'),
        ('Czy jest limit wieku?', 'Nie. Zajęcia są dla dorosłych w każdym wieku.'),
    ], 'Sekretariat odpowiada pon–pt 12:30–18:30, telefon codziennie 9:00–20:00.')
    body += CTA_2627
    page('jak-sie-zapisac.html', 'Jak się zapisać', body, 'Zapis na kurs roczny w 4 krokach i na kurs krótki w 3 krokach.')


def dofinansowanie():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Wsparcie finansowe', '')])
    body += hero_center('Sfinansuj kurs bez płacenia<br>z własnej kieszeni', 'Wybierz swoją sytuację i sprawdź, z jakiego źródła możesz skorzystać.')
    paths = [
        ('up', 'Urząd pracy', 'Dofinansowanie przez urząd pracy', 'Bon szkoleniowy albo dofinansowanie dla osób bezrobotnych i szukających pracy. Zapytaj doradcę w swoim urzędzie pracy o skierowanie na kurs.'),
        ('kfs', 'KFS', 'Krajowy Fundusz Szkoleniowy', 'Pracodawca może pokryć koszt szkolenia pracowników. Wniosek składa firma w urzędzie pracy właściwym dla swojej siedziby.'),
        ('pozyczka', 'Pożyczka', 'Nieoprocentowana pożyczka na kształcenie', 'Pożyczka bez odsetek dla każdego, kto podnosi kwalifikacje. Część kwoty może zostać umorzona.'),
        ('sponsoring', 'Sponsoring', 'Sponsoring kursu', 'Sponsor pokrywa koszt kursu, a Ty wykonujesz dla niego uzgodnione projekty graficzne.'),
        ('pracodawca', 'Pracodawca', 'Kurs opłacony przez pracodawcę', 'Pracodawca finansuje kurs pracownikowi na nowym stanowisku albo w firmie w restrukturyzacji.'),
        ('ulga', 'Ulga podatkowa', 'Ulga dla prowadzących działalność', 'Opłatę za kurs wliczasz w koszty firmy i płacisz niższy podatek. Wystawimy fakturę VAT na firmę.'),
    ]
    tabs = []
    for i, (k, label, _, _) in enumerate(paths):
        on = i == 0
        tabs.append('<button type="button" role="tab" data-tab="%s" aria-selected="%s" class="chip group">'
                    '<span data-tab-step="-1" class="-ml-1 hidden rounded-full p-1 group-aria-selected:inline-flex" aria-label="Poprzednia ścieżka">%s</span>'
                    '%s<span data-tab-step="1" class="-mr-1 hidden rounded-full p-1 group-aria-selected:inline-flex" aria-label="Następna ścieżka">%s</span></button>'
                    % (k, 'true' if on else 'false', svg(CHEVRON_LEFT, 'h-4 w-4'), label, svg(CHEVRON_RIGHT, 'h-4 w-4')))
    docs = [('Program i wymiar godzin kursu', 'Załącznik do wniosku'), ('Oferta i kosztorys', 'Przygotowuje sekretariat w 24 h'),
            ('Zaświadczenie o wpisie do rejestru', 'Rejestr MEN nr 277460 i RIS WUP Kraków'), ('Zaświadczenie o zapisie', 'Wystawiane po przyjęciu zgłoszenia')]
    doc_list = ''.join('<li class="flex gap-3">%s<span><span class="block text-sm font-medium text-gray-900">%s</span><span class="text-xs text-gray-600">%s</span></span></li>'
                       % (svg(X, 'mt-0.5 h-5 w-5 shrink-0 text-gray-900'), a, b) for a, b in docs)
    panels = ''.join(f'''<div data-panel="{k}" role="tabpanel" {'' if i == 0 else 'hidden'}>
  {split(badge('Ścieżka ' + str(i + 1) + ' z 6', 'dark') + ' ' + badge('Dokumenty w 24 h', 'dark') + '<h2 class="h2 mt-3">' + title + '</h2><p class="lead mt-3">' + text + '</p><p class="mt-6 text-sm font-medium text-gray-900">Co przygotujemy do wniosku:</p><ul class="mt-3 space-y-4">' + doc_list + '</ul>', 'Zdjęcie 4:3', image_left=True)}
</div>''' for i, (k, _, title, text) in enumerate(paths))
    body += f'''<section class="container-page pb-20">
  <div role="tablist" aria-label="Źródła finansowania" data-tabs data-tabs-target="#sciezki" class="flex flex-wrap justify-center gap-2">{''.join(tabs)}</div>
  <div id="sciezki" class="mt-16">{panels}</div>
</section>'''
    body += f'''<section class="container-page section">
  {split(section_head('Pomagamy przejść przez wniosek', 'Od 1998 roku szkolimy grafików w Krakowie. Sekretariat przygotuje ofertę, program i zaświadczenia, których wymaga urząd pracy albo pracodawca.', 'O szkole')
         + stats([('Zjazdy', 'Co 2 weekend'), ('Wyróżnienie', 'Orły Edukacji'), ('Certyfikat', 'Z hologramem')]))}
</section>'''
    body += faq_section([
        ('Czy mogę łączyć źródła finansowania?', 'Często tak, np. pracodawca dopłaca część kosztu, a resztę pokrywa KFS. Zasady ustala instytucja przyznająca środki.'),
        ('Ile trwa decyzja?', 'To zależy od instytucji i terminu naboru. Zacznij z wyprzedzeniem — dokumenty ze szkoły przygotujemy w 24 h.'),
        ('Co jeśli dostanę odmowę?', 'Sprawdź inną ścieżkę, np. pożyczkę albo ulgę podatkową. Sekretariat pomoże wybrać kolejną opcję.'),
        ('Czy KFS obejmuje kursy krótkie?', 'Tak, jeśli szkolenie jest związane z pracą.'),
        ('Czy muszę być bezrobotny?', 'Nie. Pracujący mogą skorzystać z KFS, pożyczki, pomocy pracodawcy albo ulgi.'),
        ('Kto wystawia fakturę?', 'Szkoła wystawia fakturę VAT na osobę albo firmę wskazaną w zgłoszeniu.'),
        ('Czy dofinansowanie obejmuje kursy roczne?', 'Tak. Każda ścieżka dotyczy zarówno kursów rocznych, jak i krótkich.'),
    ], full_link=True, open_first=False)
    body += CTA_2627
    page('dofinansowanie.html', 'Dofinansowanie', body, 'Sześć sposobów na sfinansowanie kursu: urząd pracy, KFS, pożyczka, sponsoring, pracodawca, ulga.')


# ================================================================ KOMPONENTY: formularze, filtry, kadra, blog
def field(label, name, kind='text', required=True, full=False, options=None, hint=''):
    req = '' if required else ' <span class="text-gray-500">(opcjonalne)</span>'
    base = ('mt-1.5 block w-full rounded-lg border border-gray-400 bg-white px-3 text-sm text-gray-900 '
            'focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900')
    if kind == 'textarea':
        control = '<textarea id="%s" name="%s" rows="4" class="%s py-2.5"%s></textarea>' % (name, name, base, ' required' if required else '')
    elif kind == 'select':
        control = '<select id="%s" name="%s" class="%s min-h-11">%s</select>' % (name, name, base, ''.join('<option>%s</option>' % o for o in options))
    else:
        control = '<input id="%s" name="%s" type="%s" class="%s min-h-11"%s>' % (name, name, kind, base, ' required' if required else '')
    help_ = ('<p class="mt-1 text-xs text-gray-600">%s</p>' % hint) if hint else ''
    return ('<div class="%s"><label for="%s" class="text-sm font-medium text-gray-900">%s%s</label>%s%s</div>'
            % ('col-span-2' if full else '', name, label, req, control, help_))


def form(fields, submit, note=''):
    consent = ('<div class="col-span-2 flex items-start gap-3">'
               '<input id="rodo" name="rodo" type="checkbox" required class="mt-0.5 h-5 w-5 rounded border-gray-400">'
               '<label for="rodo" class="text-sm text-gray-700">Wyrażam zgodę na przetwarzanie danych w celu obsługi zgłoszenia. '
               '<a href="#" class="underline">Polityka prywatności</a></label></div>')
    note_html = ('<p class="text-xs text-gray-600">%s</p>' % note) if note else ''
    return ('<form class="grid grid-cols-2 gap-5 rounded-card bg-gray-100 p-8" onsubmit="event.preventDefault()">%s%s'
            '<div class="col-span-2 flex items-center gap-4"><button type="submit" class="btn btn-primary">%s</button>%s</div></form>'
            % (''.join(fields), consent, submit, note_html))


def chips_bar(items, target, mode='filter', center=True):
    html = ''.join('<button type="button" role="tab" data-tab="%s" aria-selected="%s" class="chip">%s</button>'
                   % (k, 'true' if i == 0 else 'false', l) for i, (k, l) in enumerate(items))
    return ('<div role="tablist" data-tabs data-tabs-mode="%s" data-tabs-target="%s" class="flex flex-wrap %s gap-2">%s</div>'
            % (mode, target, 'justify-center' if center else '', html))


def person_card(name, role, courses, cat):
    return ('<article class="card flex flex-col p-4" data-cat="%s">%s<h3 class="mt-4 font-medium text-gray-900">%s</h3>'
            '<p class="text-sm text-gray-600">%s</p><p class="mt-2 text-xs text-gray-600">Prowadzi: %s</p>'
            '<div class="mt-auto pt-3"><a href="#" class="link-arrow">Biogram%s</a></div></article>'
            % (cat, media('Zdjęcie 4:5', 'aspect-[4/5]'), name, role, courses, svg(CHEVRON_RIGHT, 'h-4 w-4')))


def post_card(title, topic, minutes, cat, href='blog-artykul.html'):
    return ('<article data-cat="%s"><a href="%s" class="group block">%s<p class="mt-4 text-xs text-gray-600">%s · %s min czytania</p>'
            '<h3 class="mt-1 text-lg font-medium text-gray-900 group-hover:underline">%s</h3></a></article>'
            % (cat, href, media('Zdjęcie 3:2', 'aspect-[3/2]'), topic, minutes, title))


def grid_section(head, cards, cols=3, extra=''):
    return ('<section class="container-page section">%s<div class="mt-8 grid gap-5" style="grid-template-columns:repeat(%d,minmax(0,1fr))">%s</div>%s</section>'
            % (head, cols, ''.join(cards), extra))


# ================================================================ STRONY: pozostałe podstrony
def dla_firm():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Dla firm', '')])
    body += hero_split(
        'Szkolenia graficzne dla Twojego zespołu',
        'Twój zespół sam przygotuje grafiki, katalogi i wizualizacje, bez zlecania ich agencji. Uczymy Photoshopa, InDesigna, Canvy, Figmy i Blendera, a koszt może pokryć KFS.',
        badges=badge('Dla firm (B2B)', 'dark') + badge('Faktura VAT', 'dark'),
        actions=btn('Zamów wycenę', '#wycena') + btn('Zadzwoń', PHONE_HREF, 'secondary'))
    body += proof_bar([('28 lat', 'Doświadczenia'), ('nr 277460', 'Rejestr MEN'), ('Faktura VAT', 'Na firmę'), ('KFS', 'Pomagamy z wnioskiem')])
    models = [('Szkolenie zamknięte', 'Tylko Twój zespół. Termin i tryb, online albo w Krakowie, ustalamy razem.'),
              ('Miejsca w grupach otwartych', 'Pracownicy dołączają do najbliższych terminów z katalogu kursów krótkich.'),
              ('Program na miarę', 'Łączymy tematy z kilku kursów pod konkretny cel zespołu.')]
    body += grid_section(section_head('Wybierz formę współpracy', 'Dopasujemy zakres, termin i miejsce do potrzeb zespołu.', 'Współpraca'),
                         [info_card(a, b) for a, b in models])
    areas = [('Grafika i Adobe', 'Photoshop, Illustrator i InDesign w codziennej pracy działu marketingu.'),
             ('Grafika 3D i animacja', 'Wizualizacje produktów w Blenderze i animacje w After Effects.'),
             ('Web i UX', 'Figma, badania UX, Webflow i WordPress dla zespołów produktowych.'),
             ('Social media i marketing', 'Grafiki i rolki w Canvie oraz copywriting sprzedażowy.'),
             ('Druk i DTP', 'Skład, typografia i pliki gotowe dla drukarni.'),
             ('Wideo', 'Montaż w Final Cut Pro X i Premiere Pro.')]
    body += grid_section(section_head('Obszary szkoleń', badge_label='Tematy'),
                         [course_card(a, b, '', 'Zobacz kursy', 'kursy-krotkie.html') for a, b in areas])
    body += (steps_section([('Zapytanie', 'Formularz lub telefon'), ('Analiza', 'Rozmowa o potrzebach zespołu'),
                            ('Wycena', 'Oferta w 2 dni robocze'), ('Realizacja', 'Online albo w Krakowie')])
             .replace('>Jak się zapisać<', '>Jak pracujemy<').replace('>Zapisy<', '>Proces<'))
    body += funding_band('Szkolenie może sfinansować KFS',
                         'Firma może pokryć koszt szkolenia ze środków Krajowego Funduszu Szkoleniowego. Przygotujemy ofertę i dokumenty do wniosku.')
    body += faq_section([
        ('Od ilu osób organizujecie szkolenie?', 'Szkolenie zamknięte zorganizujemy już dla małej grupy. Pojedynczych pracowników zapiszemy do grup otwartych.'),
        ('Czy wystawiacie fakturę VAT?', 'Tak, wystawiamy fakturę VAT na firmę.'),
        ('Czy uczestnicy dostaną certyfikat?', 'Tak. Każdy uczestnik dostaje certyfikat z hologramem szkoły.'),
        ('Czy możecie przyjechać do nas?', 'Szkolimy online albo w Krakowie. Szkolenie w siedzibie firmy ustalamy indywidualnie.'),
        ('Czy szkolenie może być online?', 'Tak. Zajęcia online prowadzimy przez Jitsi, bez instalowania aplikacji.'),
    ], 'Wolisz porozmawiać? Zadzwoń %s.' % PHONE, open_first=False)
    quote_form = form([field('Firma', 'firma'), field('Osoba kontaktowa', 'osoba'), field('E-mail', 'email', 'email'), field('Telefon', 'telefon', 'tel'),
                       field('Obszar szkolenia', 'obszar', 'select', options=['Grafika i Adobe', 'Grafika 3D i animacja', 'Web i UX', 'Social media i marketing', 'Druk i DTP', 'Inne']),
                       field('Liczba osób', 'liczba', 'number'), field('Opis potrzeb', 'opis', 'textarea', required=False, full=True)],
                      'Wyślij zapytanie', 'Odpowiemy w 2 dni robocze')
    body += ('<section class="container-page section scroll-mt-24" id="wycena"><div class="grid grid-cols-2 gap-12"><div>%s</div>%s</div></section>'
             % (section_head('Zamów wycenę', 'Odpowiemy w ciągu 2 dni roboczych z propozycją zakresu i ceną.', 'Wycena'), quote_form))
    page('dla-firm.html', 'Dla firm', body, 'Szkolenia graficzne dla zespołów: zamknięte, otwarte i na miarę, z rozliczeniem KFS.')


def o_szkole():
    body = breadcrumbs([('Strona główna', 'index.html'), ('O szkole', '')])
    body += hero_split(
        '28 lat uczymy grafiki',
        'Od 1998 roku przygotowujemy dorosłych do pracy w zawodach graficznych. Uczymy wyłącznie praktycznie: zamiast wykładów pracujesz nad projektami, które trafią do Twojego portfolio.',
        badges=badge('Od 1998 roku', 'dark'),
        actions=btn('Zobacz kursy', 'kursy-krotkie.html') + btn('Poznaj kadrę', 'kadra.html', 'secondary'))
    body += proof_bar(PROOF_5)
    timeline = [('1998', 'Powstaje szkoła grafiki komputerowej w Krakowie.'), ('2019', 'Pierwsze wyróżnienie Orły Edukacji.'),
                ('2021', 'Wpis do Rejestru Instytucji Szkoleniowych WUP w Krakowie.'), ('2025', 'Siódmy rok z rzędu z tytułem Orły Edukacji.'),
                ('Dziś', '4 kierunki roczne i ponad 30 kursów krótkich, online i w Krakowie.')]
    items = ''.join('<li class="relative pt-6"><span class="absolute -top-1.5 left-0 h-3 w-3 rounded-full bg-gray-500"></span>'
                    '<p class="text-lg font-semibold text-gray-900">%s</p><p class="mt-1 text-sm text-gray-600">%s</p></li>' % (y, x) for y, x in timeline)
    body += ('<section class="container-page section">%s<ol class="mt-10 grid grid-cols-5 gap-6 border-t border-gray-300">%s</ol></section>'
             % (section_head('Historia', badge_label='Od 1998'), items))
    body += '<section class="container-page section">%s</section>' % split(
        section_head('Uczymy tego, co przyda się w pracy następnego dnia',
                     'Od pierwszych zajęć pracujesz w programie, a prowadzący pokazują, jak robi się to w prawdziwych projektach. Kończysz z portfolio, a nie z notatkami do szuflady.', 'Misja')
        + stats([('Zjazdy', 'Co 2 weekend'), ('Wyróżnienie', 'Orły Edukacji'), ('Certyfikat', 'Z hologramem')]),
        'Zdjęcie z pracowni', image_left=True)
    docs = [('Rejestr Szkół i Placówek Oświatowych', 'nr 277460'), ('Rejestr Instytucji Szkoleniowych WUP Kraków', 'nr 2.12/00188/2021'), ('Regulamin szkoły', 'PDF · 150 KB')]
    rows = ''.join('<li class="flex items-center justify-between gap-4 border-b border-gray-300 py-4"><span>'
                   '<span class="block text-sm font-medium text-gray-900">%s</span><span class="text-xs text-gray-600">%s</span></span>%s</li>'
                   % (a, b, btn('Pobierz PDF', '#', 'secondary')) for a, b in docs)
    body += ('<section class="container-page section"><div class="grid grid-cols-2 gap-12"><div>%s</div><ul class="border-t border-gray-300">%s</ul></div></section>'
             % (section_head('Dokumenty i uprawnienia', 'Dyplomy i zaświadczenia wydajemy na podstawie wpisów do rejestrów oświatowych.', 'Dokumenty'), rows))
    body += cta_card('Nie wiesz, od czego zacząć?', 'Porozmawiaj z sekretariatem. Pomożemy dobrać kurs i sprawdzimy możliwe dofinansowanie.', CTA_ACTIONS, phone_line=True)
    page('o-szkole.html', 'O szkole', body, 'Publishing School: szkoła grafiki komputerowej w Krakowie od 1998 roku.')


def kadra():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kadra', '')])
    body += hero_center('Uczą praktycy', 'Graficy, projektanci, programiści i poligrafowie, którzy pracują w zawodzie. Uczysz się od ludzi, którzy na co dzień robią to, czego uczą.')
    people = [('mgr Ludmiła Mikołajczyk', 'Grafik DTP · InDesign', 'Grafika DTP', 'dtp'),
              ('dr Justyna Kraszewska-Kozik', 'UX designer', 'Web Designer UI/UX', 'web'),
              ('mgr Anastasiia Dudina', 'Grafik 3D · Blender', 'Blender 3D od podstaw', '3d'),
              ('mgr Natalia Mazurkiewicz-Szafarska', 'Grafik reklamowy', 'Graphic Designer', 'graphic'),
              ('mgr inż. Jan Ślebodziński', 'Web designer · Webflow', 'Webflow, WordPress', 'web'),
              ('mgr Karolina Gorączko', 'Grafik 3D · wizualizacje', 'Grafika 3D', '3d'),
              ('dr hab. Magda Szplit-Królikowska', 'Artystka grafik · animacja 2D', 'Graphic Designer', 'graphic'),
              ('mgr Agnieszka Sieprawska', 'Grafik DTP · opakowania', 'Grafika DTP', 'dtp')]
    body += ('<section class="container-page pb-20">%s<div id="kadra-grid" class="mt-10 grid grid-cols-4 gap-5">%s</div></section>'
             % (chips_bar([('all', 'Wszyscy'), ('dtp', 'DTP'), ('web', 'Web i UX'), ('3d', 'Grafika 3D'), ('graphic', 'Graphic Designer')], '#kadra-grid'),
                ''.join(person_card(*p) for p in people)))
    body += cta_card('Chcesz uczyć się u tych osób?', 'Sprawdź kursy i zarezerwuj miejsce w grupie 2026/27.',
                     btn('Zobacz kursy', 'kursy-krotkie.html') + btn('Zadaj pytanie', 'kontakt.html', 'secondary'))
    page('kadra.html', 'Kadra', body, 'Prowadzący Publishing School: praktycy grafiki, UX, 3D i DTP.')


def prace_absolwentow():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Prace absolwentów', '')])
    body += hero_center('Prace absolwentów', 'Projekty, które powstały na kursach. Tak wygląda portfolio po zakończeniu nauki.')
    works = [('3d', 'Grafika 3D', 'Sylwia K.', '2025/26'), ('web', 'Web Designer UI/UX', 'Michał P.', '2025/26'), ('dtp', 'Grafika DTP', 'Tomasz L.', '2024/25'),
             ('graphic', 'Graphic Designer', 'Anna W.', '2024/25'), ('web', 'Web Designer UI/UX', 'Karolina Z.', '2024/25'), ('3d', 'Grafika 3D', 'Piotr S.', '2023/24'),
             ('dtp', 'Grafika DTP', 'Ewa M.', '2023/24'), ('graphic', 'Graphic Designer', 'Jan R.', '2023/24'), ('web', 'Web Designer UI/UX', 'Olga N.', '2023/24')]
    cards = ''.join('<figure data-cat="%s">%s<figcaption class="mt-3 flex justify-between text-sm"><span class="font-medium text-gray-900">%s</span>'
                    '<span class="text-gray-600">%s · rocznik %s</span></figcaption></figure>' % (c, media('Praca 4:3'), k, n, r) for c, k, n, r in works)
    body += ('<section class="container-page pb-20">%s<div id="prace-grid" class="mt-10 grid grid-cols-3 gap-6">%s</div><div class="mt-10 text-center">%s</div></section>'
             % (chips_bar([('all', 'Wszystkie'), ('dtp', 'DTP'), ('web', 'Web i UX'), ('3d', 'Grafika 3D'), ('graphic', 'Graphic Designer')], '#prace-grid'),
                cards, btn('Pokaż kolejne prace', '#', 'secondary')))
    body += CTA_2627
    page('prace-absolwentow.html', 'Prace absolwentów', body, 'Portfolio absolwentów Publishing School: 3D, UX/UI, DTP i grafika reklamowa.')


def blog():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Blog', '')])
    body += hero_split(
        'Jak zbudować pierwsze portfolio UX bez doświadczenia',
        'Pracodawcy w UX patrzą najpierw na portfolio, a nie na dyplom. Pokazujemy, jak w kilka tygodni zebrać 3 projekty, które otworzą Ci drzwi na rozmowę.',
        badges=badge('Najnowszy', 'dark') + badge('Kariera', 'dark'),
        actions=btn('Czytaj artykuł', 'blog-artykul.html'), note='12.09.2026 · 6 min czytania')
    posts = [('Figma czy Adobe XD? Od czego zacząć naukę projektowania', 'Narzędzia', 5, 'narzedzia'),
             ('Plik do druku, który drukarnia przyjmie za pierwszym razem', 'Porady', 7, 'porady'),
             ('Czy po trzydziestce można zostać grafikiem? Historie absolwentów', 'Kariera', 6, 'kariera'),
             ('Orły Edukacji po raz siódmy: co to znaczy dla kursantów', 'Z życia szkoły', 3, 'szkola'),
             ('Blender za darmo: 5 rzeczy, które zrobisz po pierwszym kursie', 'Narzędzia', 5, 'narzedzia'),
             ('Canva w pracy marketera: 7 błędów, których łatwo uniknąć', 'Porady', 4, 'porady')]
    body += ('<section class="container-page section">%s<div class="mt-6">%s</div><div id="blog-grid" class="mt-10 grid grid-cols-3 gap-8">%s</div>'
             '<div class="mt-10 text-center">%s</div></section>'
             % (section_head('Wszystkie artykuły', badge_label='Blog'),
                chips_bar([('all', 'Wszystkie'), ('kariera', 'Kariera'), ('narzedzia', 'Narzędzia'), ('porady', 'Porady'), ('szkola', 'Z życia szkoły')], '#blog-grid', center=False),
                ''.join(post_card(*p) for p in posts), btn('Pokaż kolejne artykuły', '#', 'secondary')))
    page('blog.html', 'Blog', body, 'Blog Publishing School: kariera w grafice, narzędzia i porady.')


ARTICLE_BODY = (
    '<p>Szukasz pierwszej pracy w UX i słyszysz, że bez doświadczenia nie masz szans? Rekruterzy mówią co innego: najpierw oglądają portfolio. '
    'Dobre case study potrafi zastąpić rok stażu.</p>'
    '<h2>Zacznij od problemu, nie od ekranu</h2>'
    '<p>Wybierz usługę, z której korzystasz na co dzień i która Cię irytuje: rezerwację wizyt, formularz w urzędzie, sklep internetowy. '
    'Zapisz, co nie działa i kogo to dotyczy.</p>'
    '<blockquote><p>Pracodawca chce zobaczyć, jak myślisz, a nie tylko jak ładne robisz ekrany.</p></blockquote>'
    '<ul><li>Porozmawiaj z 3–5 osobami, które korzystają z tej usługi</li><li>Narysuj prosty prototyp w Figmie i przetestuj go</li>'
    '<li>Opisz, co zmieniłeś po testach i dlaczego</li></ul>'
    '<h2>Trzy projekty wystarczą</h2>'
    '<p>Lepiej pokazać trzy dopracowane case study niż dziesięć pięknych ekranów bez historii. Na kursie Web Designer UI/UX każdy moduł kończy się projektem, '
    'więc portfolio budujesz w trakcie nauki.</p>')


def blog_artykul():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Blog', 'blog.html'), ('Jak zbudować pierwsze portfolio UX', '')])
    body += ('<article><header class="container-page pb-10 pt-10"><div class="mx-auto max-w-3xl">'
             '<p class="flex items-center gap-3 text-sm text-gray-600"><a href="blog.html" class="badge">Kariera</a>'
             '<time datetime="2026-09-12">12.09.2026</time><span>· 6 min czytania</span></p>'
             '<h1 class="h1 mt-4">Jak zbudować pierwsze portfolio UX bez doświadczenia</h1></div>'
             '<div class="mx-auto mt-10 max-w-5xl">%s</div></header>'
             '<div class="container-page"><div class="prose prose-gray mx-auto max-w-[68ch] pb-16">%s</div></div></article>'
             % (media('Zdjęcie 16:9', 'aspect-video'), ARTICLE_BODY))
    body += ('<section class="container-page pb-20"><div class="mx-auto max-w-5xl">%s<div class="mt-6 grid grid-cols-2 gap-5">%s%s</div></div></section>'
             % (section_head('Chcesz nauczyć się tego w praktyce?', badge_label='Polecane kursy'),
                course_card('Web Designer UI/UX', 'Kurs roczny od podstaw do portfolio, zjazdy co drugi weekend.', 'Wrzesień – czerwiec · online / Kraków'),
                course_card('Kurs UX — User Experience', 'Heurystyki, badania i wireframing w 16 godzin.', '16 h · online lub Kraków · 530 zł', 'Zobacz kurs', 'kursy-krotkie.html')))
    page('blog-artykul.html', 'Jak zbudować pierwsze portfolio UX', body, 'Jak zebrać 3 projekty do portfolio UX bez doświadczenia zawodowego.')


def kontakt():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kontakt', '')])
    body += hero_center('Kontakt', 'Zadzwoń albo napisz. Odpowiadamy najpóźniej następnego dnia roboczego.')
    body += proof_bar([(PHONE, 'Telefon, codziennie 9:00–20:00'), ('sekretariat@publishingschool.pl', 'E-mail'),
                       ('ul. Kosynierów 15B', 'II piętro, 31-572 Kraków'), ('pon–pt 12:30–18:30', 'Sekretariat na miejscu')])
    contact_form = form([field('Imię', 'imie'), field('E-mail', 'email', 'email'), field('Telefon', 'telefon', 'tel', required=False, full=True),
                         field('Temat', 'temat', 'select', full=True, options=['Kurs roczny', 'Kurs krótki', 'Dofinansowanie', 'Oferta dla firm', 'Inne']),
                         field('Wiadomość', 'wiadomosc', 'textarea', full=True)],
                        'Wyślij wiadomość', 'Odpowiemy najpóźniej następnego dnia roboczego')
    body += ('<section class="container-page section"><div class="grid grid-cols-2 gap-12"><div>%s<div class="mt-6">%s</div></div>%s</div></section>'
             % (section_head('Napisz do nas', 'Zapytaj o kurs, termin, dofinansowanie albo ofertę dla firmy.', 'Formularz'),
                media('Mapa Google (opcjonalnie)'), contact_form))
    body += faq_section([
        ('W jakich godzinach mogę zadzwonić?', 'Telefon odbieramy codziennie w godzinach 9:00–20:00.'),
        ('Czy mogę przyjść do szkoły bez umówienia?', 'Sekretariat jest czynny pon–pt 12:30–18:30. Przed wizytą najlepiej zadzwonić.'),
        ('Jak szybko odpowiadacie na e-maile?', 'Najpóźniej następnego dnia roboczego.'),
    ], open_first=False)
    page('kontakt.html', 'Kontakt', body, 'Kontakt z Publishing School: telefon, e-mail, adres i formularz.')



if __name__ == '__main__':
    home()
    kurs_roczny()
    kursy_krotkie()
    kurs_krotki()
    jak_sie_zapisac()
    dofinansowanie()
    dla_firm()
    o_szkole()
    kadra()
    prace_absolwentow()
    blog()
    blog_artykul()
    kontakt()
