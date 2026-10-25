"use server"

import type { ContactFormState } from "@/lib/contact"

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/
const PHONE_RE = /^[+\d][\d\s-]{6,19}$/

const text = (data: FormData, key: string) => String(data.get(key) ?? "").trim()

/**
 * Walidacja po stronie serwera. Brak dostawcy poczty: po poprawnej walidacji
 * wiadomość nie jest jeszcze nigdzie wysyłana (patrz TODO poniżej).
 */
export async function sendContactMessage(
  _prev: ContactFormState,
  formData: FormData
): Promise<ContactFormState> {
  const values = {
    imie: text(formData, "imie"),
    email: text(formData, "email"),
    telefon: text(formData, "telefon"),
    firma: text(formData, "firma"),
    wiadomosc: text(formData, "wiadomosc"),
  }

  // pole-pułapka dla botów: człowiek go nie widzi i nie wypełnia
  if (text(formData, "strona_www") !== "") {
    return { status: "success", errors: {}, values: {} }
  }

  const errors: ContactFormState["errors"] = {}
  if (values.imie.length < 2) errors.imie = "Podaj imię i nazwisko."
  if (!EMAIL_RE.test(values.email)) errors.email = "Podaj poprawny adres e-mail, np. anna@firma.pl."
  if (!PHONE_RE.test(values.telefon)) errors.telefon = "Podaj numer telefonu, np. 504 068 626."
  if (formData.get("zgoda") === null) errors.zgoda = "Zgoda jest potrzebna, żebyśmy mogli odpowiedzieć na zgłoszenie."

  if (Object.keys(errors).length > 0) {
    return { status: "error", errors, values }
  }

  // TODO: podłączyć wysyłkę (np. Resend/SMTP) na sekretariat@publishingschool.pl.
  // Do tego czasu wiadomość nie opuszcza serwera.

  return { status: "success", errors: {}, values: {} }
}
