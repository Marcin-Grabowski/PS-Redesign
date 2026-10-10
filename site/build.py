"""Generator stron Publishing School (desktop).

Każda funkcja w sekcji KOMPONENTY zwraca fragment HTML z klasami Tailwinda.
Strony są składane z komponentów w sekcji STRONY i zapisywane obok tego pliku.
Uruchom:  python3 build.py
"""
import os
import re

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
  .btn-brand { @apply min-h-12 bg-brand px-4 text-base text-white hover:bg-brand-dark; }
  .btn-brand-outline { @apply min-h-12 border border-brand bg-transparent px-4 text-base text-brand hover:bg-brand-soft; }
  .btn-ghost { @apply min-h-12 border border-neutral-500 bg-transparent px-4 text-base text-neutral-600 hover:border-ink hover:text-ink; }
  .btn-solid { @apply min-h-12 border border-neutral-500 bg-neutral-500 px-4 text-base text-white hover:bg-neutral-600; }
  .eyebrow { @apply text-sm uppercase text-neutral-600; }
  .ps-h2 { @apply text-4xl font-medium leading-10 text-ink; }
  .ps-card { @apply flex flex-col gap-6 rounded-card border border-neutral-500 p-6 text-olive shadow-[0_1px_1px_rgba(0,0,0,0.05)]; }
  .ps-link { @apply inline-flex min-h-11 items-center gap-3 text-base font-medium text-olive hover:underline; }
  .ps-card.course-card { @apply relative border-transparent bg-white text-gray-600 shadow-sm ring-1 ring-gray-950/5 transition hover:-translate-y-0.5 hover:shadow-lg hover:ring-brand/30; }
  .course-card h3 { @apply font-semibold tracking-tight text-gray-900; }
  .course-card .ps-link { @apply text-brand-dark no-underline hover:no-underline; }
  .course-card .ps-link::after { content: ''; position: absolute; inset: 0; border-radius: inherit; }
  .course-card .ps-link:focus-visible { @apply outline-none; }
  .course-card:has(.ps-link:focus-visible) { @apply ring-2 ring-brand; }
  .course-card:hover .ps-link svg, .course-card:hover .ps-link img { @apply translate-x-0.5; }
  .btn-on-dark { @apply border border-white bg-white text-gray-900 hover:bg-gray-100; }
  .badge { @apply inline-flex items-center rounded-full bg-gray-200 px-2.5 py-0.5 text-xs font-medium text-gray-700; }
  .badge-dark { @apply bg-gray-500 text-white; }
  .badge-accent { @apply bg-teal-50 text-teal-700; }
  .card { @apply rounded-card border border-gray-400 bg-gray-50 p-6; }
  .chip { @apply inline-flex min-h-11 items-center gap-2 rounded-full border border-gray-400 bg-white px-4 text-sm text-gray-900 hover:border-gray-900; }
  .chip-active { @apply border-gray-500 bg-gray-500 text-white hover:border-gray-600; }
  .seg { @apply inline-flex min-h-11 items-center px-4 text-sm text-brand-dark hover:bg-brand-soft; }
  .seg + .seg { @apply border-l border-brand; }
  .seg[aria-selected='true'] { @apply bg-brand text-white hover:bg-brand; }
  .link-arrow { @apply inline-flex min-h-11 items-center gap-2 text-sm font-medium text-gray-900 hover:underline; }
  .ph { background: repeating-linear-gradient(45deg, theme('colors.gray.200') 0 10px, theme('colors.gray.100') 10px 20px); }
  .spy-active { @apply border-gray-900 text-gray-900; }
}
"""

# Delikatne, rozmyte plamy koloru w tle górnej części strony — tech-minimalizm z akcentem SaaS.
# fixed + -z-10, więc świecą przez przezroczyste sekcje i gasną pod nieprzezroczystymi (header, karty).
BG_BLOBS = (
    '<div aria-hidden="true" class="pointer-events-none fixed inset-x-0 top-0 -z-10 h-[720px] overflow-hidden"'
    ' style="mask-image:linear-gradient(to bottom, black, transparent);-webkit-mask-image:linear-gradient(to bottom, black, transparent)">'
    '<div class="absolute -left-24 -top-28 h-[340px] w-[340px] rounded-full bg-fuchsia-400/10 blur-[90px]"></div>'
    '<div class="absolute right-[-80px] top-16 h-[300px] w-[300px] rounded-full bg-cyan-300/10 blur-[90px]"></div>'
    '<div class="absolute left-[42%] top-[360px] h-[260px] w-[260px] rounded-full bg-lime-300/10 blur-[80px]"></div>'
    '</div>'
)

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
HOME_SVG = ('<svg class="h-5 w-5 shrink-0" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="'
            'M9.293 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 17 11h-1v6a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3a1 1 0 0 0-1-1H9'
            'a1 1 0 0 0-1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6H3a1 1 0 0 1-.707-1.707l7-7Z"/></svg>')
_UNUSED_HOME = ('M9.293 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 17 11h-1v6a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3a1 1 0 0 0-1-1H9'
        'a1 1 0 0 0-1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6H3a1 1 0 0 1-.707-1.707l7-7Z')
SLASH = ('<svg class="h-full w-6 shrink-0 text-gray-200" viewBox="0 0 24 44" preserveAspectRatio="none" fill="currentColor" aria-hidden="true">'
         '<path d="M.293 0l22 22-22 22h1.414l22-22-22-22H.293z"/></svg>')
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


LOGO_PARTS = [('magenta', '1.67%', '0.45%'), ('lime', '29.82%', '17.33%'), ('cyan', '62%', '6.32%'), ('text', '14.68%', '35.65%')]


def logo(light=False):
    # logo z Figmy złożone z 4 warstw SVG (rozmiar z atrybutów SVG, pozycja wg makiety)
    suffix, size = ('-footer', 'h-16 w-[214px]') if light else ('', 'h-12 w-40')
    layers = ''.join('<img src="assets/figma/logo-%s%s.svg" alt="" class="absolute block max-w-none" style="top:%s;left:%s">'
                     % (name, suffix, top, left) for name, top, left in LOGO_PARTS)
    return '<span class="relative block shrink-0 %s" aria-hidden="true">%s</span>' % (size, layers)


def breadcrumbs(items):
    """Okruszki wg komponentu Tailwind UI „simple with slashes”.

    items: [(etykieta, href)] — pierwszy element renderuje się jako ikona domu,
    ostatni jako tekst bieżącej strony, element bez href jako nieklikalny poziom.
    """
    label_cls = 'ml-4 text-sm font-medium'
    parts = []
    for i, (label, href) in enumerate(items):
        last = i == len(items) - 1
        if i == 0:
            parts.append('<li><a href="%s" class="flex min-h-11 items-center text-gray-400 hover:text-gray-500">%s'
                         '<span class="sr-only">%s</span></a></li>'
                         % (href or '#', HOME_SVG, label))
            continue
        if last:
            inner = '<span aria-current="page" class="%s text-gray-700">%s</span>' % (label_cls, label)
        elif href:
            inner = '<a href="%s" class="%s flex min-h-11 items-center text-gray-500 hover:text-gray-700">%s</a>' % (href, label_cls, label)
        else:
            inner = '<span class="%s text-gray-500">%s</span>' % (label_cls, label)
        parts.append('<li><div class="flex items-center">%s%s</div></li>' % (SLASH, inner))
    return ('<nav aria-label="Okruszki" class="container-page pt-6"><ol role="list" class="flex items-center space-x-4">%s</ol></nav>'
            % ''.join(parts))


# ---------------------------------------------------------------- nagłówek i stopka
NAV = [
    ('Kurs', [('Kursy roczne', [('Grafika 3D', 'kurs-grafika-3d.html'), ('Web Designer UI/UX', 'kurs-web-designer.html'),
                                ('Grafika DTP', 'kurs-grafika-dtp.html'), ('Graphic Designer', 'kurs-graphic-designer.html')]),
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
    return ('<header class="sticky top-0 z-40 bg-page/95 backdrop-blur">'
            '<div class="container-page flex h-20 items-center justify-between">'
            '<a href="index.html" aria-label="Publishing School, strona główna">%s</a>'
            '<nav aria-label="Główna"><ul class="flex items-center gap-6 text-base font-medium text-ink">%s</ul></nav>'
            '%s</div></header>' % (logo(), ''.join(items), btn('Zapytaj o kurs', 'kontakt.html', 'brand')))


def footer():
    def col(title, links):
        return ('<nav data-name="link-group" aria-label="%s"><p data-name="title" class="text-base font-semibold text-page">%s</p><ul data-name="links" class="mt-4 space-y-3 text-base font-medium text-page">%s</ul></nav>'
                % (title, title, ''.join('<li><a data-name="link" href="%s" class="hover:underline">%s</a></li>' % (h, l) for l, h in links)))
    return f'''<footer data-name="footer" class="bg-stopka text-page">
  <div class="container-page pb-12 pt-20">
    <div data-name="top" class="flex items-start justify-between">
      <div data-name="brand"><a data-name="logo" href="index.html" aria-label="Publishing School, strona główna">{logo(light=True)}</a><p data-name="tagline" class="mt-2 text-base font-medium">Szkoła grafiki komputerowej</p></div>
      <a data-name="social-link" href="https://www.facebook.com/" class="flex h-12 w-12 items-center justify-center" aria-label="Facebook"><img src="assets/figma/facebook.svg" alt="" width="24" height="24"></a>
    </div>
    <div data-name="cta-band" class="mt-6 flex items-center justify-between border-y border-gray-400 py-6">
      <p data-name="heading" class="text-2xl leading-8">Szkolisz pracowników? Kurs dopasujemy do Twojego zespołu.</p>
      {btn('Oferta dla firm', 'dla-firm.html', 'brand')}
    </div>
    <div data-name="columns" class="mt-6 flex items-start justify-between gap-10 text-sm leading-5">
      <address data-name="contact" class="space-y-4 not-italic">
        <p data-name="org">„Publishing School”<br>Placówka Kształcenia Ustawicznego</p>
        <p data-name="address">Adres:<br>ul. Kosynierów 15B, II piętro<br>31-572 Kraków</p>
        <p data-name="hours">Sekretariat czynny:<br>pon–pt, 12:30–18:30</p>
        <p data-name="email">E-mail: <a href="mailto:sekretariat@publishingschool.pl" class="hover:underline">sekretariat@publishingschool.pl</a></p>
      </address>
      <div data-name="link-columns" class="flex gap-16">
        {col('Kursy', [('Grafika 3D', 'kurs-grafika-3d.html'), ('Web Designer UI/UX', 'kurs-web-designer.html'), ('Grafika DTP', 'kurs-grafika-dtp.html'), ('Graphic Designer', 'kurs-graphic-designer.html'), ('Kursy krótkie', 'kursy-krotkie.html')])}
        {col('Rekrutacja', [('Zapisy', 'jak-sie-zapisac.html'), ('Formularz zapisu', 'jak-sie-zapisac.html'), ('Dofinansowanie kursów', 'dofinansowanie.html')])}
        {col('O nas', [('O szkole', 'o-szkole.html'), ('Kadra', 'kadra.html'), ('Prace absolwentów', 'prace-absolwentow.html'), ('Blog', 'blog.html'), ('Kontakt', 'kontakt.html')])}
      </div>
    </div>
    <div data-name="legal" class="mt-10 flex items-center justify-between border-t border-gray-500 pt-5 text-xs">
      <p data-name="copyright">© 2026 Publishing School — Wszystkie prawa zastrzeżone</p>
      <ul data-name="legal-links" class="flex gap-6"><li><a data-name="link" href="#" class="hover:text-white hover:underline">Polityka prywatności</a></li><li><a data-name="link" href="#" class="hover:text-white hover:underline">RODO</a></li><li><a data-name="link" href="#" class="hover:text-white hover:underline">Procedura reklamacyjna</a></li></ul>
    </div>
  </div>
</footer>'''


# ---------------------------------------------------------------- sekcje
def hero_split(title, lead, actions='', badges='', badges_after='', note='', image='Zdjęcie 4:3', top='pt-6', img_html=''):
    return f'''<section class="container-page grid grid-cols-2 items-center gap-12 pb-16 {top}">
  <div>
    {'<div class="flex gap-2">' + badges + '</div>' if badges else ''}
    <h1 class="h1 mt-4">{title}</h1>
    <p class="lead mt-4 max-w-xl">{lead}</p>
    {'<div class="mt-4 flex flex-wrap gap-2">' + badges_after + '</div>' if badges_after else ''}
    {'<div class="mt-6 flex flex-wrap items-center gap-3">' + actions + '</div>' if actions else ''}
    {'<p class="mt-3 text-xs text-gray-600">' + note + '</p>' if note else ''}
  </div>
  {img_html or media(image)}
</section>'''


def hero_center(title, lead):
    return f'''<section class="container-page py-20 text-center">
  <h1 class="h1 mx-auto max-w-3xl">{title}</h1>
  <p class="lead mx-auto mt-4 max-w-2xl">{lead}</p>
</section>'''


def photo(src, alt, width, height, extra='', lazy=True):
    return ('<img src="assets/img/%s" width="%d" height="%d" alt="%s" class="w-full rounded-3xl object-cover %s"%s>'
            % (src, width, height, alt, extra, ' loading="lazy"' if lazy else ' fetchpriority="high"'))


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


def course_card(title, text, meta='', link_label='Zobacz program', href='index.html#kursy-roczne', center_link=False, cat='', extra=''):
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


def split(content, image_label='Zdjęcie 4:3', image_left=False, img_html=''):
    img = img_html or media(image_label)
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


def reviews(cards, title='Opinie absolwentów i słuchaczy z Google'):
    items = ''.join(f'''<article class="card w-[calc((100%-4.5rem)/4)] shrink-0 snap-start">
  <p class="flex gap-1 text-gray-900" aria-label="Ocena 5 na 5">{''.join(svg(STAR, 'h-4 w-4', stroke=False) for _ in range(5))}</p>
  <p class="mt-3 text-sm text-gray-700">{text}</p>
  <p class="mt-3 text-sm font-medium text-gray-900">{name}</p>
  <a href="{href}" class="link-arrow">{course}{svg(CHEVRON_RIGHT, 'h-4 w-4')}</a>
</article>''' for text, name, course, href in cards)
    return f'''<section class="container-page section" data-carousel>
  {section_head(title, badge_label='Opinie')}
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


def page(filename, title, body, description='', head_extra=''):
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
<script src="assets/tailwind.config.js?v=2"></script>
<style type="text/tailwindcss">{COMPONENT_CSS}</style>
<style>[hidden]{{display:none!important}}</style>
{head_extra}
</head>
<body class="min-w-[1280px] bg-page font-sans text-gray-900 antialiased">
{BG_BLOBS}
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
# wg makiety Figma „PS Lo-Fi” (node 3873:18431) — pasek dowodowy strony głównej
PROOF_HOME = [('Od 1998 r.', 'uczymy grafiki'), ('Orły Edukacji', '2019–2025'), ('Status słuchacza', 'ZUS, KRUS i UP'),
              ('RSPO nr 277460', 'rejestr MEN'), ('Rejestr WUP', 'nr 2.12/00188/2021')]
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
# ---------------------------------------------------------------- strona główna wg Figmy (PS Lo-Fi, node 3873:18431)
CHEV = '<img src="assets/figma/chevron-right.svg" alt="" width="24" height="24">'
CHEV_GRAY = '<img src="assets/figma/chevron-right-2.svg" alt="" width="24" height="24">'


def ps_head(eyebrow, title, lead='', center=True):
    align = 'items-center text-center' if center else 'items-start'
    lead_html = ('<p class="%s text-ink">%s</p>' % ('text-lg leading-7' if center else 'text-base leading-6', lead)) if lead else ''
    return ('<div class="flex flex-col gap-4 %s"><p class="eyebrow">%s</p><h2 class="ps-h2">%s</h2>%s</div>'
            % (align, eyebrow, title, lead_html))


def ps_card(title, text, link_label, href, icon='', extra=''):
    icon_html = ('<span class="flex h-16 items-center" aria-hidden="true"><img src="assets/figma/%s.svg" alt=""></span>' % icon) if icon else ''
    if icon and 'course-card' in extra:
        m = f"url(assets/figma/{icon}.svg) center/contain no-repeat"
        icon_html = f'<span class="flex h-16 w-16 items-center justify-center rounded-2xl bg-brand-soft" aria-hidden="true"><span class="block h-8 w-8 bg-brand" style="-webkit-mask:{m};mask:{m}"></span></span>'
    return f'''<article class="ps-card {extra}">
  {icon_html}
  <div class="flex flex-1 flex-col justify-between">
    <div class="flex flex-col gap-4"><h3 class="text-2xl leading-8">{title}</h3><p class="text-base leading-6">{text}</p></div>
    <div class="pt-6"><a href="{href}" class="ps-link">{link_label}{CHEV}</a></div>
  </div>
</article>'''


def home():
    ic = lambda d: f'<svg class="h-5 w-5 text-brand" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="{d}"/></svg>'
    hero = f'''<section class="relative overflow-hidden">
  <div class="container-page grid grid-cols-12 items-center gap-x-12 pb-24 pt-16">
    <div class="col-span-7">
      <a href="#kursy-roczne" class="inline-flex items-center gap-2 rounded-full bg-brand-soft px-3 py-1 text-sm font-medium text-brand-dark ring-1 ring-inset ring-brand/20 hover:ring-brand/40">Nabór na kursy roczne do 30 września · start na koniec miesiąca<svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m9 6 6 6-6 6"/></svg></a>
      <h1 class="mt-6 whitespace-nowrap text-[3.5rem] font-semibold leading-[1.08] tracking-tight text-gray-900">Zostań grafikiem.<br><span class="text-brand">Od podstaw do portfolio.</span></h1>
      <p class="mt-6 max-w-xl text-lg leading-8 text-gray-600">Kursy roczne z grafiki 3D, DTP, web designu i reklamy. Uczysz się od praktyków i kończysz z portfolio oraz dyplomem polsko-angielskim.</p>
      <ul class="mt-8 flex flex-wrap gap-x-8 gap-y-3 text-base text-gray-700">
        <li class="flex items-center gap-2">{ic('M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z')}Co drugi weekend</li>
        <li class="flex items-center gap-2">{ic('M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Zm0-8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z')}Online na żywo lub w Krakowie</li>
        <li class="flex items-center gap-2">{ic('M12 6v12M15 9.5c0-1.4-1.3-2.5-3-2.5s-3 1.1-3 2.5 1.3 2.2 3 2.5 3 1.1 3 2.5-1.3 2.5-3 2.5-3-1.1-3-2.5M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0Z')}11 rat 0% lub dofinansowanie KFS</li>
      </ul>
      <div class="mt-10 flex items-center gap-3"><a href="#kursy-roczne" class="btn btn-brand shadow-sm">Wybierz kierunek</a><a href="{PHONE_HREF}" class="btn btn-brand bg-white text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Zadzwoń: 504 068 626</a></div>
      <p class="mt-4 text-sm text-gray-600">Wahasz się? Sekretariat pomoże dobrać kurs — codziennie 9:00–20:00. <a href="kursy-krotkie.html" class="font-medium text-brand-dark underline-offset-4 hover:underline">Zobacz też kursy krótkie →</a></p>
    </div>
    <div class="relative col-span-5">
      <svg aria-hidden="true" viewBox="0 0 600 600" class="absolute -right-24 top-1/2 h-[640px] w-[640px] -translate-y-1/2 text-brand-soft"><path fill="currentColor" d="M96 150C150 40 330 10 450 70c90 45 160 120 130 230-25 90-120 120-90 200 15 40-40 80-140 85C240 592 70 560 40 430 15 320 40 250 96 150Z"/></svg>
      <img src="assets/img/hero-probnik-kolorow.webp" width="766" height="1164" alt="Kursantka porównuje próbniki kolorów Pantone" class="relative aspect-[4/5] w-full rounded-3xl object-cover shadow-xl ring-1 ring-gray-900/10" fetchpriority="high">
      <div class="absolute -left-10 bottom-10 flex items-center gap-3 rounded-2xl bg-white px-4 py-3 shadow-lg ring-1 ring-gray-900/5"><span class="text-3xl font-semibold tracking-tight text-brand">1998</span><span class="text-sm leading-5 text-gray-600">uczymy grafiki<br>Orły Edukacji 2019–2025</span></div>
    </div>
  </div>
</section>'''

    stats = ''.join(f'<div class="flex-1 px-6 py-8 text-center"><dd class="text-xl font-semibold text-gray-900">{a}</dd><dt class="mt-1 text-sm text-gray-600">{b}</dt></div>'
                    for a, b in PROOF_HOME if '1998' not in a)
    proof = f'<section aria-label="Najważniejsze informacje" class="border-y border-gray-200 bg-white"><dl class="container-page flex divide-x divide-gray-200">{stats}</dl></section>'

    router = f'''<section class="container-page py-20" id="kursy-roczne">
  {ps_head('Kursy roczne', 'Kursy roczne — 9 miesięcy przygotowania do pracy w grafice', 'Wybierz specjalizację. 200 godzin zajęć w soboty i niedziele, od końca września do końca czerwca — online na żywo albo w Krakowie. Kończysz z portfolio i dyplomem polsko-angielskim.')}
  <div class="mt-10 grid grid-cols-2 gap-6">{''.join(ps_card(c['name'], c['card'], 'Zobacz program<span class="sr-only"> kursu ' + c['name'] + '</span>', c['slug'], c['icon'], extra='course-card') for c in COURSES)}</div>
</section>'''

    short = f'''<section class="container-page py-20">
  {ps_head('Kursy krótkie', 'Krótkie kursy — pogłęb konkretną umiejętność', 'Nie potrzebujesz całego roku? Wybierz jeden temat lub narzędzie i zacznij w najbliższym terminie.')}
  <div class="mt-6 grid grid-cols-2 gap-6">
    {ps_card('Blender 3D od podstaw', 'Modelujesz, teksturujesz i renderujesz własną scenę do portfolio. Najbliższy termin: 17, 18 i 24.10.2026, online, 9:00–13:30 · 870 zł.', 'Zobacz program i termin<span class="sr-only"> kursu Blender 3D od podstaw</span>', 'kurs-krotki.html', 'icon-printer', extra='course-card')}
    <div class="grid grid-cols-2 gap-6">
      {ps_card('Wszystkie kursy krótkie', 'Nie potrzebujesz całego roku? Wybierz jedno narzędzie lub temat i porównaj terminy oraz ceny.', 'Zobacz katalog kursów', 'kursy-krotkie.html', 'icon-printer', extra='course-card')}
      {ps_card('Szkolenie dla zespołu', 'Dopasujemy zakres, termin i miejsce do potrzeb Twojej firmy. Wycenę dostajesz w 2 dni robocze.', 'Zamów wycenę', 'dla-firm.html#wycena', 'icon-printer', extra='course-card')}
    </div>
  </div>
</section>'''

    acc_items = [
        ('Pracuję lub prowadzę działalność', ab('Masz dwie drogi, a sekretariat pomoże wybrać lepszą.', [
            'KFS: wniosek składa pracodawca w urzędzie pracy',
            'działalność gospodarcza: kurs wliczasz w koszty i dostajesz fakturę',
            'raty 0%, jeśli wolisz zapłacić sam(a)'],
            '<a href="dofinansowanie.html" class="text-brand hover:underline">Zobacz opcje dla pracujących</a>')),
        ('Szukam pracy albo chcę zmienić zawód', ab('Urząd pracy może pomóc Ci zmienić zawód.', [
            'bon szkoleniowy lub opłacenie kursu przez urząd, jeśli jesteś zarejestrowana/y',
            'nieoprocentowana pożyczka na kształcenie, częściowo umarzana',
            'status słuchacza honorowany przez urzędy pracy i ZUS',
            'pierwszy krok: rozmowa z sekretariatem, który powie, co zrobić po kolei'])),
        ('Szkolę pracowników', ab('Szkolenie zespołu możesz sfinansować z KFS.', [
            'przygotujemy ofertę i komplet dokumentów do wniosku',
            'fakturę wystawimy na firmę',
            'kurs dopasujemy do poziomu i potrzeb zespołu'],
            '<a href="dla-firm.html" class="text-brand hover:underline">Zobacz ofertę dla firm</a>')),
    ]
    acc = ps_accordion(acc_items)
    funding = f'''<section class="container-page py-20" id="dofinansowanie">
  <div class="flex items-start gap-6">
    <div class="w-[628px] shrink-0">
      <div class="max-w-[543px] pb-5">{ps_head('Dofinansowania', 'Sprawdź, jak sfinansować kurs w Twojej sytuacji', 'Jesteśmy w Rejestrze Instytucji Szkoleniowych WUP (nr 2.12/00188/2021), więc za kurs może zapłacić urząd pracy albo KFS. Sekretariat pomoże przygotować dokumenty.', center=False)}</div>
      <a href="dofinansowanie.html" class="btn btn-ghost">Zobacz wszystkie opcje dofinansowania{CHEV_GRAY}</a>
      <p class="mt-2 text-xs text-black">Informacje ogólne. O przyznaniu dofinansowania decyduje urząd pracy.</p>
    </div>
    <div class="flex-1">{acc}</div>
  </div>
</section>'''

    school_stats = [('28 lat', 'uczymy grafiki'), ('200 h', 'praktyki na każdym kierunku'), ('4 kierunki', 'roczne i ponad 30 kursów krótkich')]
    school_dl = ''.join(f'<div class="flex h-[102px] flex-1 flex-col justify-center gap-2 rounded-2xl"><dt class="order-2 text-base leading-6">{b}</dt><dd class="order-1 text-2xl font-semibold leading-8">{a}</dd></div>'
                        for a, b in school_stats)
    school = f'''<section class="container-page py-20">
  <div class="flex items-center gap-6">
    <div class="flex flex-1 justify-center">
      <img src="assets/img/o-szkole-laptop.webp" width="1016" height="884" loading="lazy" alt="Kursant pracuje na laptopie przy biurku z linijką i notatkami" class="w-full max-w-[508px] rounded-3xl">
    </div>
    <div class="flex flex-1 flex-col gap-12">
      <div class="flex flex-col items-start gap-6">
        {ps_head('O szkole', 'Uczymy praktycznie, od pierwszych zajęć', 'Uczą graficy, projektanci, programiści i poligrafowie, którzy na co dzień pracują w zawodzie. Od 1998 roku prowadzimy zajęcia bez wykładów — każdy kurs kończysz z pracami do portfolio.', center=False)}
        <a href="o-szkole.html" class="btn btn-ghost">Poznaj szkołę{CHEV_GRAY}</a>
      </div>
      <dl class="flex gap-4 text-ink">{school_dl}</dl>
    </div>
  </div>
</section>'''

    opinions = [('Konkretnie i bez lania wody. Po dwóch weekendach sama przygotowuję grafiki do sklepu.', 'Kursantka, Photoshop'),
                ('Najbardziej przydało mi się przygotowanie plików do druku. Drukarnia nie odsyła już poprawek.', 'Absolwent, Grafika DTP'),
                ('Zaczynałam od zera, a na koniec miałam gotowy render do portfolio. Zajęcia online bez problemów.', 'Kursantka, Blender 3D'),
                ('Po roku miałam portfolio, z którym dostałam pierwszą pracę jako projektantka UI.', 'Absolwentka, Web Designer UI/UX'),
                ('Małe grupy robią różnicę — prowadzący znał mój projekt i pomagał go dopracować.', 'Absolwent, Graphic Designer')]
    stars = ''.join('<img src="assets/figma/star.svg" alt="" width="24" height="24">' for _ in range(5))
    cards = ''.join(f'''<article class="flex w-[411px] shrink-0 snap-start flex-col gap-4 rounded-3xl border border-black bg-alt p-6 shadow-[0_1px_2px_rgba(0,0,0,0.05)]">
  <p class="flex" role="img" aria-label="Ocena 5 na 5">{stars}</p>
  <blockquote class="text-base leading-6 text-ink">{t}</blockquote>
  <div class="flex items-center justify-between gap-4"><p class="text-sm text-neutral-600">{n}</p><span class="flex h-8 items-center rounded-full border border-[#053339] px-2 text-sm font-medium text-olive">Google</span></div>
</article>''' for t, n in opinions)
    reviews_html = f'''<section class="container-page py-20" data-carousel>
  <p class="eyebrow">Opinie</p>
  <div class="mt-6 flex items-start justify-between">
    <h2 class="ps-h2">Opinie słuchaczy w Google</h2>
    <div class="flex gap-6">
      <button type="button" data-carousel-step="-1" class="flex h-12 w-12 items-center justify-center rounded-full bg-neutral-200 hover:bg-neutral-300" aria-label="Poprzednie opinie"><img src="assets/figma/arrow-left.svg" alt="" width="24" height="24"></button>
      <button type="button" data-carousel-step="1" class="flex h-12 w-12 items-center justify-center rounded-full bg-neutral-500 hover:bg-neutral-600" aria-label="Następne opinie"><img src="assets/figma/arrow-right-white.svg" alt="" width="24" height="24"></button>
    </div>
  </div>
  <div data-carousel-track class="mt-6 flex snap-x gap-6 overflow-x-hidden scroll-smooth">{cards}</div>
  <div class="mt-6 text-center"><a href="o-szkole.html" class="btn btn-ghost">Zobacz wszystkie opinie{CHEV_GRAY}</a></div>
</section>'''

    cta = final_cta()
    body = hero + proof + router + short + funding + school + reviews_html + cta
    page('index.html', 'Strona główna', body, 'Szkoła grafiki komputerowej w Krakowie: kursy roczne i krótkie, online i stacjonarnie.')


# ---------------------------------------------------------------- kursy roczne: dane (źródło: publishingschool.pl, 09.2026)
COMMON_BADGES = ('<span class="rounded-full bg-info px-2 py-1 text-sm text-white">Kurs roczny · 200 godzin</span>'
                 '<span class="rounded-full border border-brand-dark px-2 py-1 text-sm text-brand-dark">Online na żywo lub w Krakowie</span>')

COURSES = [
    dict(
        slug='kurs-grafika-3d.html', name='Grafika 3D', icon='icon-printer',
        card='Modelujesz i renderujesz w Blenderze, Cinema 4D i ZBrushu. Kończysz z portfolio 3D pod gry, reklamę i wizualizacje.',
        h1='Grafika 3D — kurs roczny od podstaw do portfolio',
        lead='Modelujesz, animujesz i renderujesz sceny w Blenderze, Cinema 4D, Mai i ZBrushu. 200 godzin praktyki co drugi weekend, online na żywo albo w Krakowie. Kończysz z portfolio pod gry, reklamę i wizualizacje.',
        hero=None, hero_label='Zdjęcie: render 3D kursanta',
        dla=[('Zaczynasz od zera', 'Marzysz o pracy w 3D, ale nie wiesz, od czego zacząć', 'Zaczynamy od interfejsu Blendera i pierwszej bryły. Po 200 godzinach masz modele, animację i render w portfolio.'),
             ('Zmieniasz zawód', 'Chcesz przejść do branży gier, reklamy lub wizualizacji', 'Uczysz się w weekendy, więc nie rezygnujesz z obecnej pracy. Kończysz z portfolio, które pokażesz studiu.'),
             ('Pracujesz w kreatywnej branży', 'Jesteś grafikiem, architektem lub filmowcem i chcesz dodać 3D', 'Dołożysz modelowanie, światło i animację do tego, co już robisz, i weźmiesz droższe zlecenia.'),
             ('Szukasz dofinansowania', 'Zależy Ci, żeby kurs nie obciążył budżetu', 'Urząd pracy może opłacić kurs osobom bezrobotnym, a KFS pracującym. Sekretariat pomoże z dokumentami.')],
        outcomes=['Modelujesz obiekty i postacie — od bryły po detal w ZBrushu',
                  'Ustawiasz światło i materiały, renderujesz sceny w Blenderze i Cinema 4D',
                  'Przygotowujesz modele do gier i uruchamiasz je w Unity',
                  'Planujesz animację na storyboardzie i składasz film w After Effects'],
        jobs=['Grafik 3D w agencji', 'Wizualizator 3D', 'Modelarz postaci do gier', 'Animator 3D', 'Montażysta animacji', 'Freelancer 3D'],
        tools='Blender, Cinema 4D, Maya, ZBrush, Unity, After Effects, Photoshop'),
    dict(
        slug='kurs-grafika-dtp.html', name='Grafika DTP', icon='icon-printer',
        card='Składasz książki, katalogi i opakowania w InDesignie. Uczysz się przygotowywać pliki, które drukarnia przyjmie bez poprawek.',
        h1='Grafika DTP — kurs roczny: publikacje do druku',
        lead='Projektujesz i składasz książki, katalogi, opakowania i plakaty w InDesignie, Photoshopie i Illustratorze. Uczysz się też druku i papieru, więc Twoje pliki drukarnia przyjmie bez poprawek. 200 godzin praktyki, online albo w Krakowie.',
        hero=('hero-probnik-kolorow.webp', 'Kursantka przegląda wzorniki kolorów i katalog druku', 766, 1164),
        dla=[('Zaczynasz od zera', 'Chcesz projektować książki, katalogi i opakowania', 'Uczysz się InDesigna, Photoshopa i Illustratora od podstaw. Każdy moduł kończy się projektem do portfolio.'),
             ('Zmieniasz zawód', 'Szukasz stabilnego zawodu w agencji, wydawnictwie lub drukarni', 'Po kursie składasz publikacje i przygotowujesz pliki do druku. Umiesz też dobrać papier i technikę.'),
             ('Składasz materiały w pracy', 'Pliki wracają z drukarni do poprawki', 'Poznasz prepress: spady, profile kolorów i formaty. Twoje pliki będą przechodzić za pierwszym razem.'),
             ('Szukasz dofinansowania', 'Zależy Ci, żeby kurs nie obciążył budżetu', 'Urząd pracy może opłacić kurs osobom bezrobotnym, a KFS pracującym. Sekretariat pomoże z dokumentami.')],
        outcomes=['Składasz książki, katalogi i ulotki w InDesignie',
                  'Retuszujesz zdjęcia w Photoshopie i rysujesz logotypy w Illustratorze',
                  'Przygotowujesz pliki do druku (prepress), które drukarnia przyjmie bez poprawek',
                  'Dobierasz papier, technikę druku i uszlachetnienia do projektu'],
        jobs=['Grafik DTP w agencji', 'Grafik w wydawnictwie', 'Specjalista prepress w drukarni', 'Redaktor techniczny', 'Operator druku cyfrowego', 'Grafik freelancer'],
        tools='InDesign, Photoshop, Illustrator'),
    dict(
        slug='kurs-web-designer.html', name='Web Designer UI/UX', icon='icon-uxui',
        card='Projektujesz w Figmie, budujesz strony w WordPressie i Webflow, kodujesz w HTML i CSS. Nie potrzebujesz doświadczenia.',
        h1='Web Designer UI/UX — kurs roczny od podstaw do portfolio',
        lead='Projektujesz strony i aplikacje w Figmie, budujesz je w WordPressie i Webflow, a layout kodujesz w HTML i CSS. 200 godzin praktyki co drugi weekend, online na żywo albo w Krakowie. Kończysz z portfolio i dyplomem polsko-angielskim.',
        hero=('web-designer-kod.webp', 'Dwie osoby analizują kod strony na ekranie laptopa', 996, 1164),
        dla=[('Zaczynasz od zera', 'Chcesz projektować strony, ale nie znasz Figmy ani kodu', 'Nie potrzebujesz doświadczenia. Od projektu w Figmie po stronę w WordPressie i Webflow prowadzimy Cię krok po kroku.'),
             ('Zmieniasz zawód', 'Chcesz wejść do IT bez studiów informatycznych', 'W 200 godzin budujesz portfolio z responsywnymi projektami i stronami. Uczysz się w weekendy, obok pracy.'),
             ('Pracujesz w marketingu, e-commerce lub grafice', 'Czekasz tygodniami na stronę od agencji lub programisty', 'Sam(a) zaprojektujesz landing page, postawisz go i zoptymalizujesz pod SEO.'),
             ('Szukasz dofinansowania', 'Zależy Ci, żeby kurs nie obciążył budżetu', 'Urząd pracy może opłacić kurs osobom bezrobotnym, a KFS pracującym. Sekretariat pomoże z dokumentami.')],
        outcomes=['Projektujesz responsywne strony i aplikacje w Figmie — z design systemem i prototypem',
                  'Budujesz stronę w WordPressie lub Webflow i optymalizujesz ją pod SEO',
                  'Kodujesz layout w HTML5 i CSS3',
                  'Przygotowujesz banery, grafiki i animacje na stronę'],
        jobs=['Web designer', 'UI designer', 'Grafik stron i aplikacji', 'Twórca stron WordPress', 'Koder HTML/CSS', 'Freelancer'],
        tools='Figma, WordPress, Webflow, HTML, CSS, Photoshop, Illustrator, After Effects'),
    dict(
        slug='kurs-graphic-designer.html', name='Graphic Designer', icon='icon-megafon',
        card='Projektujesz kampanie, logo i rolki do internetu i druku, a teksty reklamowe piszesz z pomocą AI.',
        h1='Graphic Designer — kurs roczny: reklama do internetu i druku',
        lead='Projektujesz kampanie, logo, posty i plakaty w Photoshopie, Illustratorze i InDesignie, montujesz rolki i krótkie filmy reklamowe, piszesz teksty z pomocą AI. 200 godzin praktyki, online albo w Krakowie.',
        hero=('o-szkole-laptop.webp', 'Kursant projektuje na laptopie przy biurku z notatkami', 1016, 884),
        dla=[('Zaczynasz od zera', 'Chcesz projektować reklamy, logo i posty jak profesjonalista', 'Uczysz się Photoshopa, Illustratora i InDesigna od podstaw. Po kursie masz kampanię i identyfikację marki w portfolio.'),
             ('Zmieniasz zawód', 'Szukasz pracy w agencji reklamowej lub dziale marketingu', 'Portfolio z kampaniami, logo i filmem reklamowym pokażesz na rozmowie kwalifikacyjnej.'),
             ('Prowadzisz social media lub firmę', 'Twoje grafiki wyglądają amatorsko', 'Nauczysz się kompozycji, typografii i montażu rolek. Teksty reklamowe napiszesz z pomocą AI.'),
             ('Szukasz dofinansowania', 'Zależy Ci, żeby kurs nie obciążył budżetu', 'Urząd pracy może opłacić kurs osobom bezrobotnym, a KFS pracującym. Sekretariat pomoże z dokumentami.')],
        outcomes=['Projektujesz kampanię reklamową do social mediów i druku',
                  'Tworzysz logo i identyfikację wizualną marki',
                  'Piszesz teksty reklamowe i opisy produktów z pomocą AI',
                  'Montujesz rolki i krótki film reklamowy w After Effects'],
        jobs=['Grafik reklamowy', 'Projektant kreatywny', 'Copywriter', 'Grafik w zespole kampanii', 'Asystent art directora', 'Freelancer'],
        tools='Photoshop, Illustrator, InDesign, After Effects, CapCut, ChatGPT'),
]
COURSE_URL = {c['name']: c['slug'] for c in COURSES}

def ab(intro, bullets, outro=''):
    li = ''.join('<li class="flex gap-3"><svg class="mt-0.5 h-5 w-5 shrink-0 text-brand" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m5 12 5 5L20 7"/></svg><span>%s</span></li>' % b for b in bullets)
    return '<p>%s</p><ul class="mt-3 space-y-2">%s</ul>%s' % (intro, li, ('<p class="mt-3">%s</p>' % outro) if outro else '')


FAQ_COURSE = [
    ('Nigdy nie projektowałem(-am). Czy dam radę?', ab('Tak. Większość kursantów zaczyna od zera.', [
        'zaczynamy od podstaw każdego programu, krok po kroku',
        'grupy są małe, więc prowadzący widzi Twoją pracę i pomaga na bieżąco',
        'pierwszy projekt do portfolio robisz już w pierwszych tygodniach',
        'nie musisz mieć własnych licencji na start, doradzimy, co zainstalować'])),
    ('Pracuję. Czy pogodzę kurs z pracą?', ab('Tak, kurs jest układany pod osoby pracujące.', [
        'zajęcia w soboty i niedziele, dwa razy w miesiącu',
        'od końca września do końca czerwca, bez zajęć w tygodniu',
        'projekty robisz we własnym tempie między zjazdami',
        'jeśli opuścisz zjazd, prowadzący podpowie, jak nadrobić materiał'])),
    ('Ile płacę i kiedy? Czy są raty?', ab('Cena jest jedna, a Ty wybierasz sposób płatności.', [
        '11 rat 0% bez odsetek i bez opłat dodatkowych',
        'albo płatność jednorazowa, wtedy płacisz mniej',
        'kurs online kosztuje tyle samo co stacjonarny',
        'faktura na osobę prywatną lub firmę'])),
    ('Czy ktoś może zapłacić za mój kurs?', ab('Tak. Jesteśmy w Rejestrze Instytucji Szkoleniowych WUP (nr 2.12/00188/2021).', [
        'urząd pracy może sfinansować kurs osobom bezrobotnym i poszukującym pracy',
        'KFS pomaga pracującym, a wniosek składa pracodawca',
        'możesz wziąć nieoprocentowaną pożyczkę na kształcenie',
        'sekretariat przygotuje z Tobą dokumenty'],
        '<a href="dofinansowanie.html" class="text-brand hover:underline">Sprawdź, co Ci przysługuje</a>')),
    ('Online czy w Krakowie, co wybrać?', ab('Ten sam kurs w dwóch formach, a Ty wybierasz przy zapisie.', [
        'online na żywo: łączysz się z grupą i prowadzącym z domu',
        'stacjonarnie: pracujesz w pracowni w Krakowie (ul. Kosynierów 15B)',
        'zajęcia w te same weekendy, z tym samym programem',
        'cena jest taka sama w obu formach'])),
    ('Co dostanę po kursie?', ab('Poza wiedzą dostajesz dokumenty i portfolio, które da się pokazać.', [
        'portfolio z projektami z każdego modułu',
        'polsko-angielski dyplom z suplementem',
        'zaświadczenie zgodne z przepisami MEN',
        'status słuchacza honorowany przez ZUS, KRUS i urzędy pracy'])),
    ('Do kiedy mogę się zapisać?', ab('Nabór na kursy roczne trwa do 30 września.', [
        'liczba miejsc w grupach jest ograniczona',
        'sekretariat potwierdza miejsce i prowadzi przez formalności',
        'start zajęć pod koniec września'],
        '<a href="jak-sie-zapisac.html" class="font-medium text-brand hover:underline">Zobacz, jak się zapisać</a>')),
]


def ps_accordion(items, open_first=True, heading=False):
    tag = 'h3' if heading else 'span'
    return ''.join(f'''<details class="group {'border-t-2' if i == 0 else 'border-t'} border-ink px-4 py-6"{' open' if (open_first and i == 0) else ''}>
  <summary class="flex cursor-pointer list-none items-start justify-between gap-4 text-base font-medium leading-6 text-ink [&::-webkit-details-marker]:hidden"><{tag} class="text-base font-medium">{q}</{tag}><img src="assets/figma/icon-a.svg" alt="" width="24" height="24" class="hidden group-open:block"><img src="assets/figma/icon-b.svg" alt="" width="24" height="24" class="group-open:hidden"></summary>
  <div class="mt-4 max-w-[575px] text-base leading-6 text-ink">{a}</div>
</details>''' for i, (q, a) in enumerate(items))


def check_item(text):
    return ('<li class="flex gap-3"><svg class="mt-0.5 h-5 w-5 shrink-0 text-brand" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">'
            '<path stroke-linecap="round" stroke-linejoin="round" d="m5 12 5 5L20 7"/></svg><span>%s</span></li>' % text)


def final_cta(title='Nie wiesz, który kurs wybrać?',
              text='Nabór na kursy roczne trwa do 30 września. Powiedz, co chcesz robić — sekretariat pomoże dobrać kierunek i sprawdzi, z jakiego dofinansowania możesz skorzystać.',
              second=('Zobacz kursy roczne', 'index.html#kursy-roczne')):
    return f'''<section class="container-page py-20">
  <div class="relative overflow-hidden rounded-3xl bg-brand px-6 py-16 text-center text-white sm:px-12">
    <div class="pointer-events-none absolute inset-0" aria-hidden="true">
      <div class="absolute -right-24 -top-24 h-72 w-72 rounded-full bg-brand-dark"></div>
      <div class="absolute -bottom-32 -left-16 h-72 w-72 rounded-full bg-brand-soft/15"></div>
      <svg class="absolute inset-0 h-full w-full opacity-[0.08]"><defs><pattern id="cta-grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0v40" fill="none" stroke="white" stroke-width=".5"/></pattern></defs><rect width="100%" height="100%" fill="url(#cta-grid)"/></svg>
    </div>
    <div class="relative flex flex-col items-center gap-6">
      <span class="inline-flex items-center rounded-full border border-white/40 px-4 py-1.5 text-sm font-medium">Rekrutacja otwarta</span>
      <h2 class="text-4xl font-semibold leading-tight sm:text-5xl">{title}</h2>
      <p class="max-w-[640px] text-lg leading-7">{text}</p>
      <div class="flex flex-wrap items-center justify-center gap-3">
        <a href="kontakt.html" class="btn min-h-12 bg-white px-6 text-base font-semibold text-brand-dark hover:bg-brand-soft">Zadaj pytanie</a>
        <a href="{second[1]}" class="btn min-h-12 border border-white px-6 text-base font-medium text-white hover:bg-white/10">{second[0]}</a>
      </div>
      <p class="text-base">Zadzwoń: <a href="{PHONE_HREF}" class="font-semibold underline underline-offset-4">504 068 626</a> lub <a href="tel:+48124116566" class="font-semibold underline underline-offset-4">12 411 65 66</a> · codziennie 9:00–20:00</p>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- programy kursów rocznych (tematy: publishingschool.pl, plan 2025/26)
# moduł: (tytuł, godziny, wstęp, tematy, efekt do portfolio)
PROGRAMS = {
    'kurs-grafika-3d.html': [
        ('Grafika 3D w Blenderze i Cinema 4D', 50,
         'Najdłuższy moduł kursu. Zaczynasz od prostych brył, a kończysz na modelu samochodu i kompletnym wnętrzu — w Blenderze, najpopularniejszym darmowym programie do grafiki 3D, z przeglądem możliwości Cinema 4D.',
         ['narzędzia i budowa sceny', 'modelowanie obiektów o złożonej strukturze, np. samochodu', 'modelowanie mebli i całych wnętrz', 'oświetlenie sceny', 'animacja zbudowanych obiektów', 'rendering'],
         'animowana wizualizacja wnętrza i model pojazdu'),
        ('Grafika 3D w Mai', 28,
         'Maya to standard w studiach filmowych i gamedevie. Uczysz się jej interfejsu i przenosisz umiejętności z Blendera do programu, którego wymagają pracodawcy.',
         ['interfejs, narzędzia i scena', 'modelowanie elementów architektury i zieleni', 'tworzenie i animacja postaci', 'animacja obiektów, np. samochodu', 'rendering i compositing klipu 3D'],
         'wizualizacja architektury z otoczeniem i animowany klip 3D'),
        ('Modele 3D do gier: ZBrush lub Blender, Unity', 40,
         'Moduł dla osób, które chcą pracować w gamedevie. Rzeźbisz postać zgodnie z anatomią, przygotowujesz ją technicznie do gry i uruchamiasz w silniku Unity.',
         ['rzeźbienie cyfrowe w ZBrushu', 'modele organiczne i nieorganiczne, rośliny', 'postać zgodna z anatomią, ubranie i wyposażenie', 'retopologia, rigging i teksturowanie', 'import modeli do silnika Unity'],
         'postać do gry gotowa do użycia w Unity'),
        ('Scenariusz, storyboard i animatic z AI', 22,
         'Zanim zaczniesz animować, planujesz — tak jak w prawdziwym studiu. Wymyślasz fabułę z pomocą AI, rysujesz storyboard i składasz animatic w Photoshopie i After Effects.',
         ['scenariusz i fabuła z pomocą AI', 'storyboard', 'montaż czołówki, treści i tyłówki', 'udźwiękowienie i korekty', 'prezentacja projektu'],
         'animatic Twojego filmu animowanego'),
        ('Postprodukcja w After Effects', 42,
         'After Effects zamienia rendery w gotowy film. Uczysz się kompozycji, kamery, światła i dźwięku, a na koniec montujesz własny showreel.',
         ['warstwy, klatki kluczowe i timing', 'prekompozycje i maski', 'światło i animacja kamery', 'praca z wideo i dźwiękiem', 'rendering'],
         'showreel — film z Twoimi pracami 3D'),
        ('Projekt 3D i portfolio', 18,
         'Na koniec wybierasz program i temat, a prowadzący pomagają Ci złożyć portfolio, które pokażesz studiu lub klientowi.',
         ['kompozycje statyczne i animowane w wybranym programie 3D', 'konsultacje i korekty portfolio', 'recenzowana prezentacja projektów'],
         'kompletne portfolio grafika 3D'),
    ],
    'kurs-grafika-dtp.html': [
        ('Projektowanie druków', 28,
         'Zanim otworzysz program, uczysz się, jak projektować publikacje: dobór fontów, układ strony i struktura książki. To wiedza, która odróżnia grafika od operatora programu.',
         ['typografia i dobór fontów', 'układy graficzne i wyróżnienia', 'struktura książki, także niekonwencjonalnej', 'opakowania, plakaty, ulotki, wizytówki i outdoor', 'redakcja techniczna, skład i korekta'],
         'makiety publikacji do dalszego składu'),
        ('DTP: Photoshop, Illustrator i InDesign', 140,
         'Serce kursu — 140 godzin przy komputerze w trzech programach Adobe, których wymaga każda agencja i drukarnia. Każde ćwiczenie to realny druk: od naklejki po katalog w twardej okładce.',
         ['Photoshop: retusz, kolaż, ulotka, etykieta, aplikacja na T-shirt, pudełko do druku cyfrowego i offsetowego',
          'Illustrator: logotypy, ikony, kompozycje liternicze, baner, opakowanie do druku fleksograficznego, wykrojnik',
          'InDesign: plakat, kolorowy katalog, okładka miękka i twarda, dokumenty wielostronicowe',
          'kontrola plików pod wymagania drukarni (preflight)', 'próbna praca graficzna dla klienta'],
         'identyfikacja wizualna, opakowanie i katalog gotowe do druku'),
        ('Drukowanie i wykańczanie druków', 16,
         'Poznajesz techniki druku, więc wiesz, jak przygotować plik pod offset, druk cyfrowy czy sitodruk — i rozmawiasz z drukarnią jak fachowiec.',
         ['rastry, CMYK i RGB', 'offset, druk cyfrowy, sitodruk, fleksografia, rotograwiura', 'hot-stamping, termotransfer, druk UV, solwent i lateks', 'znakowanie gadżetów', 'wykończenie introligatorskie (finishing)'],
         'specyfikacja techniczna druku do Twojego projektu'),
        ('Dobór materiałów do druku', 11,
         'Ten sam projekt wygląda zupełnie inaczej na innym papierze. Uczysz się dobierać podłoża, farby i uszlachetnienia do projektu i budżetu.',
         ['papiery i podłoża niepapierowe', 'farby i tonery', 'materiały introligatorskie', 'uszlachetnienia i zabezpieczenia opakowań przed podróbkami'],
         'dobór materiałów do projektu dyplomowego'),
        ('Autorski katalog i portfolio', 5,
         'Projekt dyplomowy: składasz własny katalog, a prowadzący konsultują typografię i redakcję. Najlepsze prace trafiają do galerii szkoły.',
         ['konsultacje typograficzne i redakcyjne', 'korekty indywidualne', 'prezentacja projektu'],
         'autorski katalog i portfolio grafika DTP'),
    ],
    'kurs-web-designer.html': [
        ('UI i UX z wykorzystaniem AI', 38,
         'Uczysz się myśleć jak projektant produktu: kim jest użytkownik, czego szuka i jak ułatwić mu drogę do celu. AI pomaga szybciej analizować i generować pomysły.',
         ['responsive i adaptive web design, mobile first', 'breakpointy i projektowanie pod dotyk', 'architektura informacji i wireframe', 'persona i mapa doświadczeń użytkownika', 'badania UX jakościowe i ilościowe'],
         'persona, mapa doświadczeń i makiety serwisu'),
        ('Figma — interfejsy z pomocą AI', 33,
         'Figma to dziś podstawowe narzędzie web designera. Budujesz design system, komponenty i responsywne layouty, a na koniec projektujesz własną stronę.',
         ['narzędzia, kształty, maski i pluginy', 'design system: kolory, gradienty, style tekstu', 'komponenty i biblioteki', 'responsywne layouty', 'wstęp do prototypowania'],
         'projekt responsywnej strony internetowej w Figmie'),
        ('WordPress z elementami SEO', 37,
         'Na WordPressie działa większość stron w internecie. Stawiasz od zera kilka serwisów i uczysz się, jak sprawić, żeby Google je znalazł.',
         ['hosting, domena, motywy i wtyczki', 'edytory Gutenberg i Elementor, szablony blokowe', 'menu, slidery, formularz kontaktowy, mapa Google, blog', 'animacje i elementy responsywne', 'SEO z wtyczką Yoast i podstawy WooCommerce'],
         'strony pizzerii, agencji interaktywnej i studia foto'),
        ('Grafika i wideo na strony: Photoshop, Illustrator, After Effects', 38,
         'Strona potrzebuje grafik. Przygotowujesz banery, ikony, logotypy i krótkie animacje — tak, żeby nie zależeć od grafika.',
         ['Photoshop: retusz, banery w RGB, slider, animacja', 'Illustrator: ikony, logotypy, wykresy', 'After Effects: krótki film, kamera, światło, dźwięk'],
         'zestaw banerów, ikon i animacja na stronę'),
        ('Webflow — podstawy z AI', 20,
         'Webflow pozwala budować profesjonalne strony bez pisania kodu. Poznajesz jego mocne i słabe strony, żeby wiedzieć, kiedy go wybrać.',
         ['możliwości i ograniczenia no-code', 'szablony i edytor „przeciągnij i upuść”', 'elementy statyczne i interaktywne', 'SEO w Webflow'],
         'strona zbudowana w Webflow'),
        ('HTML5 i CSS3', 32,
         'Znając kod, lepiej projektujesz i dogadujesz się z programistami. Kodujesz layout od zera, łącznie z responsywnością i animacjami.',
         ['struktura dokumentu, linki, tabele i formularze', 'selektory, box model i pozycjonowanie', 'elementy blokowe i liniowe', 'media queries (RWD)', 'animacje i transformacje CSS'],
         'zakodowana responsywna strona'),
        ('Portfolio web designera', 2,
         'Prowadzący pomagają wybrać najlepsze projekty i przygotować prezentację, z którą pójdziesz na rozmowę.',
         ['konsultacje projektów', 'prezentacja portfolio'],
         'portfolio web designera'),
    ],
    'kurs-graphic-designer.html': [
        ('Grafika do internetu i narzędzia AI', 44,
         'Projektujesz wszystko, czego marka potrzebuje w sieci — od posta na Facebooka po e-katalog — i uczysz się pracować szybciej z generatorami AI.',
         ['Photoshop: animowane reklamy, posty, banery', 'Illustrator: ikony, logo, infografiki, identyfikacja do internetu', 'InDesign: e-wizytówki, interaktywne plakaty, e-katalogi', 'AI: ChatGPT, DALL-E, GetImg, OpenArt, DreamStudio', 'montaż rolek w CapCut lub Edits'],
         'pakiet reklamowy do social mediów'),
        ('Grafika do druku', 86,
         'Największy moduł kursu. Projektujesz materiały, które naprawdę trafiają do drukarni: od naklejki po katalog z okładką.',
         ['Photoshop: kolaż, identyfikacja do druku, T-shirt, banery outdoorowe, naklejki, etykiety', 'Illustrator: logo, wizytówki, metki, wykrojniki', 'InDesign: plakaty, dokumenty wielostronicowe, katalogi z okładką', 'próbna praca dla klienta'],
         'identyfikacja wizualna i katalog gotowe do druku'),
        ('Trening kreatywności w reklamie', 11,
         'Dobry grafik reklamowy ma pomysły na zawołanie. Ćwiczysz myślenie kombinacyjne i lateralne, żeby nie utknąć przed pustą kartką.',
         ['analiza własnych predyspozycji', 'myślenie twórcze i kombinacyjne', 'rozwiązywanie problemów kreatywnych'],
         'koncepcje kampanii reklamowych'),
        ('Warsztaty copywritingu z AI', 15,
         'Reklama to obraz i słowo. Uczysz się pisać teksty, które sprzedają — i używać AI, żeby robić to szybciej.',
         ['oferty sprzedażowe i opisy produktów', 'posty, treści na bloga i stronę', 'kampanie e-mailowe', 'slogany i teksty sponsorowane'],
         'teksty do Twojej kampanii'),
        ('Krótki film reklamowy w After Effects', 23,
         'Wideo to dziś najskuteczniejsza forma reklamy. Tworzysz animowany spot od importu materiałów po dźwięk.',
         ['warstwy, klatki kluczowe i timing', 'maski, światło i animacja kamery', 'praca z wideo', 'udźwiękowienie i rendering'],
         'animowany spot reklamowy'),
        ('Typografia, kompozycja, kolor i druk', 17,
         'Fundamenty, które sprawiają, że projekt wygląda profesjonalnie i dobrze się drukuje.',
         ['fonty i typografia', 'CMYK, RGB i rastry', 'techniki druku', 'papiery, podłoża, farby i uszlachetnienia'],
         'projekty poprawione pod kątem typografii i druku'),
        ('Portfolio — pakiet reklamowy', 4,
         'Składasz kampanię reklamową do portfolio, a prowadzący konsultują ją indywidualnie.',
         ['konsultacje indywidualne', 'prezentacja projektów'],
         'kompletny pakiet reklamowy w portfolio'),
    ],
}

# teksty SEO (akapit „O kursie”) — frazy: kurs + narzędzie + Kraków/online
SEO_TEXT = {
    'kurs-grafika-3d.html': [
        'Kurs grafiki 3D w Publishing School to 200 godzin praktycznych zajęć z modelowania, animacji, renderingu i postprodukcji. Uczysz się w <strong>Blenderze, Cinema 4D, Mai, ZBrushu, Unity i After Effects</strong> — programach, z których korzystają studia gier, agencje reklamowe i firmy robiące wizualizacje architektury.',
        'Zajęcia odbywają się w soboty i niedziele, dwa razy w miesiącu: <strong>stacjonarnie w Krakowie</strong> albo <strong>online na żywo</strong> z grupą. Kurs zaczynasz od podstaw, a kończysz z portfolio grafika 3D, showreelem i polsko-angielskim dyplomem.',
    ],
    'kurs-grafika-dtp.html': [
        'Kurs grafiki DTP to 200 godzin nauki projektowania i przygotowania publikacji do druku. Pracujesz w <strong>InDesignie, Photoshopie i Illustratorze</strong>, a do tego poznajesz techniki druku, papiery i uszlachetnienia — wiedzę, której wymagają agencje, wydawnictwa i drukarnie.',
        'Uczysz się <strong>w Krakowie lub online</strong>, co drugi weekend. Składasz książki, katalogi, opakowania i plakaty, a kurs kończysz autorskim katalogiem, portfolio grafika DTP i dyplomem polsko-angielskim.',
    ],
    'kurs-web-designer.html': [
        'Kurs web designu i UI/UX to 200 godzin nauki projektowania i budowania stron internetowych. Projektujesz w <strong>Figmie</strong>, stawiasz strony w <strong>WordPressie i Webflow</strong>, kodujesz w <strong>HTML i CSS</strong>, a do tego przygotowujesz grafiki i animacje w programach Adobe.',
        'Zajęcia są <strong>w Krakowie lub online na żywo</strong>, w soboty i niedziele. Przechodzisz cały proces: od badań z użytkownikami i makiet, przez design system i SEO, po gotową stronę w sieci. Kończysz z portfolio web designera i dyplomem polsko-angielskim.',
    ],
    'kurs-graphic-designer.html': [
        'Kurs grafiki reklamowej to 200 godzin nauki projektowania reklam do internetu i druku. Pracujesz w <strong>Photoshopie, Illustratorze, InDesignie i After Effects</strong>, montujesz rolki w CapCut, a teksty reklamowe piszesz z pomocą <strong>narzędzi AI</strong>.',
        'Uczysz się <strong>w Krakowie lub online</strong>, co drugi weekend. Projektujesz logo, identyfikacje, posty, plakaty i spoty wideo, a kurs kończysz kompletnym pakietem reklamowym w portfolio i dyplomem polsko-angielskim.',
    ],
}


def program_body(intro, topics, effect):
    items = ''.join('<li class="flex gap-3"><span class="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true"></span><span>%s</span></li>' % t for t in topics)
    return ('<p>%s</p><p class="mt-4 font-medium">Czego się uczysz</p><ul class="mt-2 space-y-1.5">%s</ul>'
            '<p class="mt-4 rounded-2xl bg-brand-soft px-4 py-3 text-olive"><strong class="font-semibold">Do portfolio:</strong> %s</p>'
            % (intro, items, effect))


def course_schema(c, hours):
    import json
    data = [{
        '@context': 'https://schema.org', '@type': 'Course', 'name': 'Kurs roczny ' + c['name'],
        'description': c['lead'], 'inLanguage': 'pl',
        'provider': {'@type': 'EducationalOrganization', 'name': 'Publishing School', 'sameAs': 'https://publishingschool.pl',
                     'address': {'@type': 'PostalAddress', 'streetAddress': 'ul. Kosynierów 15B', 'postalCode': '31-572', 'addressLocality': 'Kraków', 'addressCountry': 'PL'}},
        'educationalCredentialAwarded': 'Dyplom polsko-angielski z suplementem, zaświadczenie zgodne z przepisami MEN',
        'syllabusSections': [{'@type': 'Syllabus', 'name': t, 'description': i, 'timeRequired': 'PT%dH' % h} for t, h, i, _, _ in PROGRAMS[c['slug']]],
        'hasCourseInstance': [{'@type': 'CourseInstance', 'courseMode': m, 'courseWorkload': 'PT%dH' % hours} for m in ('onsite', 'online')],
    }, {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', a)).strip()}} for q, a in FAQ_COURSE],
    }]
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)


def course_page(c):
    program = PROGRAMS[c['slug']]
    hours = sum(m[1] for m in program)
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kursy roczne', 'index.html#kursy-roczne'), (c['name'], '')])
    hero_img = (photo(c['hero'][0], c['hero'][1], c['hero'][2], c['hero'][3], 'h-[520px] w-auto max-w-full', lazy=False)
                if c['hero'] else media(c['hero_label'], 'aspect-[4/5] h-[520px]'))
    body += f'''<section class="container-page pb-16 pt-8">
  <div class="grid min-h-[520px] grid-cols-2 items-center gap-6">
    <div class="max-w-[560px]">
      <div class="flex gap-2">{COMMON_BADGES}</div>
      <h1 class="mt-4 text-5xl font-semibold leading-[3rem] text-ink">{c['h1']}</h1>
      <p class="mt-4 text-base leading-6 text-ink">{c['lead']}</p>
      <div class="mt-5 flex gap-2">{btn('Zarezerwuj miejsce', '#zapisy', 'brand')}{btn('Zobacz program', '#program', 'brand-outline')}</div>
      <p class="mt-3 text-sm text-neutral-600">11 rat 0% · dofinansowanie z urzędu pracy lub KFS · dyplom PL/EN</p>
    </div>
    <div class="flex justify-center">{hero_img}</div>
  </div>
</section>'''
    stats = ''.join(f'<div class="flex flex-1 flex-col items-center gap-2 p-4"><dt class="order-2 text-base leading-6">{b}</dt><dd class="order-1 text-2xl font-semibold leading-8">{a}</dd></div>'
                    for a, b in [(f'{hours} godzin', 'samej praktyki'), ('Wrzesień – czerwiec', 'soboty i niedziele, 2× w miesiącu'),
                                 ('11 rat 0%', 'ta sama cena online i w Krakowie'), ('Dyplom PL/EN', 'i zaświadczenie zgodne z MEN')])
    body += f'<section aria-label="Najważniejsze informacje" class="bg-alt py-9"><dl class="container-page flex text-center text-ink">{stats}</dl></section>'
    body += anchor_nav([('Dla kogo', 'dla-kogo'), ('Program', 'program'), ('Po kursie', 'po-kursie'), ('Cena', 'cena'), ('Zapisy', 'zapisy'), ('FAQ', 'faq')])

    DLA_ICON = {'Zaczynasz od zera': 'sprout', 'Zmieniasz zawód': 'route', 'Szukasz dofinansowania': 'banknote', 'Prowadzisz social media lub firmę': 'megaphone',
                'Pracujesz w marketingu, e-commerce lub grafice': 'briefcase', 'Pracujesz w kreatywnej branży': 'briefcase', 'Składasz materiały w pracy': 'printer'}
    dla = ''.join(f'<article class="ps-card"><p class="text-sm font-semibold uppercase tracking-wide text-brand">{g} <span class="font-normal normal-case tracking-normal text-neutral-500">(icon: {DLA_ICON[g]})</span></p><h3 class="text-xl font-medium leading-7">{a}</h3><p class="text-base leading-6">{b}</p></article>' for g, a, b in c['dla'])
    body += f'''<section class="container-page scroll-mt-36 py-20" id="dla-kogo">
  {ps_head('Dla kogo', 'Ten kurs jest dla Ciebie, jeśli', 'Nie musisz umieć nic z programów graficznych. Znajdź swoją sytuację poniżej.')}
  <div class="mt-10 grid grid-cols-4 gap-6">{dla}</div>
  <p class="mt-8 text-center text-base leading-6 text-ink">Nie wiesz, czy to kurs dla Ciebie? <a href="kontakt.html" class="font-medium text-brand hover:underline">Napisz do sekretariatu</a> lub zadzwoń: <a href="{PHONE_HREF}" class="font-medium hover:underline">504 068 626</a>.</p>
</section>'''

    body += f'''<section class="container-page py-20">
  <div class="flex items-center gap-12">
    <div class="flex flex-1 justify-center">{photo('programy-adobe.webp', 'Pasek aplikacji na MacBooku: Illustrator, Photoshop, InDesign, After Effects', 1020, 960, 'max-w-[508px]')}</div>
    <div class="flex flex-1 flex-col gap-6">
      {ps_head('Efekty', 'Co potrafisz po kursie', 'Każdy moduł kończy się projektem, który trafia do Twojego portfolio.', center=False)}
      <ul class="space-y-4 text-base leading-6 text-ink">{''.join(check_item(o) for o in c['outcomes'])}</ul>
      <p class="text-sm text-neutral-600">Programy: {c['tools']}</p>
    </div>
  </div>
</section>'''

    prog = [(f'{t} <span class="ml-2 font-normal text-neutral-600">· {h} godz.</span>', program_body(i, tp, ef)) for t, h, i, tp, ef in program]
    seo = ''.join(f'<p>{p}</p>' for p in SEO_TEXT[c['slug']])
    body += f'''<section class="container-page scroll-mt-36 py-20" id="program">
  <div class="flex items-start gap-12">
    <div class="sticky top-40 w-[360px] shrink-0">
      {ps_head('Program', f'Program kursu {c["name"]}', center=False)}
      <p class="mt-4 text-base leading-6 text-ink">Uczysz się w soboty i niedziele, dwa razy w miesiącu. Każdy moduł kończy się projektem do portfolio.</p>
      <dl class="mt-6 grid grid-cols-2 gap-4 text-ink">
        <div class="rounded-2xl bg-alt p-4"><dd class="text-2xl font-semibold">{hours} godz.</dd><dt class="text-sm text-neutral-600">praktyki</dt></div>
        <div class="rounded-2xl bg-alt p-4"><dd class="text-2xl font-semibold">{len(program)} {'moduły' if len(program) in (2, 3, 4) else 'modułów'}</dd><dt class="text-sm text-neutral-600">z projektem</dt></div>
      </dl>
      <div class="mt-6">{btn('Zarezerwuj miejsce', '#zapisy', 'brand')}</div>
    </div>
    <div class="flex-1">
      {ps_accordion(prog, heading=True)}
      <div class="mt-10 space-y-4 border-t border-neutral-300 pt-8 text-base leading-7 text-neutral-600">{seo}</div>
    </div>
  </div>
</section>'''

    jobs = ''.join(check_item(j) for j in c['jobs'])
    body += f'''<section class="container-page scroll-mt-36 py-20" id="po-kursie">
  <div class="flex items-center gap-12">
    <div class="flex flex-1 flex-col gap-6">
      {ps_head('Po kursie', 'Gdzie możesz pracować', 'Absolwenci pracują w agencjach, firmach i na własny rachunek. Na koniec kursu masz portfolio, które pokażesz na rozmowie.', center=False)}
      <ul class="grid grid-cols-2 gap-x-6 gap-y-4 text-base leading-6 text-ink">{jobs}</ul>
      <div><a href="prace-absolwentow.html" class="btn btn-ghost">Zobacz prace absolwentów{CHEV_GRAY}</a></div>
    </div>
    <div class="flex flex-1 justify-center">{photo('programy-adobe.webp', 'Pasek aplikacji na MacBooku: Illustrator, Photoshop, InDesign, After Effects', 1020, 960, 'max-w-[508px]')}</div>
  </div>
</section>'''

    included = ['Zajęcia na żywo z praktykami', 'Konsultacje portfolio', 'Dyplom polsko-angielski z suplementem',
                'Zaświadczenie zgodne z przepisami MEN', 'Status słuchacza (ZUS, KRUS, UP)', 'Pracownia w Krakowie lub zajęcia online']
    body += f'''<section class="container-page scroll-mt-36 py-20" id="cena" data-price>
  {ps_head('Cena', 'Prosta cena', 'Kurs online kosztuje tyle samo co stacjonarny. Za kurs może zapłacić urząd pracy, KFS albo Twój pracodawca — sekretariat pomoże przygotować dokumenty.')}
  <div class="mt-8 flex items-center justify-center gap-3 text-base">
    <span data-price-label="raty">Raty 0%</span>
    <button type="button" role="switch" aria-checked="false" aria-label="Płatność jednorazowa za cały rok" class="group relative inline-flex h-7 w-12 items-center rounded-full bg-neutral-300 transition-colors after:absolute after:-inset-2.5 aria-checked:bg-brand focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand">
      <span class="ml-0.5 h-6 w-6 rounded-full bg-white shadow transition-transform group-aria-checked:translate-x-5"></span>
    </button>
    <span data-price-label="raz">Jednorazowo za rok</span>
    <span data-price-view="raz" class="rounded-full bg-brand-soft px-3 py-1 text-sm font-medium text-brand">Oszczędzasz [x]%</span>
  </div>
  <div class="mt-8 grid grid-cols-2 gap-6">
    <div class="ps-card">
      <p data-price-view="raty" class="text-base text-neutral-600">Płatność w ratach</p>
      <p data-price-view="raz" class="text-base text-neutral-600">Jedna płatność za cały rok</p>
      <p data-price-view="raty"><span class="text-5xl font-semibold text-ink">[kwota]</span> <span class="text-base text-neutral-600">zł / mies. · 11 rat 0%</span></p>
      <p data-price-view="raz"><span class="text-5xl font-semibold text-ink">[kwota]</span> <span class="text-base text-neutral-600">zł za cały kurs</span></p>
      <p data-price-view="raty" class="text-base leading-6">Bez odsetek i bez opłat dodatkowych. Cena kursu jest ta sama online i w Krakowie.</p>
      <p data-price-view="raz" class="text-base leading-6">Płacisz raz przed startem zajęć i masz cały rok bez rat. Faktura na osobę prywatną lub firmę — przy działalności kurs wliczasz w koszty.</p>
      <div class="mt-auto flex gap-2 pt-2">{btn('Zarezerwuj miejsce', '#zapisy', 'brand')}{btn('Sprawdź dofinansowanie', 'dofinansowanie.html', 'brand-outline')}</div>
    </div>
    <div class="ps-card">
      <p class="text-base font-medium text-ink">W cenie kursu</p>
      <ul class="grid grid-cols-2 gap-x-6 gap-y-4 text-base leading-6 text-ink">{''.join(check_item(i) for i in included)}</ul>
    </div>
  </div>
</section>'''

    steps = [('1', 'Formularz', 'Pobierasz formularz zgłoszeniowy i wysyłasz go na krystyna@publishingschool.pl.'),
             ('2', 'Dokumenty', 'Dołączasz 2 zdjęcia paszportowe. Z dokumentami do dofinansowania pomoże sekretariat.'),
             ('3', 'Rozmowa wstępna', 'Krótka rozmowa online albo w szkole — dopasujemy formę zajęć.'),
             ('4', 'Pierwsze zajęcia', 'Podpisujesz umowę, wybierasz raty i zaczynasz pod koniec września.')]
    step_html = ''.join(f'<li class="ps-card"><span class="flex h-10 w-10 items-center justify-center rounded-full bg-brand text-base font-semibold text-white">{n}</span><h3 class="text-xl font-medium leading-7">{a}</h3><p class="text-base leading-6">{b}</p></li>' for n, a, b in steps)
    body += f'''<section class="container-page scroll-mt-36 py-20" id="zapisy">
  {ps_head('Zapisy', 'Jak się zapisać', 'Cztery kroki. Sekretariat przeprowadzi Cię przez każdy z nich.')}
  <ol class="mt-10 grid grid-cols-4 gap-6">{step_html}</ol>
  <div class="mt-8 text-center">{btn('Pobierz formularz zgłoszeniowy', 'jak-sie-zapisac.html', 'brand')}</div>
</section>'''

    body += f'''<section class="container-page scroll-mt-36 py-20" id="faq">
  <div class="flex items-start gap-6">
    <div class="w-[520px] shrink-0">
      {ps_head('FAQ', 'Najczęściej zadawane pytania', f'Nie ma tu Twojego pytania? Zadzwoń {PHONE} (codziennie 9:00–20:00) albo napisz. Odpowiadamy szybko.', center=False)}
      <div class="mt-6"><a href="kontakt.html" class="btn btn-ghost">Zadaj pytanie</a></div>
    </div>
    <div class="flex-1">{ps_accordion(FAQ_COURSE, open_first=False)}</div>
  </div>
</section>'''
    body += final_cta(f'Zacznij kurs {c["name"]} pod koniec września',
                      'Nabór na kursy roczne trwa do 30 września. Zadzwoń albo napisz — sekretariat odpowie na pytania i sprawdzi, z jakiego dofinansowania możesz skorzystać.',
                      ('Porównaj kierunki', 'index.html#kursy-roczne'))
    page(c['slug'], f'Kurs {c["name"]} — Kraków i online', body,
         f'Kurs {c["name"]} od podstaw: {hours} godzin praktyki ({c["tools"]}). Zajęcia w Krakowie lub online, 11 rat 0%, dofinansowanie z urzędu pracy, dyplom PL/EN.',
         head_extra=course_schema(c, hours))


def kursy_roczne():
    for c in COURSES:
        course_page(c)


SHORT_COURSES = [
    ('Blender 3D od podstaw', 'Modelowanie, teksturowanie i render — kończysz z gotową sceną do portfolio.', '17, 18 i 24.10.2026 · online · 870 zł', '3d soon', 'kurs-krotki.html'),
    ('InDesign dla początkujących', 'Skład publikacji, style i eksport do PDF — przygotujesz pliki gotowe do druku.', '17–28.10.2026 · online · 760 zł', 'adobe soon', 'kurs-krotki.html'),
    ('Kurs UX — User Experience', 'Heurystyki, badania i wireframing — zaprojektujesz lepszą ścieżkę użytkownika.', 'Zapytaj o termin · 530 zł', 'web', 'kurs-krotki.html'),
    ('Photoshop dla początkujących', 'Retusz, maski i warstwy — przygotujesz grafiki do sklepu i social mediów.', '02–05.10.2026 · online', 'adobe soon', 'kurs-krotki.html'),
    ('Canva: grafiki i rolki', 'Grafiki, rolki i animacje do social mediów — bez znajomości programów Adobe.', '23–29.09.2026 · online', 'social soon', 'kurs-krotki.html'),
    ('Typografia w pracy grafika', 'Dobór krojów, hierarchia i skład — Twoje projekty staną się czytelniejsze.', '24–30.09.2026 · online', 'druk soon', 'kurs-krotki.html'),
]


def ps_faq(items, lead):
    return f'''<section class="container-page scroll-mt-36 py-20" id="faq">
  <div class="flex items-start gap-6">
    <div class="w-[520px] shrink-0">
      {ps_head('FAQ', 'Najczęściej zadawane pytania', lead, center=False)}
      <div class="mt-6"><a href="kontakt.html" class="btn btn-ghost">Zadaj pytanie</a></div>
    </div>
    <div class="flex-1">{ps_accordion(items, open_first=False)}</div>
  </div>
</section>'''


def price_block(included, lead, monthly=True):
    return f'''<section class="container-page scroll-mt-36 py-20" id="cena" data-price>
  {ps_head('Cena', 'Prosta cena', lead)}
  <div class="mt-8 flex items-center justify-center gap-3 text-base">
    <span data-price-label="raty">Raty 0%</span>
    <button type="button" role="switch" aria-checked="false" aria-label="Płatność jednorazowa" class="group relative inline-flex h-7 w-12 items-center rounded-full bg-neutral-300 transition-colors after:absolute after:-inset-2.5 aria-checked:bg-brand focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand">
      <span class="ml-0.5 h-6 w-6 rounded-full bg-white shadow transition-transform group-aria-checked:translate-x-5"></span>
    </button>
    <span data-price-label="raz">Jednorazowo</span>
    <span data-price-view="raz" class="rounded-full bg-brand-soft px-3 py-1 text-sm font-medium text-brand">Oszczędzasz [x]%</span>
  </div>
  <div class="mt-8 grid grid-cols-2 gap-6">
    <div class="ps-card">
      <p data-price-view="raty" class="text-base text-neutral-600">Płatność w ratach</p>
      <p data-price-view="raz" class="text-base text-neutral-600">Płatność jednorazowa</p>
      <p data-price-view="raty"><span class="text-5xl font-semibold text-ink">[kwota]</span> <span class="text-base text-neutral-600">zł / mies. · 11 rat 0%</span></p>
      <p data-price-view="raz"><span class="text-5xl font-semibold text-ink">[kwota]</span> <span class="text-base text-neutral-600">zł za cały kurs</span></p>
      <p data-price-view="raty" class="text-base leading-6">Bez odsetek i bez opłat dodatkowych.</p>
      <p data-price-view="raz" class="text-base leading-6">Płacisz raz przed startem. Faktura na osobę prywatną lub firmę.</p>
      <div class="mt-auto flex gap-2 pt-2">{btn('Zarezerwuj miejsce', 'jak-sie-zapisac.html', 'brand')}{btn('Sprawdź dofinansowanie', 'dofinansowanie.html', 'brand-outline')}</div>
    </div>
    <div class="ps-card">
      <p class="text-base font-medium text-ink">W cenie kursu</p>
      <ul class="grid grid-cols-2 gap-x-6 gap-y-4 text-base leading-6 text-ink">{''.join(check_item(i) for i in included)}</ul>
    </div>
  </div>
</section>'''


def hero_banner():
    return ('<section class="mx-auto w-full max-w-7xl px-6 min-[1360px]:px-0">'
            + photo('o-szkole-laptop.webp', 'Kursant pracuje na laptopie przy biurku', 1016, 884, 'h-[480px]')
            + '</section>')


def center_hero(title, lead, extra=''):
    return f'''<section class="container-page flex min-h-[calc(100svh-8.5rem)] flex-col items-center justify-center py-20">
  <div class="mx-auto flex w-[630px] max-w-full flex-col items-center gap-4 py-6 text-center text-ink">
    <h1 class="text-5xl font-semibold leading-[3rem]">{title}</h1>
    <p class="text-base leading-6">{lead}</p>
    {extra}
  </div>
</section>'''


def kursy_krotkie():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Kursy', 'index.html#kursy-roczne'), ('Kursy krótkie', '')])
    body += center_hero('Kursy krótkie', 'Jeden temat, kilka dni nauki, certyfikat na koniec. Wybierz kategorię i zacznij w najbliższy weekend.')
    body += hero_banner()
    opts = [('Bon szkoleniowy', 'Urząd pracy może opłacić kurs osobom bezrobotnym i poszukującym pracy.'),
            ('KFS', 'Krajowy Fundusz Szkoleniowy dla pracujących — wniosek składa pracodawca.'),
            ('Pracodawca', 'Firma opłaca kurs pracownika. Wystawiamy fakturę i komplet dokumentów.'),
            ('Pożyczka szkoleniowa', 'Nieoprocentowana pożyczka na kształcenie z możliwością częściowego umorzenia.')]
    cards = ''.join(f'<article class="ps-card items-center text-center"><img src="assets/figma/icon-printer.svg" alt="" class="h-16"><h3 class="text-xl font-medium leading-7">{a}</h3><p class="text-base leading-6">{b}</p></article>' for a, b in opts)
    body += f'''<section class="container-page py-20">
  {ps_head('Dofinansowania', 'Kurs może opłacić pracodawca albo urząd pracy', 'Dokumenty do wniosku przygotujemy w ciągu 24 h.')}
  <div class="mt-10 grid grid-cols-4 gap-6">{cards}</div>
  <p class="mt-6 text-center text-xs text-neutral-600">Informacje ogólne. O przyznaniu dofinansowania decyduje urząd pracy.</p>
</section>'''
    chips = [('all', 'Wszystkie'), ('soon', 'Najbliższe'), ('3d', 'Grafika 3D'), ('adobe', 'Grafika komputerowa'), ('web', 'Web design'), ('druk', 'Druk i DTP')]
    chip_html = ''.join('<button type="button" role="tab" data-tab="%s" aria-selected="%s" class="seg">%s</button>' % (k, 'true' if k == 'all' else 'false', l) for k, l in chips)
    cards = ''.join(ps_card(t, f'{d} <span class="mt-2 block text-sm text-neutral-600">{m}</span>', 'Zobacz program', h, 'icon-printer', extra='" data-cat="' + c) for t, d, m, c, h in SHORT_COURSES)
    body += f'''<section class="container-page py-20">
  {ps_head('Katalog', 'Wybierz rodzaj kursu', '6 kategorii, ponad 30 tematów.')}
  <div role="tablist" aria-label="Kategorie kursów" data-tabs data-tabs-mode="filter" data-tabs-target="#course-grid" class="mx-auto mt-6 flex w-fit max-w-full flex-wrap overflow-hidden rounded-full border border-brand">{chip_html}</div>
  <div class="mt-6 border-t border-neutral-400"></div>
  <div id="course-grid" class="mt-8 grid grid-cols-3 gap-6">{cards}</div>
  <div class="mt-8 text-center">{btn('Pokaż kolejne kursy (8)', '#', 'brand-outline')}</div>
</section>'''
    school_stats = [('Zjazdy', 'co 2 weekendy'), ('Wyróżnienie', 'Orły Edukacji'), ('Certyfikat', 'z hologramem')]
    sdl = ''.join(f'<div class="flex flex-1 flex-col justify-center gap-2 rounded-2xl bg-alt p-4"><dt class="order-2 text-base leading-6">{b}</dt><dd class="order-1 text-2xl font-semibold leading-8">{a}</dd></div>' for a, b in school_stats)
    body += f'''<section class="container-page py-20">
  <div class="flex items-center gap-12">
    <div class="flex flex-1 justify-center"><img src="assets/img/o-szkole-laptop.webp" width="1016" height="884" loading="lazy" alt="Kursant pracuje na laptopie przy biurku z linijką i notatkami" class="w-full max-w-[508px] rounded-3xl"></div>
    <div class="flex flex-1 flex-col gap-8">
      {ps_head('O szkole', 'Uczysz się u praktyków, w małych grupach', 'Od 1998 roku szkolimy grafików w Krakowie. Zajęcia prowadzą projektanci, którzy pracują w zawodzie, a każdy kurs kończy się pracą, którą pokażesz w portfolio albo wykorzystasz w firmie.', center=False)}
      <div><a href="o-szkole.html" class="btn btn-brand-outline">Poznaj szkołę</a></div>
      <dl class="flex gap-4 text-ink">{sdl}</dl>
    </div>
  </div>
</section>'''
    body += final_cta('Nie mamy teraz potwierdzonego terminu', 'Sprawdź możliwe dofinansowania. Sekretariat pomoże przygotować dokumenty.',
                      second=('Zobacz kursy roczne', 'index.html#kursy-roczne'))
    page('kursy-krotkie.html', 'Kursy krótkie', body, 'Katalog kursów krótkich Publishing School: grafika, 3D, UX, social media i druk.')


def kurs_krotki():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Lista kursów krótkich', 'kursy-krotkie.html'), ('Blender 3D od podstaw', '')])
    meta = ''.join(f'<span class="rounded-full bg-alt px-3 py-1 text-sm text-ink">{m}</span>' for m in ['17, 18 i 24.10.2026', 'Online · Jitsi', '9:00–13:30'])
    body += f'''<section class="container-page pb-16 pt-8">
  <div class="grid min-h-[520px] grid-cols-2 items-center gap-6">
    <div class="max-w-[560px]">
      <div class="flex gap-2"><span class="rounded-full bg-info px-2 py-1 text-sm text-white">Grafika 3D</span><span class="rounded-full border border-brand-dark px-2 py-1 text-sm text-brand-dark">Kurs krótki</span></div>
      <h1 class="mt-4 text-5xl font-semibold leading-[3rem] text-ink">Blender 3D od podstaw</h1>
      <p class="mt-4 text-base leading-6 text-ink">W trzy dni przejdziesz od pierwszego uruchomienia Blendera do gotowego renderu. Wymodelujesz, oteksturujesz i oświetlisz własną scenę, którą dodasz do portfolio.</p>
      <div class="mt-4 flex flex-wrap gap-2">{meta}</div>
      <div class="mt-5 flex gap-2">{btn('Zapisz się na kurs', '#cena', 'brand')}</div>
    </div>
    <div class="flex justify-center">{photo('web-designer-kod.webp', 'Dwie osoby pracują przy komputerze nad projektem 3D', 996, 1164, 'h-[520px] w-auto max-w-full', lazy=False)}</div>
  </div>
</section>'''
    stats = ''.join(f'<div class="flex flex-1 flex-col items-center gap-2 p-4"><dt class="order-2 text-base leading-6">{b}</dt><dd class="order-1 text-2xl font-semibold leading-8">{a}</dd></div>'
                    for a, b in [('28 lat', 'doświadczenia szkoły'), ('16 godzin', 'zajęć online'), ('3 spotkania', '9:00–13:30'), ('10–12 osób', 'w grupie')])
    body += f'<section aria-label="Najważniejsze informacje" class="bg-alt py-9"><dl class="container-page flex text-center text-ink">{stats}</dl></section>'
    body += anchor_nav([('Efekty', 'efekty'), ('Program', 'program'), ('Prowadzący', 'kadra'), ('Cena', 'cena')])
    odb = [('Zaczynasz od zera', 'Nie potrzebujesz doświadczenia w grafice 3D.'), ('Chcesz pokazać produkt w 3D', 'Wizualizacje do sklepu, social mediów i prezentacji.'),
           ('Myślisz o pracy grafika 3D', 'Kurs to pierwszy krok i pierwsza praca w portfolio.'), ('Szukasz dofinansowania', 'Kurs może sfinansować urząd pracy albo KFS.')]
    cards = ''.join(f'<article class="ps-card items-center text-center"><img src="assets/figma/icon-printer.svg" alt="" class="h-16"><h3 class="text-xl font-medium leading-7">{a}</h3><p class="text-base leading-6">{b}</p></article>' for a, b in odb)
    body += f'''<section class="container-page scroll-mt-36 py-20" id="dla-kogo">
  {ps_head('Dla kogo', 'Ten kurs jest dla Ciebie, jeśli', 'Nie musisz umieć nic z grafiki 3D.')}
  <div class="mt-10 grid grid-cols-4 gap-6">{cards}</div>
</section>'''
    kom = ['Modelujesz obiekty metodą low poly', 'Teksturujesz modele i ustawiasz materiały', 'Oświetlasz scenę i ustawiasz kamerę', 'Eksportujesz gotowy render do portfolio']
    body += f'''<section class="container-page scroll-mt-36 py-20" id="efekty">
  <div class="flex items-center gap-12">
    <div class="flex flex-1 justify-center">{photo('programy-adobe.webp', 'Pasek aplikacji na MacBooku', 1020, 960, 'max-w-[508px]')}</div>
    <div class="flex flex-1 flex-col gap-6">
      {ps_head('Efekty', 'Zyskasz takie umiejętności', 'Każdy moduł kończy się projektem, który trafia do Twojego portfolio.', center=False)}
      <ul class="space-y-4 text-base leading-6 text-ink">{''.join(check_item(o) for o in kom)}</ul>
      <p class="text-sm text-neutral-600">Programy: Blender</p>
    </div>
  </div>
</section>'''
    prog = [('Moduł 1 · Interfejs i modelowanie', 'Poruszasz się po programie i modelujesz obiekty metodą low poly.'),
            ('Moduł 2 · Materiały i światło', 'Teksturujesz modele, ustawiasz shadery i oświetlasz scenę.'),
            ('Moduł 3 · Kamera i render', 'Ustawiasz kamerę, parametry renderu i finalizujesz pracę.'),
            ('Wymagania techniczne', 'Komputer z zainstalowanym Blenderem (program jest darmowy).')]
    body += f'''<section class="container-page scroll-mt-36 py-20" id="program">
  <div class="flex items-start gap-12">
    <div class="sticky top-40 w-[360px] shrink-0">
      {ps_head('Program', 'Program kursu', 'Zajęcia online przez Jitsi. Każdy moduł kończy się pracą do portfolio.', center=False)}
      <dl class="mt-6 grid grid-cols-2 gap-4 text-ink">
        <div class="rounded-2xl bg-alt p-4"><dd class="text-2xl font-semibold">16 godz.</dd><dt class="text-sm text-neutral-600">zajęć</dt></div>
        <div class="rounded-2xl bg-alt p-4"><dd class="text-2xl font-semibold">3 spotkania</dd><dt class="text-sm text-neutral-600">17, 18 i 24.10</dt></div>
      </dl>
      <div class="mt-6">{btn('Pobierz program (PDF)', '#', 'brand-outline')}</div>
    </div>
    <div class="flex-1">{ps_accordion(prog, heading=True)}</div>
  </div>
</section>'''
    body += f'''<section class="container-page scroll-mt-36 py-20" id="kadra">
  <div class="flex items-center gap-12">
    <div class="flex flex-1 flex-col gap-8">
      {ps_head('Prowadząca', 'mgr Anastasiia Dudina', 'Graficzka 3D, specjalistka Blendera. Absolwentka grafiki 3D w Publishing School, pracuje jako freelancerka i tworzy modele oraz wizualizacje.', center=False)}
      <dl class="flex gap-4 text-ink">{''.join(f'<div class="flex flex-1 flex-col justify-center gap-2 rounded-2xl bg-alt p-4"><dt class="order-2 text-base leading-6">{b}</dt><dd class="order-1 text-2xl font-semibold leading-8">{a}</dd></div>' for a, b in [('Blender 3D', 'specjalizacja'), ('Orły Edukacji', 'wyróżnienie szkoły'), ('Z hologramem', 'certyfikat')])}</dl>
    </div>
    <div class="flex flex-1 justify-center">{media('Zdjęcie prowadzącej lub praca z kursu', 'aspect-[4/3] w-full')}</div>
  </div>
</section>'''
    body += price_block(['Materiały do zajęć', 'Nagrania zajęć', 'Certyfikat z hologramem', 'Wysyłka certyfikatu', 'Konsultacje', 'Scena do portfolio', 'Status uczestnika', 'Wsparcie sekretariatu'],
                        'Kurs opłacasz z góry, przed startem. Możesz też rozłożyć płatność albo skorzystać z dofinansowania KFS.')
    body += final_cta('Zarezerwuj miejsce w grupie 2026/27', 'Nabór 2026/27: liczba miejsc w grupach jest ograniczona.', second=('Zobacz kursy roczne', 'index.html#kursy-roczne'))
    body += ps_faq([
        ('Jak działa dofinansowanie z KFS?', 'Krajowy Fundusz Szkoleniowy dla osób zatrudnionych — wniosek składa pracodawca w urzędzie pracy właściwym dla regionu zarejestrowania siedziby firmy. <a href="dofinansowanie.html" class="text-brand hover:underline">Zobacz dofinansowanie</a>'),
        ('Czy potrzebuję własnego laptopa?', 'Tak, z zainstalowanym Blenderem. Program jest darmowy.'),
        ('Jak wyglądają zajęcia online?', 'Łączysz się przez Jitsi i pracujesz w programie razem z prowadzącą. Nie trzeba zakładać konta.'),
        ('Czy dostanę certyfikat?', 'Tak. Po kursie wysyłamy pocztą hologramowany certyfikat w języku polskim.'),
        ('Co jeśli grupa się nie zbierze?', 'Zaproponujemy najbliższy termin tego samego kursu albo zwrot wpłaty.'),
        ('Kiedy płacę za kurs?', 'Kurs krótki opłacasz z góry, przed pierwszymi zajęciami.'),
    ], f'Nie ma tu Twojego pytania? Zadzwoń {PHONE}.')
    page('kurs-krotki.html', 'Blender 3D od podstaw', body, 'Kurs Blender 3D od podstaw: 16 h online, certyfikat z hologramem.')


def jak_sie_zapisac():
    body = breadcrumbs([('Strona główna', 'index.html'), ('Zapisy', ''), ('Jak się zapisać', '')])
    extra = f'''<div class="mt-1 flex gap-2">{btn('Kurs roczny — 4 kroki', '#przebieg', 'brand', attrs='data-open-tab="roczne"')}{btn('Kurs krótki — 3 kroki', '#przebieg', 'brand-outline', attrs='data-open-tab="krotkie"')}</div>
    <p class="text-sm">Wahasz się między kierunkami? Napisz maila lub zadzwoń: <a href="{PHONE_HREF}" class="font-medium hover:underline">504 068 626</a></p>'''
    body += center_hero('Jak się zapisać', 'Zapis wygląda inaczej na kurs roczny i na kurs krótki. Wybierz, na co się zapisujesz, i sprawdź kolejne kroki.', extra)
    body += hero_banner()
    roczne = ps_accordion([
        ('Krok 1 · Wypełniasz formularz (5 minut)', ab('Zaczynasz od formularza zgłoszeniowego.', ['pobierz formularz dla swojego kierunku', 'wypełnij go w czytniku PDF', 'nie wiesz, który kierunek wybrać? Zadzwoń, doradzimy bez zobowiązań'])),
        ('Krok 2 · Wysyłasz dokumenty', ab('Potrzebujemy tylko kilku rzeczy.', ['wypełniony formularz', '2 zdjęcia paszportowe', 'adres do wysyłki: <a href="mailto:krystyna@publishingschool.pl" class="text-brand hover:underline">krystyna@publishingschool.pl</a>'], 'Z dokumentami do dofinansowania pomoże sekretariat.')),
        ('Krok 3 · Krótka rozmowa', ab('To nie egzamin, tylko spotkanie na start.', ['online przez Jitsi, mailowo albo telefonicznie', 'dopasujemy formę zajęć: online lub Kraków', 'odpowiemy na Twoje pytania o program i raty'])),
        ('Krok 4 · Zaczynasz kurs', ab('Zostały już tylko formalności.', ['podpisujesz kontrakt edukacyjny', 'wybierasz raty 0% albo płatność jednorazową', 'zaczynasz zajęcia pod koniec września']))], heading=True)
    krotkie = ps_accordion([
        ('Krok 1 · Wybierasz termin (2 minuty)', ab('Wszystko robisz na stronie kursu.', ['wybierasz termin zajęć', 'wypełniasz krótki formularz', 'nie potrzebujesz rozmowy wstępnej ani zdjęć'])),
        ('Krok 2 · Opłacasz miejsce', ab('Opłata z góry rezerwuje Twoje miejsce w grupie.', ['płacisz przed startem kursu', 'możesz poprosić o fakturę na firmę', 'dokumenty do KFS przygotujemy w 24 h'])),
        ('Krok 3 · Dostajesz potwierdzenie', ab('Zanim zaczniesz, dostaniesz komplet informacji.', ['e-mail z potwierdzeniem zapisu', 'harmonogram zajęć', 'link do zajęć online']))], heading=True)
    def panel(key, eyebrow, title, text, c1, c2, acc, hidden):
        return f'''<div data-panel="{key}" role="tabpanel"{' hidden' if hidden else ''} class="flex items-start gap-12">
      <div class="w-[406px] shrink-0">
        {ps_head(eyebrow, title, text, center=False)}
        <dl class="mt-6 grid grid-cols-2 gap-4 text-ink">
          <div class="rounded-2xl bg-alt p-4"><dd class="text-xl font-semibold">{c1[0]}</dd><dt class="text-sm text-neutral-600">{c1[1]}</dt></div>
          <div class="rounded-2xl bg-alt p-4"><dd class="text-xl font-semibold">{c2[0]}</dd><dt class="text-sm text-neutral-600">{c2[1]}</dt></div>
        </dl>
      </div>
      <div class="flex-1">{acc}</div>
    </div>'''
    body += f'''<section class="container-page scroll-mt-24 pb-20 pt-16" id="przebieg">
  {ps_head('Zapisy', 'Jak przebiega zapis', 'Na kurs roczny zapisujesz się w 4 krokach, na kurs krótki w 3.')}
  <div role="tablist" aria-label="Rodzaj kursu" data-tabs data-tabs-target="#przebieg-panele" class="mx-auto mt-6 flex w-fit overflow-hidden rounded-full border border-brand">
    <button type="button" role="tab" data-tab="roczne" aria-selected="true" class="seg">Kursy roczne</button>
    <button type="button" role="tab" data-tab="krotkie" aria-selected="false" class="seg">Kursy krótkie</button>
  </div>
  <div id="przebieg-panele" class="mt-10">
    {panel('roczne', 'Kursy roczne', 'Zapisy na kursy roczne', 'Pobierz formularz dla swojego kierunku, wypełnij go i prześlij e-mailem.', ('4 kroki', 'formalności'), ('2 zdjęcia', 'paszportowe'), roczne, False)}
    {panel('krotkie', 'Kursy krótkie', 'Zapisy na kursy krótkie', 'Bez zdjęć i rozmowy wstępnej. Miejsce rezerwuje opłata wniesiona z góry.', ('3 kroki', 'formalności'), ('Opłata z góry', 'przed startem'), krotkie, True)}
  </div>
</section>
<section class="container-page py-20" id="kursy-roczne">
  {ps_head('Kursy roczne', 'Kursy roczne — 9 miesięcy przygotowania do pracy w grafice', 'Wybierz specjalizację. 200 godzin zajęć w soboty i niedziele, od końca września do końca czerwca — online na żywo albo w Krakowie.')}
  <div class="mt-10 grid grid-cols-4 gap-6">{''.join(ps_card(c['name'], c['card'], 'Zobacz program', c['slug'], c['icon']) for c in COURSES)}</div>
</section>'''
    body += final_cta()
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
    kursy_roczne()
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
