// Konfiguracja Tailwinda dla wszystkich stron.
// Tokeny z makiety Figma „PS Lo-Fi”: marka (magenta), info (cyjan), tekst, tła i stopka.
// Pozostałe kolory: domyślna paleta Tailwinda (gray-*).
tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      colors: {
        brand: { DEFAULT: '#b04090', dark: '#96367b', soft: '#fbeff7' },
        info: '#009daf',
        ink: '#0a0a0a',
        olive: '#32340a',
        page: '#fafafa',
        alt: '#f5f5f5',
        stopka: '#404040',
      },
      borderRadius: {
        card: '1.5rem',
      },
      boxShadow: {
        proof: '0 2px 10px rgb(17 24 39 / 0.08)',
      },
    },
  },
};
