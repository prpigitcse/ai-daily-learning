import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { LearningEntry, MetaData, GroupedEntries } from './types';

const learningDirectory = path.join(process.cwd(), 'learning');

export function extractExplanation(code: string): { explanation?: string; cleanCode: string } {
    const docstringRegex = /^\s*"""([\s\S]*?)"""/;
    const match = code.match(docstringRegex);

    if (match) {
        let explanation = match[1].trim();
        if (explanation.toLowerCase().startsWith('code explanation:')) {
            explanation = explanation.substring('code explanation:'.length).trim();
        } else if (explanation.toLowerCase().startsWith('logic breakdown:')) {
            explanation = explanation.substring('logic breakdown:'.length).trim();
        }
        const cleanCode = code.replace(docstringRegex, '').trim();
        return { explanation, cleanCode };
    }

    return { cleanCode: code };
}


export async function getEntry(year: string, month: string, day: string): Promise<LearningEntry | null> {
    const yearPath = path.join(learningDirectory, year);
    if (!fs.existsSync(yearPath)) return null;

    // Find actual folder name (case-insensitive month)
    const months = fs.readdirSync(yearPath);
    const actualMonth = months.find(m => m.toLowerCase() === month.toLowerCase());

    if (!actualMonth) return null;

    const entryPath = path.join(yearPath, actualMonth, day);

    if (!fs.existsSync(entryPath)) return null;

    const metaContent = fs.readFileSync(path.join(entryPath, 'meta.md'), 'utf8');
    const theoryContent = fs.readFileSync(path.join(entryPath, 'theory.md'), 'utf8');
    const mathContent = fs.readFileSync(path.join(entryPath, 'math.md'), 'utf8');
    const codeContent = fs.readFileSync(path.join(entryPath, 'code.py'), 'utf8');

    // Manual parse of meta.md key-value pairs
    const meta: MetaData = { title: '' };
    metaContent.split('\n').forEach(line => {
        const [key, ...valueParts] = line.split(':');
        if (key && valueParts.length > 0) {
            const value = valueParts.join(':').trim().replace(/^"(.*)"$/, '$1');
            (meta as any)[key.trim()] = value;
        }
    });

    if (meta.title === '') meta.title = `${month} ${day}, ${year}`;

    const { explanation, cleanCode } = extractExplanation(codeContent);

    // Excerpt is the first paragraph of theory.md, stripped of markdown symbols
    const paragraphs = theoryContent.split('\n\n');
    let firstBodyParagraph = paragraphs.find(p => !p.trim().startsWith('#')) || paragraphs[0];
    const excerpt = firstBodyParagraph
        .replace(/[#*`]/g, '')
        .replace(/\[(.*?)\]\(.*?\)/g, '$1') // Remove links but keep text
        .trim();


    // Convert month name to number for Date object
    const monthMap: { [key: string]: number } = {
        'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5,
        'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 11
    };

    const date = new Date(parseInt(year), monthMap[actualMonth || month] || 0, parseInt(day));

    const slugifiedTitle = meta.title
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)/g, '');

    return {
        year,
        month,
        day,
        slug: `${year}/${month.toLowerCase()}/${day}/${slugifiedTitle}`,
        meta,
        theory: theoryContent,
        math: mathContent,
        code: cleanCode,
        explanation,
        excerpt,
        date,
    };
}

export async function getAllEntries(): Promise<LearningEntry[]> {
    const years = fs.readdirSync(learningDirectory).filter(f => fs.statSync(path.join(learningDirectory, f)).isDirectory());
    const entries: LearningEntry[] = [];

    for (const year of years) {
        const months = fs.readdirSync(path.join(learningDirectory, year)).filter(f => fs.statSync(path.join(learningDirectory, year, f)).isDirectory());
        for (const month of months) {
            const days = fs.readdirSync(path.join(learningDirectory, year, month)).filter(f => fs.statSync(path.join(learningDirectory, year, month, f)).isDirectory());
            for (const day of days) {
                const entry = await getEntry(year, month, day);
                if (entry) entries.push(entry);
            }
        }
    }

    // Sort newest first
    return entries.sort((a, b) => b.date.getTime() - a.date.getTime());
}

export function groupEntriesByWeek(entries: LearningEntry[]) {
    const weeksMap: { [weekKey: string]: { range: string; days: LearningEntry[] } } = {};

    entries.forEach(entry => {
        // Calculate week range
        const d = new Date(entry.date);
        const day = d.getDay(); // 0 (Sun) to 6 (Sat)
        const diffToSun = d.getDate() - day;
        const sun = new Date(new Date(d).setDate(diffToSun));
        const sat = new Date(new Date(d).setDate(diffToSun + 6));

        const monthShort = (date: Date) => date.toLocaleString('en-US', { month: 'short' });
        const weekKey = `${sun.toISOString().split('T')[0]}_${sat.toISOString().split('T')[0]}`;
        const weekRange = `${monthShort(sun)} ${sun.getDate()} — ${monthShort(sat)} ${sat.getDate()}`;

        if (!weeksMap[weekKey]) {
            weeksMap[weekKey] = { range: weekRange, days: [] };
        }
        weeksMap[weekKey].days.push(entry);
    });

    // Sort weeks descending
    return Object.keys(weeksMap)
        .sort((a, b) => b.localeCompare(a))
        .map(weekKey => ({
            id: weekKey,
            weekRange: weeksMap[weekKey].range,
            days: weeksMap[weekKey].days.sort((a, b) => b.date.getTime() - a.date.getTime()),
            // Store the month/year of the first day for grouping later
            monthKey: `${weeksMap[weekKey].days[0].month} ${weeksMap[weekKey].days[0].year}`
        }));
}

export type WeekData = ReturnType<typeof groupEntriesByWeek>[number];

export function groupWeeksByMonth(weeks: WeekData[]): GroupedEntries[] {
    const grouped: { [monthKey: string]: GroupedEntries } = {};

    weeks.forEach(week => {
        if (!grouped[week.monthKey]) {
            grouped[week.monthKey] = { month: week.monthKey, weeks: [] };
        }
        grouped[week.monthKey].weeks.push(week);
    });

    return Object.values(grouped);
}

export async function getAdjacentEntries(currentDate: Date) {
    const entries = await getAllEntries();
    const sorted = entries.sort((a, b) => a.date.getTime() - b.date.getTime()); // Ascending for easier index finding

    const currentIndex = sorted.findIndex(e => e.date.getTime() === currentDate.getTime());

    if (currentIndex === -1) return { prev: null, next: null };

    return {
        prev: currentIndex > 0 ? sorted[currentIndex - 1] : null,
        next: currentIndex < sorted.length - 1 ? sorted[currentIndex + 1] : null,
    };
}
