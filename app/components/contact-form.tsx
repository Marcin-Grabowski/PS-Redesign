"use client"

import { useActionState, useEffect, useRef, useState } from "react"
import { CheckCircle2Icon, SendIcon } from "lucide-react"

import { sendContactMessage } from "@/app/kontakt/actions"
import { Button } from "@/components/ui/button"
import { Checkbox } from "@/components/ui/checkbox"
import {
  Field,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import {
  CONTACT,
  LINKS,
  initialContactState,
  type ContactField,
  type ContactFormState,
} from "@/lib/contact"

function Hint({ children }: { children: React.ReactNode }) {
  return <span className="font-normal text-muted-foreground">{children}</span>
}

export function ContactForm() {
  const [state, formAction, pending] = useActionState(
    sendContactMessage,
    initialContactState
  )
  const formRef = useRef<HTMLFormElement>(null)
  const successRef = useRef<HTMLDivElement>(null)
  // błąd znika, gdy użytkownik zaczyna poprawiać dane pole (stan dotyczy jednego wyniku wysyłki)
  const [editedState, setEditedState] = useState<{
    forState: ContactFormState
    fields: Partial<Record<ContactField, boolean>>
  }>({ forState: state, fields: {} })
  const edited = editedState.forState === state ? editedState.fields : {}

  useEffect(() => {
    if (state.status === "error") {
      formRef.current
        ?.querySelector<HTMLElement>('[aria-invalid="true"]')
        ?.focus()
    }
    if (state.status === "success") successRef.current?.focus()
  }, [state])

  if (state.status === "success") {
    return (
      <div
        ref={successRef}
        tabIndex={-1}
        role="status"
        className="flex flex-col items-start gap-3 rounded-xl bg-accent p-6 outline-none"
      >
        <CheckCircle2Icon className="size-8 text-primary" aria-hidden="true" />
        <h3 className="text-lg font-semibold text-accent-foreground">
          Dziękujemy za wiadomość
        </h3>
        <p className="text-sm text-foreground">
          Potwierdzenie przyjdzie e-mailem. Odpowiemy najpóźniej następnego dnia
          roboczego. Jeśli sprawa jest pilna, zadzwoń:{" "}
          <a
            href={CONTACT.phones[0].href}
            className="font-medium text-accent-foreground underline underline-offset-4"
          >
            {CONTACT.phones[0].label}
          </a>{" "}
          ({CONTACT.phoneHours}).
        </p>
      </div>
    )
  }

  const err = (f: ContactField) => (edited[f] ? undefined : state.errors[f])
  const touch = (f: ContactField) => () =>
    setEditedState({ forState: state, fields: { ...edited, [f]: true } })
  const v = state.values

  return (
    <form ref={formRef} action={formAction} noValidate className="flex flex-col gap-6">
      {/* pole-pułapka dla botów, ukryte przed ludźmi i czytnikami ekranu */}
      <div aria-hidden="true" className="absolute -left-[9999px] h-0 w-0 overflow-hidden">
        <label htmlFor="strona_www">Nie wypełniaj tego pola</label>
        <input id="strona_www" name="strona_www" type="text" tabIndex={-1} autoComplete="off" />
      </div>

      <FieldGroup className="gap-5">
        <div className="grid gap-5 sm:grid-cols-2">
          <Field data-invalid={!!err("imie")}>
            <FieldLabel htmlFor="imie">
              Imię i nazwisko <Hint>(wymagane)</Hint>
            </FieldLabel>
            <Input
              id="imie"
              name="imie"
              autoComplete="name"
              required
              defaultValue={v.imie}
              onChange={touch("imie")}
              aria-invalid={!!err("imie")}
              aria-describedby={err("imie") ? "imie-error" : undefined}
              className="h-11"
            />
            <FieldError id="imie-error">{err("imie")}</FieldError>
          </Field>

          <Field data-invalid={!!err("email")}>
            <FieldLabel htmlFor="email">
              E-mail <Hint>(wymagane)</Hint>
            </FieldLabel>
            <Input
              id="email"
              name="email"
              type="email"
              autoComplete="email"
              required
              defaultValue={v.email}
              onChange={touch("email")}
              aria-invalid={!!err("email")}
              aria-describedby={err("email") ? "email-error" : undefined}
              className="h-11"
            />
            <FieldError id="email-error">{err("email")}</FieldError>
          </Field>
        </div>

        <div className="grid gap-5 sm:grid-cols-2">
          <Field data-invalid={!!err("telefon")}>
            <FieldLabel htmlFor="telefon">
              Telefon <Hint>(wymagane)</Hint>
            </FieldLabel>
            <Input
              id="telefon"
              name="telefon"
              type="tel"
              autoComplete="tel"
              required
              defaultValue={v.telefon}
              onChange={touch("telefon")}
              aria-invalid={!!err("telefon")}
              aria-describedby={err("telefon") ? "telefon-error" : "telefon-hint"}
              className="h-11"
            />
            <FieldDescription id="telefon-hint">
              Oddzwonimy, jeśli wolisz rozmowę.
            </FieldDescription>
            <FieldError id="telefon-error">{err("telefon")}</FieldError>
          </Field>

          <Field>
            <FieldLabel htmlFor="firma">
              Nazwa firmy <Hint>(opcjonalnie)</Hint>
            </FieldLabel>
            <Input
              id="firma"
              name="firma"
              autoComplete="organization"
              defaultValue={v.firma}
              className="h-11"
            />
            <FieldDescription>Jeśli pytasz o kurs dla zespołu.</FieldDescription>
          </Field>
        </div>

        <Field>
          <FieldLabel htmlFor="wiadomosc">
            Wiadomość <Hint>(opcjonalnie)</Hint>
          </FieldLabel>
          <Textarea
            id="wiadomosc"
            name="wiadomosc"
            rows={5}
            defaultValue={v.wiadomosc}
            placeholder="Napisz, który kurs Cię interesuje albo o co chcesz zapytać."
            className="min-h-32"
          />
        </Field>

        <Field orientation="horizontal" data-invalid={!!err("zgoda")}>
          <Checkbox
            id="zgoda"
            name="zgoda"
            required
            onCheckedChange={touch("zgoda")}
            aria-invalid={!!err("zgoda")}
            aria-describedby={err("zgoda") ? "zgoda-error" : undefined}
            className="mt-0.5 size-5"
          />
          <div className="flex flex-col gap-1">
            <FieldLabel htmlFor="zgoda" className="font-normal">
              <span className="leading-snug">
                Wyrażam zgodę na przetwarzanie moich danych osobowych w celu obsługi
                zgłoszenia. Szczegóły w{" "}
                <a
                  href={LINKS.privacy}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="font-medium underline underline-offset-4 hover:text-primary"
                >
                  polityce prywatności
                  <span className="sr-only"> (otwiera się w nowej karcie)</span>
                </a>
                . <Hint>(wymagane)</Hint>
              </span>
            </FieldLabel>
            <FieldError id="zgoda-error">{err("zgoda")}</FieldError>
          </div>
        </Field>
      </FieldGroup>

      <div className="flex flex-col items-start gap-3 sm:flex-row sm:items-center">
        <Button type="submit" size="lg" disabled={pending} className="h-11 px-6">
          <SendIcon data-icon="inline-start" aria-hidden="true" />
          {pending ? "Wysyłanie…" : "Wyślij"}
        </Button>
        <p className="text-sm text-muted-foreground">
          Potwierdzenie przyjdzie e-mailem. Odpowiadamy najpóźniej następnego dnia
          roboczego.
        </p>
      </div>
    </form>
  )
}
