import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getEntry, getAllEntries } from '@/lib/parser';
import { renderMarkdown } from '@/lib/markdown';
import { ArticleSection } from '@/components/content/ArticleSection';
import { CodeBlock } from '@/components/content/CodeBlock';
import { ExplanationBlock } from '@/components/content/ExplanationBlock';

interface PageProps {
    params: Promise<{
        year: string;
        month: string;
        day: string;
    }>;
}

export async function generateStaticParams() {
    const entries = await getAllEntries();
    return entries.map((entry) => ({
        year: entry.year,
        month: entry.month,
        day: entry.day,
    }));
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
    const { year, month, day } = await params;
    const entry = await getEntry(year, month, day);

    if (!entry) notFound();

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
        </article>
    );
}
