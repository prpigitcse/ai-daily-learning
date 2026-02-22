import { getAllEntries, groupEntries } from "@/lib/parser";
import { ArticleSection } from "@/components/content/ArticleSection";
import Link from "next/link";

export const metadata = {
    title: "Sitemap — AI Logbook",
    description: "A complete list of all entries in the AI Logbook.",
};

export default async function SitemapPage() {
    const entries = await getAllEntries();
    const grouped = groupEntries(entries);

    return (
        <article>
            <ArticleSection title="Sitemap">
                <div className="space-y-12">
                    {grouped.map((monthData, mIdx) => (
                        <div key={mIdx}>
                            <h3 className="text-sm mono font-bold uppercase tracking-wider text-zinc-400 mb-6">
                                {monthData.month}
                            </h3>
                            <div className="space-y-8">
                                {monthData.weeks.map((week, wIdx) => (
                                    <div key={wIdx} className="pl-4 border-l border-zinc-100">
                                        <h4 className="text-xs font-semibold text-zinc-500 mb-4">
                                            {week.weekRange}
                                        </h4>
                                        <ul className="space-y-3">
                                            {week.days.map((day, dIdx) => (
                                                <li key={dIdx}>
                                                    <Link
                                                        href={`/${day.slug}`}
                                                        className="text-zinc-800 hover:text-violet-600 transition-colors text-sm font-medium"
                                                    >
                                                        {day.meta.title}
                                                    </Link>
                                                    <span className="text-zinc-400 text-[10px] mono ml-3 uppercase opacity-60">
                                                        {day.date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                                                    </span>
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}

                    {entries.length === 0 && (
                        <p className="text-zinc-400 italic">No entries found.</p>
                    )}
                </div>
            </ArticleSection>
        </article>
    );
}
