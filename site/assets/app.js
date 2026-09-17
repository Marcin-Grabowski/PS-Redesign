// Interakcje wspólne dla wszystkich stron. Każdy moduł jest aktywowany atrybutem data-*.
(() => {
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

  // Menu rozwijane w nagłówku: [data-dropdown] > button + [data-dropdown-panel]
  const dropdowns = $$('[data-dropdown]');
  const closeAll = (except) => dropdowns.forEach((d) => {
    if (d === except) return;
    d.querySelector('button').setAttribute('aria-expanded', 'false');
    d.querySelector('[data-dropdown-panel]').hidden = true;
  });
  dropdowns.forEach((d) => {
    const btn = d.querySelector('button');
    const panel = d.querySelector('[data-dropdown-panel]');
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = panel.hidden;
      closeAll(d);
      panel.hidden = !open;
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('click', (e) => { if (!e.target.closest('[data-dropdown]')) closeAll(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeAll(); });

  // Przełącznik ceny: [data-price] zawiera button[role=switch], [data-price-view="raty|raz"], [data-price-label="raty|raz"]
  $$('[data-price]').forEach((root) => {
    const sw = root.querySelector('[role="switch"]');
    const render = (on) => {
      sw.setAttribute('aria-checked', String(on));
      const mode = on ? 'raz' : 'raty';
      $$('[data-price-view]', root).forEach((el) => { el.hidden = el.dataset.priceView !== mode; });
      $$('[data-price-label]', root).forEach((el) => {
        const active = el.dataset.priceLabel === mode;
        el.classList.toggle('font-semibold', active);
        el.classList.toggle('text-gray-900', active);
        el.classList.toggle('text-gray-500', !active);
      });
    };
    sw.addEventListener('click', () => render(sw.getAttribute('aria-checked') !== 'true'));
    render(false);
  });

  // Zakładki / chipsy: [data-tabs] z przyciskami [data-tab="id"] i panelami [data-panel="id"] w [data-tabs-target]
  $$('[data-tabs]').forEach((group) => {
    const tabs = $$('[data-tab]', group);
    const scope = document.querySelector(group.dataset.tabsTarget) || document;
    const filter = group.dataset.tabsMode === 'filter';
    const activate = (id) => {
      tabs.forEach((t) => {
        const on = t.dataset.tab === id;
        t.setAttribute('aria-selected', String(on));
        t.classList.toggle('chip-active', on);
      });
      if (filter) {
        $$('[data-cat]', scope).forEach((card) => {
          card.hidden = !(id === 'all' || card.dataset.cat.split(' ').includes(id));
        });
      } else {
        $$('[data-panel]', scope).forEach((p) => { p.hidden = p.dataset.panel !== id; });
      }
    };
    tabs.forEach((t) => t.addEventListener('click', () => activate(t.dataset.tab)));
    $$('[data-tab-step]', group).forEach((arrow) => arrow.addEventListener('click', (e) => {
      e.stopPropagation();
      const i = tabs.findIndex((t) => t.getAttribute('aria-selected') === 'true');
      const next = tabs[(i + Number(arrow.dataset.tabStep) + tabs.length) % tabs.length];
      activate(next.dataset.tab);
      next.focus();
    }));
    const initial = tabs.find((t) => t.getAttribute('aria-selected') === 'true') || tabs[0];
    activate(initial.dataset.tab);
  });

  // Linki, które przełączają zakładkę: [data-open-tab="id"]
  $$('[data-open-tab]').forEach((link) => link.addEventListener('click', () => {
    const tab = document.querySelector('[data-tab="' + link.dataset.openTab + '"]');
    if (tab) tab.click();
  }));

  // Karuzela: [data-carousel] z [data-carousel-track] i przyciskami [data-carousel-step="-1|1"]
  $$('[data-carousel]').forEach((root) => {
    const track = root.querySelector('[data-carousel-track]');
    $$('[data-carousel-step]', root).forEach((btn) => btn.addEventListener('click', () => {
      const card = track.firstElementChild;
      const step = card ? card.getBoundingClientRect().width + 24 : track.clientWidth;
      track.scrollBy({ left: step * Number(btn.dataset.carouselStep), behavior: 'smooth' });
    }));
  });

  // Galeria prac: [data-gallery] z panelami [data-gallery-item]; kliknięty panel się rozszerza
  $$('[data-gallery]').forEach((root) => {
    const items = $$('[data-gallery-item]', root);
    const activate = (item) => items.forEach((it) => {
      const on = it === item;
      it.setAttribute('aria-expanded', String(on));
      it.style.flexGrow = on ? '3' : '1';
      it.querySelector('[data-gallery-detail]').hidden = !on;
    });
    items.forEach((it) => it.addEventListener('click', () => activate(it)));
    activate(items.find((it) => it.getAttribute('aria-expanded') === 'true') || items[0]);
  });

  // Menu sekcji: podświetla sekcję widoczną na ekranie
  const spyLinks = $$('[data-spy] a[href^="#"]');
  if (spyLinks.length && 'IntersectionObserver' in window) {
    const byId = new Map(spyLinks.map((a) => [a.getAttribute('href').slice(1), a]));
    const setActive = (id) => spyLinks.forEach((a) => {
      const on = a === byId.get(id);
      a.classList.toggle('spy-active', on);
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
    const io = new IntersectionObserver((entries) => entries.forEach((e) => {
      if (e.isIntersecting) setActive(e.target.id);
    }), { rootMargin: '-35% 0px -60% 0px' });
    byId.forEach((_, id) => { const el = document.getElementById(id); if (el) io.observe(el); });
  }
})();
