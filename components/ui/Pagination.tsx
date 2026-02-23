import Link from 'next/link';

interface PaginationProps {
    prev?: { href: string; label: string } | null;
    next?: { href: string; label: string } | null;
    currentPage?: number;
    totalPages?: number;
}

export function Pagination({ prev, next, currentPage, totalPages }: PaginationProps) {
    const actualPrev = prev;
    const actualNext = next;

    // Format numbers as 01, 02, etc.
    const formatNumber = (num: number) => num.toString().padStart(2, '0');

    return (
        <div className="flex items-center gap-3">
            {actualPrev ? (
                <Link
                    href={actualPrev.href}
                    className="group flex items-center h-8 bg-card border border-card-border hover:border-accent rounded-md transition-all duration-200 overflow-hidden max-w-[120px] md:max-w-[180px]"
                    title={`Newer: ${actualPrev.label}`}
                >
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-r border-card-border group-hover:border-accent transition-colors">
                        <svg className="w-3.5 h-3.5 text-muted group-hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M15 19l-7-7 7-7" />
                        </svg>
                    </div>
                    <span className="px-2 text-[9px] mono uppercase tracking-tight text-muted group-hover:text-accent transition-colors truncate">
                        {actualPrev.label}
                    </span>
                </Link>
            ) : (
                <div className="flex items-center h-8 bg-card/30 border border-card-border/50 rounded-md opacity-30 cursor-not-allowed hidden md:flex">
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-r border-card-border/50">
                        <svg className="w-3.5 h-3.5 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M15 19l-7-7 7-7" />
                        </svg>
                    </div>
                </div>
            )}

            {currentPage && totalPages && (
                <div className="flex items-center justify-center px-3 h-8 mono text-[10px] font-bold text-muted bg-muted/10 border border-card-border/50 rounded-md min-w-[70px]">
                    <span className="text-accent">{formatNumber(currentPage)}</span>
                    <span className="mx-1 text-card-border">/</span>
                    <span>{formatNumber(totalPages)}</span>
                </div>
            )}

            {actualNext ? (
                <Link
                    href={actualNext.href}
                    className="group flex items-center h-8 bg-card border border-card-border hover:border-accent rounded-md transition-all duration-200 overflow-hidden max-w-[120px] md:max-w-[180px]"
                    title={`Older: ${actualNext.label}`}
                >
                    <span className="px-2 text-[9px] mono uppercase tracking-tight text-muted group-hover:text-accent transition-colors truncate">
                        {actualNext.label}
                    </span>
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-l border-card-border group-hover:border-accent transition-colors">
                        <svg className="w-3.5 h-3.5 text-muted group-hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                        </svg>
                    </div>
                </Link>
            ) : (
                <div className="flex items-center h-8 bg-card/30 border border-card-border/50 rounded-md opacity-30 cursor-not-allowed hidden md:flex">
                    <div className="flex items-center justify-center w-8 h-8 shrink-0 border-l border-card-border/50">
                        <svg className="w-3.5 h-3.5 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                        </svg>
                    </div>
                </div>
            )}
        </div>
    );
}
