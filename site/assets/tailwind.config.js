// Konfiguracja Tailwinda dla wszystkich stron.
// Kolory: domyślna paleta Tailwinda (bez własnych nazw):
//   tekst: gray-900 / gray-600 / gray-500   linie: gray-300   obramowania: gray-400
//   tła: white, gray-50, gray-100            przycisk główny: gray-500 → hover gray-600
//   akcent marki (logo, „Zapisz się” w nagłówku): fuchsia-700 → hover fuchsia-800
//   etykieta „Finansowanie nauki”: teal-700   stopka: gray-500
tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '1rem',
      },
      boxShadow: {
        proof: '0 2px 10px rgb(17 24 39 / 0.08)',
      },
    },
  },
};
