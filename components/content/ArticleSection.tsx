interface ArticleSectionProps {
    title: string;
    children: React.ReactNode;
}

export function ArticleSection({ title, children }: ArticleSectionProps) {
    return (
        <section className="mb-12">
            <h2 className="mono text-[0.75rem] uppercase tracking-[0.15em] text-muted mb-6 flex items-center gap-4 font-bold">
                {title}
                <div className="h-px bg-card-border flex-grow"></div>
            </h2>
            <div className="text-foreground">
                {children}
            </div>
        </section>
    );
}
