import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Analytics } from "@vercel/analytics/react";


import { SpeedInsights } from "@vercel/speed-insights/next";
import Link from "next/link";
import Image from "next/image";
import { ThemeToggle } from "@/components/ThemeToggle";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AI Logbook",
  description: "A structured public trail of learning artificial intelligence.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var theme = localStorage.getItem('theme');
                  var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                  if (theme === 'dark' || (!theme && prefersDark)) {
                    document.documentElement.classList.add('dark');
                  }
                } catch(e) {}
              })();
            `,
          }}
        />
      </head>
      <body
        className={`${inter.variable} ${jetbrainsMono.variable} antialiased selection:bg-accent-bg selection:text-accent min-h-screen bg-background text-foreground`}
      >
        <div className="fixed top-6 right-6 z-50">
          <ThemeToggle />
        </div>

        <header className="max-w-2xl mx-auto pt-24 pb-16 px-6 text-center">
          <Link href="/">
            <div className="w-16 h-16 flex items-center justify-center mb-6 mx-auto hover:scale-105 active:scale-95 transition-transform cursor-pointer">
              <Image
                src="/logo.svg"
                alt="AI Logbook"
                width={48}
                height={48}
                priority
              />
            </div>
          </Link>

          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full badge-live border border-card-border mb-6">
            <div className="w-2 h-2 rounded-full bg-accent animate-pulse"></div>
            <span className="mono text-[10px] font-bold uppercase tracking-wider">
              Live Learning Feed
            </span>
          </div>

          <Link href="/" className="hover:opacity-80 transition-opacity">
            <h1 className="text-4xl font-semibold tracking-tight text-foreground mb-3">
              AI <span className="text-accent">Logbook</span>
            </h1>
          </Link>
          <p className="text-muted text-lg font-light leading-relaxed">
            Understanding intelligent systems from first principles.
          </p>
        </header>

        <main className="max-w-2xl mx-auto pb-24 px-6">{children}</main>

        <footer className="max-w-2xl mx-auto px-6 pb-24 text-center">
          <div className="h-px bg-card-border w-full mb-12"></div>

          <div className="flex flex-col gap-4">
            <div className="flex items-center justify-center gap-2 text-muted text-[10px] mono uppercase tracking-widest">
              <span>Built with consistency</span>
              <span className="text-card-border">·</span>
              <span className="text-foreground font-bold">AI Logbook</span>
            </div>

            <p className="text-muted text-xs">
              © 2026 Pradosh. Educational content for personal learning and reference.
            </p>

            <div className="flex items-center justify-center gap-3 text-[10px] mono uppercase tracking-tighter text-muted">
              <Link
                href="/privacy"
                className="hover:text-accent transition-colors decoration-card-border underline-offset-4"
              >
                Privacy Policy
              </Link>
              <span className="text-card-border">·</span>
              <Link
                href="/sitemap"
                className="hover:text-accent transition-colors decoration-card-border underline-offset-4"
              >
                Sitemap
              </Link>
            </div>
          </div>
        </footer>
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}
