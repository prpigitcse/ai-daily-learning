import fs from 'fs';
import path from 'path';

const learningDirectory = path.join(process.cwd(), 'learning');

function walkEntries(dir: string): string[] {
    const results: string[] = [];
    if (!fs.existsSync(dir)) return results;

    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            // Check if it's a "day" directory (contains meta.md as a heuristic)
            if (fs.existsSync(path.join(fullPath, 'meta.md'))) {
                results.push(fullPath);
            } else {
                results.push(...walkEntries(fullPath));
            }
        }
    }
    return results;
}

function validateEntries() {
    console.log('🔍 Starting Data Integrity Validation...\n');
    const entryPaths = walkEntries(learningDirectory);
    const requiredFiles = ['meta.md', 'theory.md', 'math.md', 'code.py'];
    let errors = 0;

    for (const entryPath of entryPaths) {
        const relativePath = path.relative(learningDirectory, entryPath);
        const folderFiles = fs.readdirSync(entryPath);

        // 1. Check for required files
        for (const file of requiredFiles) {
            if (!folderFiles.includes(file)) {
                console.error(`❌ [${relativePath}] Missing required file: ${file}`);
                errors++;
            }
        }

        // 2. Check for docstring in code.py
        const codePath = path.join(entryPath, 'code.py');
        if (fs.existsSync(codePath)) {
            const content = fs.readFileSync(codePath, 'utf8');
            const docstringRegex = /^\s*"""([\s\S]*?)"""/;
            if (!docstringRegex.test(content)) {
                console.error(`❌ [${relativePath}] Missing logic breakdown docstring in code.py`);
                errors++;
            }
        }
    }

    if (errors > 0) {
        console.error(`\n🚨 Validation failed with ${errors} error(s). Please fix them before building.`);
        process.exit(1);
    } else {
        console.log(`\n✅ All ${entryPaths.length} entries passed validation.`);
    }
}

validateEntries();
