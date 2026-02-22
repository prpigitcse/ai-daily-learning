"use client";

import { useState } from "react";
import { LearningEntry } from "@/lib/types";
import { TimelineWeek } from "./TimelineWeek";

interface TimelineMonthProps {
    month: string;
    weeks: {
        weekRange: string;
        days: LearningEntry[];
    }[];
}

export function TimelineMonth({ month, weeks }: TimelineMonthProps) {
    const [isOpen, setIsOpen] = useState(true);

    return (
        <div className="relative">
            <button
                className="flex items-center gap-3 w-full text-left group cursor-pointer mb-8 focus:outline-none"
                onClick={() => setIsOpen(!isOpen)}
            >
                <div className={`transition-transform duration-200 ${isOpen ? "rotate-90" : ""}`}>
                    <svg className="w-3.5 h-3.5 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                    </svg>
                </div>
                <h2 className="text-sm mono font-bold uppercase tracking-[0.2em] text-muted group-hover:text-accent transition-colors">
                    {month}
                </h2>
                <div className="h-px bg-card-border flex-grow ml-4"></div>
            </button>

            {isOpen && (
                <div className="space-y-10 pl-2">
                    {weeks.map((week, idx) => (
                        <TimelineWeek key={idx} weekRange={week.weekRange} days={week.days} />
                    ))}
                </div>
            )}
        </div>
    );
}
