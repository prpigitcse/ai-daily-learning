import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { LearningEntry, MetaData } from './types';

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
    const entryPath = path.join(learningDirectory, year, month, day);

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

    const date = new Date(parseInt(year), monthMap[month] || 0, parseInt(day));

    return {
        year,
        month,
        day,
        slug: `${year}/${month}/${day}`,
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

export function groupEntries(entries: LearningEntry[]) {
    const grouped: { [monthKey: string]: { month: string; weeks: { [weekKey: string]: { range: string; days: LearningEntry[] } } } } = {};

    entries.forEach(entry => {
        const monthKey = `${entry.month} ${entry.year}`;
        if (!grouped[monthKey]) {
            grouped[monthKey] = { month: monthKey, weeks: {} };
        }

        // Calculate week range
        const d = new Date(entry.date);
        const day = d.getDay(); // 0 (Sun) to 6 (Sat)
        const diffToSun = d.getDate() - day;
        const sun = new Date(d.setDate(diffToSun));
        const sat = new Date(d.setDate(diffToSun + 6));

        const monthShort = (date: Date) => date.toLocaleString('en-US', { month: 'short' });
        const weekKey = `${sun.toISOString().split('T')[0]}_${sat.toISOString().split('T')[0]}`;
        const weekRange = `${monthShort(sun)} ${sun.getDate()} — ${monthShort(sat)} ${sat.getDate()}`;

        if (!grouped[monthKey].weeks[weekKey]) {
            grouped[monthKey].weeks[weekKey] = { range: weekRange, days: [] };
        }

        grouped[monthKey].weeks[weekKey].days.push(entry);
    });

    // Convert to array and sort
    return Object.values(grouped).map(m => ({
        month: m.month,
        weeks: Object.keys(m.weeks).sort((a, b) => b.localeCompare(a)).map(w => ({
            weekRange: m.weeks[w].range,
            days: m.weeks[w].days.sort((a, b) => b.date.getTime() - a.date.getTime())
        }))
    }));
}
