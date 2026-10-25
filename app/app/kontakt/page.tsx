import type { Metadata } from "next"
import {
  ArrowUpRightIcon,
  ChevronRightIcon,
  ClockIcon,
  LandmarkIcon,
  MailIcon,
  MapPinIcon,
  PhoneIcon,
  SchoolIcon,
} from "lucide-react"

import { ContactForm } from "@/components/contact-form"
import { Wordmark } from "@/components/site-header"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { CONTACT } from "@/lib/contact"
import { cn } from "@/lib/utils"

export const metadata: Metadata = {
  title: "Kontakt",
  description:
    "Kontakt z Publishing School: telefon, e-mail, adres w Krakowie, formularz i dane szkoły. Odpowiadamy najpóźniej następnego dnia roboczego.",
}

const linkClass =
  "font-medium text-foreground underline-offset-4 hover:text-primary hover:underline focus-visible:rounded-sm focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:outline-none"

function IconTile({ children }: { children: React.ReactNode }) {
  return (
    <span
      aria-hidden="true"
      className="flex size-10 shrink-0 items-center justify-center rounded-lg bg-accent text-accent-foreground"
    >
      {children}
    </span>
  )
}

function Eyebrow({ children }: { children: React.ReactNode }) {
  return (
    <p className="text-sm font-medium tracking-wide text-primary uppercase">{children}</p>
  )
}

function DefinitionList({
  items,
}: {
  items: readonly { label: string; value: string }[]
}) {
  return (
    <dl className="flex flex-col text-sm">
      {items.map((i) => (
        <div
          key={i.label}
          className="flex flex-col gap-0.5 border-t py-2.5 first:border-t-0 first:pt-0 sm:flex-row sm:justify-between sm:gap-4"
        >
          <dt className="text-muted-foreground">{i.label}</dt>
          <dd className="font-medium tabular-nums sm:text-right">{i.value}</dd>
        </div>
      ))}
    </dl>
  )
}

export default function ContactPage() {
  return (
    <div className="mx-auto w-full max-w-6xl px-4 sm:px-6">
      {/* Okruszki */}
      <nav aria-label="Okruszki" className="pt-6">
        <ol className="flex items-center gap-2 text-sm text-muted-foreground">
          <li>
            <a href="https://publishingschool.pl/" className="hover:text-foreground hover:underline">
              Strona główna
            </a>
          </li>
          <li aria-hidden="true">
            <ChevronRightIcon className="size-4" />
          </li>
          <li aria-current="page" className="font-medium text-primary">
            Kontakt
          </li>
        </ol>
      </nav>

      {/* Hero: tytuł + dane szkoły */}
      <section className="grid items-center gap-10 py-12 sm:py-16 lg:grid-cols-2 lg:gap-16">
        <div className="flex flex-col gap-4">
          <Eyebrow>Kontakt</Eyebrow>
          <h1 className="text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
            Zadzwoń albo napisz
          </h1>
          <p className="max-w-md text-lg text-muted-foreground text-pretty">
            Odpowiadamy najpóźniej następnego dnia roboczego.
          </p>
        </div>

        <Card>
          <CardHeader className="gap-4">
            <Wordmark />
            <CardDescription className="text-sm text-foreground">
              {CONTACT.schoolName}
            </CardDescription>
          </CardHeader>
          <CardContent className="flex flex-col gap-3 text-sm">
            <div className="flex items-start gap-3">
              <PhoneIcon className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <p className="flex flex-col">
                {CONTACT.phones.map((p) => (
                  <a key={p.href} href={p.href} className={linkClass}>
                    +48 {p.label}
                  </a>
                ))}
              </p>
            </div>
            <div className="flex items-start gap-3">
              <MailIcon className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <a href={`mailto:${CONTACT.email}`} className={cn(linkClass, "break-all")}>
                {CONTACT.email}
              </a>
            </div>
            <div className="flex items-start gap-3">
              <ClockIcon className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <p>Sekretariat czynny {CONTACT.secretariatHours}</p>
            </div>
            <div className="flex items-start gap-3">
              <MapPinIcon className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <p>
                {CONTACT.address.city} {CONTACT.address.street}
              </p>
            </div>
          </CardContent>
        </Card>
      </section>

      {/* Trzy sposoby kontaktu */}
      <section aria-labelledby="sposoby" className="pb-14">
        <h2 id="sposoby" className="sr-only">
          Sposoby kontaktu
        </h2>
        <div className="grid gap-4 md:grid-cols-3">
          <Card className="h-full">
            <CardHeader>
              <IconTile>
                <PhoneIcon className="size-5" />
              </IconTile>
              <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                Zadzwoń
              </CardTitle>
              <CardDescription>Odbieramy {CONTACT.phoneHours}.</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col gap-1 text-lg">
              {CONTACT.phones.map((p) => (
                <a key={p.href} href={p.href} className={linkClass}>
                  {p.label}
                </a>
              ))}
            </CardContent>
          </Card>

          <Card className="h-full">
            <CardHeader>
              <IconTile>
                <MailIcon className="size-5" />
              </IconTile>
              <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                Napisz do nas
              </CardTitle>
              <CardDescription>Użyj formularza albo napisz na adres sekretariatu.</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col items-start gap-2 text-sm">
              <a href="#formularz" className={linkClass}>
                Przejdź do formularza
              </a>
              <a href={`mailto:${CONTACT.email}`} className={cn(linkClass, "break-all")}>
                {CONTACT.email}
              </a>
            </CardContent>
          </Card>

          <Card className="h-full">
            <CardHeader>
              <IconTile>
                <SchoolIcon className="size-5" />
              </IconTile>
              <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                Odwiedź sekretariat
              </CardTitle>
              <CardDescription>
                Pon–pt 12:30–18:30. Przed wizytą najlepiej zadzwonić.
              </CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col items-start gap-2 text-sm">
              <p className="font-medium">
                {CONTACT.address.street}, {CONTACT.address.city}
              </p>
              <a
                href={CONTACT.address.mapUrl}
                target="_blank"
                rel="noopener noreferrer"
                className={cn(linkClass, "inline-flex items-center gap-1")}
              >
                Pokaż na mapie
                <ArrowUpRightIcon className="size-4" aria-hidden="true" />
                <span className="sr-only">(otwiera się w nowej karcie)</span>
              </a>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Formularz */}
      <section
        id="formularz"
        aria-labelledby="napisz-do-nas"
        className="scroll-mt-24 border-t py-14"
      >
        <div className="mx-auto flex max-w-2xl flex-col items-center gap-3 text-center">
          <Eyebrow>Formularz</Eyebrow>
          <h2
            id="napisz-do-nas"
            className="text-3xl font-semibold tracking-tight text-balance"
          >
            Napisz do nas
          </h2>
          <p className="text-base text-muted-foreground text-pretty">
            Zapytaj o kurs, termin, dofinansowanie albo ofertę dla firmy.
          </p>
        </div>
        <Card className="mx-auto mt-8 max-w-2xl">
          <CardContent className="p-6 sm:p-8">
            <ContactForm />
          </CardContent>
        </Card>
      </section>

      {/* Dane szkoły */}
      <section aria-labelledby="dane-szkoly" className="border-t py-14">
        <div className="mx-auto flex max-w-2xl flex-col items-center gap-3 text-center">
          <Eyebrow>Dane szkoły</Eyebrow>
          <h2 id="dane-szkoly" className="text-3xl font-semibold tracking-tight">
            O szkole
          </h2>
        </div>

        <div className="mt-8 grid gap-4 lg:grid-cols-2">
          <div className="flex flex-col gap-4">
            <Card>
              <CardHeader>
                <IconTile>
                  <ClockIcon className="size-5" />
                </IconTile>
                <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                  Sekretariat
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-col gap-2 text-sm">
                  <p>Sekretariat czynny {CONTACT.secretariatHours}</p>
                  <p className="text-muted-foreground">
                    Kontakt mailowy i telefoniczny możliwy jest codziennie w godzinach 9:00–20:00.
                  </p>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <IconTile>
                  <LandmarkIcon className="size-5" />
                </IconTile>
                <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                  Konto bankowe
                </CardTitle>
              </CardHeader>
              <CardContent className="flex flex-col gap-2 text-sm">
                <p>w {CONTACT.bank.name}:</p>
                <p className="text-lg font-medium tracking-tight tabular-nums">
                  {CONTACT.bank.account}
                </p>
                <p className="text-muted-foreground">
                  Nazwa konta: {CONTACT.bank.accountName}
                </p>
              </CardContent>
            </Card>
          </div>

          <Card>
            <CardHeader>
              <IconTile>
                <SchoolIcon className="size-5" />
              </IconTile>
              <CardTitle role="heading" aria-level={3} className="pt-2 text-base">
                Dane szkoły
              </CardTitle>
              <CardDescription className="text-sm text-foreground">
                {CONTACT.schoolName}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <DefinitionList items={CONTACT.registry} />
            </CardContent>
          </Card>
        </div>
      </section>
    </div>
  )
}
