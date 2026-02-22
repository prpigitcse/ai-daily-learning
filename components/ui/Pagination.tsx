import Link from 'next/link';

interface PaginationProps {
    prev?: { href: string; label: string } | null;
    next?: { href: string; label: string } | null;
    /** @deprecated use prev/next instead for labels */
    currentPage?: number;
    /** @deprecated use prev/next instead for labels */
    hasMore?: boolean;
}

export function Pagination({ prev, next, currentPage, hasMore }: PaginationProps) {
    // Support legacy props for homepage but with labels if possible
    const legacyPrev = currentPage && currentPage > 1 ? { href: `/?page=${currentPage - 1}`, label: `Page ${currentPage - 1}` } : null;
    const legacyNext = hasMore ? { href: `/?page=${(currentPage || 1) + 1}`, label: `Page ${(currentPage || 1) + 1}` } : null;

    const actualPrev = prev !== undefined ? prev : legacyPrev;
    const actualNext = next !== undefined ? next : legacyNext;

    return (
        <div className="flex items-center gap-2">
            {actualPrev ? (
                <Link
                    href={actualPrev.href}
                    className="group flex items-center h-8 bg-card border border-card-border hover:border-accent rounded-md transition-all duration-200 overflow-hidden max-w-[140px] md:max-w-[200px]"
                    title={`Newer: ${actualPrev.label}`}
                >
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-r border-card-border group-hover:border-accent transition-colors">
                        <svg className="w-4 h-4 text-muted group-hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M15 19l-7-7 7-7" />
                        </svg>
                    </div>
                    <span className="px-2 text-[10px] mono uppercase tracking-tight text-muted group-hover:text-accent transition-colors truncate">
                        {actualPrev.label}
                    </span>
                </Link>
            ) : (
                <div className="flex items-center h-8 bg-card/30 border border-card-border/50 rounded-md opacity-30 cursor-not-allowed">
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-r border-card-border/50">
                        <svg className="w-4 h-4 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M15 19l-7-7 7-7" />
                        </svg>
                    </div>
                    <span className="px-2 text-[10px] mono uppercase tracking-tight text-muted truncate">
                        Newest
                    </span>
                </div>
            )}

            {actualNext ? (
                <Link
                    href={actualNext.href}
                    className="group flex items-center h-8 bg-card border border-card-border hover:border-accent rounded-md transition-all duration-200 overflow-hidden max-w-[140px] md:max-w-[200px]"
                    title={`Older: ${actualNext.label}`}
                >
                    <span className="px-2 text-[10px] mono uppercase tracking-tight text-muted group-hover:text-accent transition-colors truncate">
                        {actualNext.label}
                    </span>
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-l border-card-border group-hover:border-accent transition-colors">
                        <svg className="w-4 h-4 text-muted group-hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                        </svg>
                    </div>
                </Link>
            ) : (
                <div className="flex items-center h-8 bg-card/30 border border-card-border/50 rounded-md opacity-30 cursor-not-allowed">
                    <span className="px-2 text-[10px] mono uppercase tracking-tight text-muted truncate">
                        Oldest
                    </span>
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-l border-card-border/50">
                        <svg className="w-4 h-4 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                        </svg>
                    </div>
                </div>
            )}
        </div>
    );
}
