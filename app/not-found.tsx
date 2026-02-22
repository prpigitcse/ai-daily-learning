import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
    title: "404 — Neural Path Not Found",
    description: "The weights for this route have vanished. Latent space search failed.",
    robots: { index: false, follow: false },
};

export default function NotFound() {
    return (
        <div className="min-h-[70vh] flex flex-col items-center justify-center text-center px-6 select-none">

            {/* Big 404 with AI flavor */}
            <div className="relative mb-6">
                <span
                    className="text-[9rem] sm:text-[12rem] font-black leading-none tracking-tighter text-transparent"
                    style={{
                        WebkitTextStroke: "2px var(--card-border)",
                    }}
                >
                    404
                </span>
                {/* Glowing accent overlay representing a "distorted" signal */}
                <span
                    className="absolute inset-0 flex items-center justify-center text-[9rem] sm:text-[12rem] font-black leading-none tracking-tighter text-transparent"
                    style={{
                        WebkitTextStroke: "2px var(--accent)",
                        clipPath: "inset(0 45% 0 0)",
                        opacity: 0.6,
                    }}
                    aria-hidden="true"
                >
                    404
                </span>
            </div>

            {/* AI-flavored badge */}
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-card-border bg-card text-xs font-mono text-muted mb-5">
                <span className="w-2 h-2 rounded-full bg-accent animate-pulse shrink-0" />
                <span>
                    <span className="text-accent">RuntimeError</span>
                    {": "}
                    Gradients failed to converge{" "}
                    <span className="text-accent underline decoration-dotted underline-offset-2">NaN detected</span>
                    {" in latent space"}
                </span>
            </div>

            <h1 className="text-2xl font-bold tracking-tight mb-2">
                Neural Path Not Found
            </h1>
            <p className="text-muted text-sm max-w-sm mb-8 leading-relaxed">
                The weights for this route have vanished. We&apos;ve explored the entire latent space,
                but this coordinate remains undefined in our model.
            </p>

            {/* Actions */}
            <div className="flex items-center gap-3">
                <Link
                    href="/"
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-accent text-white text-sm font-medium hover:opacity-90 transition-all duration-200 shadow-lg shadow-accent/20 active:scale-95"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    >
                        <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                        <polyline points="9 22 9 12 15 12 15 22" />
                    </svg>
                    Retrain for Home
                </Link>
            </div>
        </div>
    );
}
