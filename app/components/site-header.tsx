import Link from "next/link"

import { buttonVariants } from "@/components/ui/button"
import { LINKS } from "@/lib/contact"
import { cn } from "@/lib/utils"

/** Znak szkoły z trzech kółek (kolory logo) i nazwa. */
export function Wordmark({ className }: { className?: string }) {
  return (
    <span className={cn("flex items-center gap-2.5", className)}>
      <span className="relative block h-8 w-9 shrink-0" aria-hidden="true">
        <span className="absolute top-0 left-0 size-5 rounded-full bg-[#A4488D]" />
        <span className="absolute top-2.5 left-3 size-4 rounded-full bg-[#B1B63E]/90" />
        <span className="absolute bottom-0 left-1 size-3.5 rounded-full bg-[#4EACC8]/90" />
      </span>
      <span className="text-base leading-4 font-semibold tracking-tight">
        publishing
        <br />
        school
      </span>
    </span>
  )
}

const navLink =
  "rounded-md px-3 py-2 text-sm font-medium text-foreground/80 transition-colors hover:text-primary focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:outline-none"

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-40 border-b bg-background/90 backdrop-blur supports-[backdrop-filter]:bg-background/70">
      <div className="mx-auto flex h-16 w-full max-w-6xl items-center justify-between gap-4 px-4 sm:px-6">
        <Link href="/" aria-label="Publishing School, strona główna">
          <Wordmark />
        </Link>
        <nav aria-label="Główna" className="hidden items-center md:flex">
          {LINKS.nav.map((l) => (
            <a key={l.label} href={l.href} className={navLink}>
              {l.label}
            </a>
          ))}
          <Link href="/kontakt" aria-current="page" className={cn(navLink, "text-primary")}>
            Kontakt
          </Link>
        </nav>
        <a
          href={LINKS.nav[1].href}
          className={cn(buttonVariants({ size: "lg" }), "h-10 px-4")}
        >
          Zapisz się
        </a>
      </div>
    </header>
  )
}
