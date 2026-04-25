export interface MetaData {
    title: string;
    math_topic?: string;
    ai_topic?: string;
    code_topic?: string;
    tags?: string[];
}

export interface LearningEntry {
    year: string;
    month: string;
    day: string;
    slug: string; // YYYY/Month/DD
    meta: MetaData;
    theory?: string;
    architecture?: string;
    math?: string;
    errorInsight?: string;
    code?: string;
    explanation?: string;
    excerpt?: string;
    excerptHtml?: string;
    date: Date;
}

export interface GroupedEntries {
    month: string;
    weeks: {
        weekRange: string;
        days: LearningEntry[];
    }[];
}
