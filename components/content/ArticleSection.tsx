interface ArticleSectionProps {
    title: string;
    children: React.ReactNode;
    icon?: string;
    variant?: 'default' | 'card';
}

export function ArticleSection({ title, children, icon, variant = 'default' }: ArticleSectionProps) {
    const heading = (
        <h2 className="mono text-[0.75rem] uppercase tracking-[0.15em] text-muted mb-6 flex items-center gap-4 font-bold">
            {icon && <span className="text-base normal-case tracking-normal">{icon}</span>}
            {title}
            <div className="h-px bg-card-border flex-grow"></div>
        </h2>
    );

    return (
        <section className="mb-12">
            {heading}
            {variant === 'card' ? (
                <div className="rounded-xl border border-card-border bg-card p-6 text-sm leading-relaxed text-muted">
                    {children}
                </div>
            ) : (
                <div className="text-foreground">
                    {children}
                </div>
            )}
        </section>
    );
}
