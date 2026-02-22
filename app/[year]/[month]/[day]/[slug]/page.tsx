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
        <article>
            {/* Theory Section */}
            <ArticleSection title="The Theory">
                <div
                    className="space-y-4"
                    dangerouslySetInnerHTML={{ __html: renderedTheory }}
                />
            </ArticleSection>

            {/* Math Section */}
            <ArticleSection title="The Math">
                <div
                    className="math-container"
                    dangerouslySetInnerHTML={{ __html: renderedMath }}
                />
            </ArticleSection>

            {/* Code Section */}
            <ArticleSection title="The Code">
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
    );
}
