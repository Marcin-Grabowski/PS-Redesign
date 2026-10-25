export type ContactField =
  | "imie"
  | "email"
  | "telefon"
  | "firma"
  | "wiadomosc"
  | "zgoda"

export type ContactFormState = {
  status: "idle" | "error" | "success"
  errors: Partial<Record<ContactField, string>>
  values: Partial<Record<ContactField, string>>
}

export const initialContactState: ContactFormState = {
  status: "idle",
  errors: {},
  values: {},
}

const SITE = "https://publishingschool.pl"

/** Dane szkoły — źródło: publishingschool.pl/kontakt (sprawdzone). */
export const CONTACT = {
  schoolName: "“Publishing School” Placówka Kształcenia Ustawicznego",
  phones: [
    { label: "504 068 626", href: "tel:+48504068626" },
    { label: "12 411 65 66", href: "tel:+48124116566" },
  ],
  phoneHours: "codziennie 9:00–20:00",
  email: "sekretariat@publishingschool.pl",
  address: {
    street: "ul. Kosynierów 15B, II piętro",
    city: "31-572 Kraków",
    mapUrl:
      "https://www.google.com/maps/search/?api=1&query=Publishing+School+ul.+Kosynier%C3%B3w+15B+Krak%C3%B3w",
  },
  secretariatHours: "poniedziałek–piątek: 12:30–18:30",
  registry: [
    { label: "Ewidencja Szkół Prezydenta Miasta Krakowa", value: "4430.13.201" },
    { label: "RSPO (Rejestr Szkół i Placówek Oświatowych)", value: "277460" },
    { label: "Rejestr Instytucji Szkoleniowych WUP w Krakowie", value: "2.12/00188/2021" },
    { label: "REGON", value: "388971036" },
    { label: "NIP", value: "675-178-63-00" },
  ],

  bank: {
    name: "Santander Bank Polska",
    account: "07 1910 1048 2117 0607 5842 0001",
    accountName: "Publishing School Placówka Kształcenia Ustawicznego, ul. Kosynierów 15B, 31-572 Kraków",
  },
} as const

/** Odnośniki do aktualnej strony szkoły (strony tej aplikacji jeszcze nie istnieją). */
export const LINKS = {
  privacy: `${SITE}/polityka-prywatnosci/`,
  complaints: `${SITE}/procedura-reklamacyjna/`,
  nav: [
    { label: "Kurs", href: `${SITE}/najblizsze-kursy-2/` },
    { label: "Zapisy", href: `${SITE}/rekrutacja/` },
    { label: "Dla firm", href: "/kontakt#formularz" },
    { label: "O szkole", href: `${SITE}/o-szkole/` },
    { label: "Blog", href: `${SITE}/blog/` },
  ],
  footer: {
    Kursy: [
      { label: "Grafika 3D", href: `${SITE}/grafika-3d/` },
      { label: "Web designer UI/UX", href: `${SITE}/web-design/` },
      { label: "Grafika DTP", href: `${SITE}/poligrafia-dtp/` },
      { label: "Grafik reklamy", href: `${SITE}/grafika-reklamowa/` },
      { label: "Kursy krótkie", href: `${SITE}/najblizsze-kursy-2/` },
    ],
    Rekrutacja: [
      { label: "Jak się zapisać", href: `${SITE}/rekrutacja/` },
      { label: "Dofinansowanie kursów", href: `${SITE}/dofinansowania/` },
    ],
    "O nas": [
      { label: "O szkole", href: `${SITE}/o-szkole/` },
      { label: "Prace absolwentów", href: `${SITE}/portfolia-absolwentow/` },
      { label: "Blog", href: `${SITE}/blog/` },
      { label: "Kontakt", href: "/kontakt" },
    ],
  },
} as const
