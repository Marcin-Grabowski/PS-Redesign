import { buttonVariants } from "@/components/ui/button"
import { Wordmark } from "@/components/site-header"
import { CONTACT, LINKS } from "@/lib/contact"
import { cn } from "@/lib/utils"

const link =
  "text-sm text-foreground/80 underline-offset-4 hover:text-primary hover:underline focus-visible:rounded-sm focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:outline-none"

export function SiteFooter() {
  return (
    <>
      {/* pasek dla firm */}
      <section aria-label="Oferta dla firm" className="border-t bg-card">
        <div className="mx-auto flex w-full max-w-6xl flex-col items-start justify-between gap-4 px-4 py-8 sm:flex-row sm:items-center sm:px-6">
          <p className="text-xl font-medium tracking-tight text-balance sm:text-2xl">
            <span className="text-primary">Prowadzisz firmę?</span> Zobacz ofertę
            szkoleń dla zespołów
          </p>
          <a
            href="/kontakt#formularz"
            className={cn(buttonVariants({ size: "lg" }), "h-11 shrink-0 px-5")}
          >
            Zapytaj o szkolenie
          </a>
        </div>
      </section>

      <footer className="border-t bg-card">
        <div className="mx-auto grid w-full max-w-6xl gap-10 px-4 py-12 sm:px-6 lg:grid-cols-12">
          <div className="flex flex-col gap-3 lg:col-span-5">
            <Wordmark />
            <p className="text-sm font-medium">Szkoła grafiki komputerowej</p>
            <address className="text-sm text-muted-foreground not-italic">
              {CONTACT.schoolName}
              <br />
              {CONTACT.address.city}
              <br />
              {CONTACT.address.street}
            </address>
            <p className="text-sm text-muted-foreground">
              Sekretariat czynny: pon–pt, 12:30–18:30
              <br />
              <a href={`mailto:${CONTACT.email}`} className="text-primary underline-offset-4 hover:underline">
                {CONTACT.email}
              </a>
            </p>
          </div>

          <nav aria-label="Stopka" className="grid grid-cols-2 gap-8 sm:grid-cols-3 lg:col-span-7">
            {Object.entries(LINKS.footer).map(([title, items]) => (
              <div key={title} className="flex flex-col gap-3">
                <p className="text-sm font-semibold text-primary">{title}</p>
                <ul className="flex flex-col gap-2">
                  {items.map((l) => (
                    <li key={l.label}>
                      <a href={l.href} className={link}>
                        {l.label}
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </nav>
        </div>

        <div className="border-t">
          <div className="mx-auto flex w-full max-w-6xl flex-col gap-3 px-4 py-5 text-xs text-muted-foreground sm:flex-row sm:items-center sm:justify-between sm:px-6">
            <p>© 2026 Publishing School — Wszystkie prawa zastrzeżone</p>
            <p className="flex flex-wrap gap-x-4 gap-y-1">
              <a href={LINKS.privacy} className="underline-offset-4 hover:underline">
                Polityka prywatności
              </a>
              <a href={LINKS.privacy} className="underline-offset-4 hover:underline">
                RODO
              </a>
              <a href={LINKS.complaints} className="underline-offset-4 hover:underline">
                Procedura reklamacyjna
              </a>
            </p>
          </div>
        </div>
      </footer>
    </>
  )
}
