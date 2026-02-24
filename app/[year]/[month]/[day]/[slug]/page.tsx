import Link from 'next/link';
import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getEntry, getAllEntries, getAdjacentEntries } from '@/lib/parser';
import { renderMarkdown } from '@/lib/markdown';
import { ArticleSection } from '@/components/content/ArticleSection';
import { CodeBlock } from '@/components/content/CodeBlock';
import { ExplanationBlock } from '@/components/content/ExplanationBlock';
import { Pagination } from '@/components/ui/Pagination';

interface PageProps {
    params: Promise<{
        year: string;
        month: string;
        day: string;
        slug: string;
    }>;
}

export async function generateStaticParams() {
    const entries = await getAllEntries();
    return entries.map((entry) => {
        // The parser's slug is already YYYY/month/DD/title-slug
        const [year, month, day, slug] = entry.slug.split('/');
        return { year, month, day, slug };
    });
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
    const { year, month, day } = await params;
    const entry = await getEntry(year, month, day);

    if (!entry) return { title: 'Not Found — AI Logbook' };

    return {
        title: `${entry.meta.title} — AI Logbook`,
        description: entry.excerpt,
        openGraph: {
            title: `${entry.meta.title} — AI Logbook`,
            description: entry.excerpt,
            type: 'article',
            url: `https://ai.ppradosh.com/${entry.slug}`,
        },
        twitter: {
            card: 'summary_large_image',
            title: `${entry.meta.title} — AI Logbook`,
            description: entry.excerpt,
        },
        alternates: {
            canonical: `https://ai.ppradosh.com/${entry.slug}`,
        },
    };
}

export default async function DayPage({ params }: PageProps) {
    const { year, month, day, slug } = await params;
    const entry = await getEntry(year, month, day);

    if (!entry) notFound();

    // Strict slug validation: ensure the URL slug matches the generated slug
    const expectedSlug = entry.slug.split('/').pop();
    if (slug !== expectedSlug) notFound();

    const adjacency = await getAdjacentEntries(entry.date);
    const renderedTheory = await renderMarkdown(entry.theory);
    const renderedMath = await renderMarkdown(entry.math);
    const renderedExplanation = entry.explanation ? await renderMarkdown(entry.explanation) : null;

    return (
        <>
            {/* Breadcrumb */}
            <nav aria-label="Breadcrumb" className="mb-6">
                <ol className="flex items-center gap-2 text-sm text-muted">
                    <li>
                        <Link href="/" className="hover:text-accent transition-colors">
                            Home
                        </Link>
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                    </li>
                    <li>{year}</li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                    </li>
                    <li className="capitalize">{month}</li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                    </li>
                    <li className="text-foreground font-medium">Day {day}</li>
                </ol>
            </nav>

            <article>
                {/* Header */}
                <header className="mb-8">
                    <h1 className="text-2xl font-bold tracking-tight mb-4">
                        {entry.meta.title}
                    </h1>
                    <div className="flex gap-2 text-sm text-muted">
                        {entry.meta.ai_topic && (
                            <span className="px-2 py-0.5 rounded-md bg-muted-bg font-medium">
                                {entry.meta.ai_topic}
                            </span>
                        )}
                        {entry.meta.math_topic && (
                            <span className="px-2 py-0.5 rounded-md bg-muted-bg font-medium">
                                {entry.meta.math_topic}
                            </span>
                        )}
                        {entry.meta.code_topic && (
                            <span className="px-2 py-0.5 rounded-md bg-muted-bg font-medium">
                                {entry.meta.code_topic}
                            </span>
                        )}
                    </div>
                </header>

                {/* Theory Section */}
                <ArticleSection title="The Theory" icon="🧠" variant="card">
                    <div
                        className="space-y-4 markdown-content"
                        dangerouslySetInnerHTML={{ __html: renderedTheory }}
                    />
                </ArticleSection>

                {/* Math Section */}
                <ArticleSection title="The Math" icon="📐" variant="card">
                    <div
                        className="math-container markdown-content"
                        dangerouslySetInnerHTML={{ __html: renderedMath }}
                    />
                </ArticleSection>

                {/* Code Section */}
                <ArticleSection title="The Code" icon="⚙️">
                    <div className="space-y-8">
                        <CodeBlock code={entry.code} />
                        {renderedExplanation && (
                            <ExplanationBlock explanation={renderedExplanation} />
                        )}
                    </div>
                </ArticleSection>

                {/* Pagination Section */}
                <div className="mt-20 flex justify-center border-t border-card-border pt-12">
                    <Pagination
                        prev={adjacency.next ? { href: `/${adjacency.next.slug}`, label: adjacency.next.meta.title } : null}
                        next={adjacency.prev ? { href: `/${adjacency.prev.slug}`, label: adjacency.prev.meta.title } : null}
                    />
                </div>
            </article>
        </>
    );
}
