import Link from "next/link";

export default function EntryNotFound() {
    return (
        <div className="py-24 text-center">
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-card-border bg-card text-[10px] mono text-muted mb-6">
                <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse shrink-0" />
                <span>Segmentation Fault: Entry index out of bounds</span>
            </div>

            <h1 className="text-3xl font-bold tracking-tight mb-4">
                Coordinate Not Found
            </h1>
            <p className="text-muted text-[15px] max-w-md mx-auto mb-10 leading-relaxed">
                We attempted to retrieve the weights for this specific temporal coordinate,
                but the neural path appears to be disconnected or never initialized.
            </p>

            <Link
                href="/"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-accent text-white text-sm font-medium hover:opacity-90 transition-all duration-200 shadow-lg shadow-accent/20 active:scale-95"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18"
                    height="18"
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
                Sync with Homepage
            </Link>
        </div>
    );
}
