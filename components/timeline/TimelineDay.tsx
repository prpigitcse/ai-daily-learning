import Link from "next/link";
import { LearningEntry } from "@/lib/types";

interface TimelineDayProps {
    day: LearningEntry;
}

export function TimelineDay({ day }: TimelineDayProps) {
    // Format date: e.g. "Feb 20"
    const formattedDate = day.date.toLocaleString('en-US', { month: 'short', day: 'numeric' });

    return (
        <div className="relative pl-8 entry-item">
            <div className="entry-dot"></div>
            <header className="flex items-baseline gap-4 mb-2">
                <span className="mono text-[10px] font-medium text-accent uppercase tracking-wider opacity-70">
                    {formattedDate}
                </span>
                <Link href={`/${day.slug}`}>
                    <h3 className="entry-title text-lg font-medium text-foreground leading-tight">
                        {day.meta.title}
                    </h3>
                </Link>
            </header>
            <p className="text-muted text-[15px] leading-relaxed mb-3">
                {day.excerpt}
            </p>
            <div className="flex gap-3">
                {day.meta.ai_topic && (
                    <span className="text-[10px] mono text-muted font-medium tracking-tight">
                        #{day.meta.ai_topic}
                    </span>
                )}
                {day.meta.math_topic && (
                    <span className="text-[10px] mono text-muted font-medium tracking-tight">
                        #{day.meta.math_topic}
                    </span>
                )}
                {day.meta.code_topic && (
                    <span className="text-[10px] mono text-muted font-medium tracking-tight">
                        #{day.meta.code_topic}
                    </span>
                )}
            </div>
        </div>
    );
}
