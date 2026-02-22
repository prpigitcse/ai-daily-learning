"use client";

import { useState } from "react";
import { LearningEntry } from "@/lib/types";
import { TimelineDay } from "./TimelineDay";

interface TimelineWeekProps {
    weekRange: string;
    days: LearningEntry[];
}

export function TimelineWeek({ weekRange, days }: TimelineWeekProps) {
    const [isOpen, setIsOpen] = useState(true);

    return (
        <div>
            <button
                className="flex items-center gap-3 w-full text-left group mb-6 focus:outline-none"
                onClick={() => setIsOpen(!isOpen)}
            >
                <div className={`transition-transform duration-200 ${isOpen ? "rotate-90" : ""}`}>
                    <svg className="w-3.5 h-3.5 text-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M9 5l7 7-7 7" />
                    </svg>
                </div>
                <span className="text-xs font-semibold text-muted group-hover:text-foreground transition-colors">
                    {weekRange}
                </span>
            </button>

            {isOpen && (
                <div className="space-y-8 pl-1 ml-[7px] border-l border-card-border">
                    {days.map((day, idx) => (
                        <TimelineDay key={idx} day={day} />
                    ))}
                </div>
            )}
        </div>
    );
}
