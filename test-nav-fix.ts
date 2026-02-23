import { getEntry, getAdjacentEntries, getAllEntries } from './lib/parser';

async function test() {
    console.log("Testing navigation logic...");

    // Test getEntry with lowercase month (as in URL)
    const year = "2026";
    const month = "february";
    const day = "23";

    const entry = await getEntry(year, month, day);
    if (entry) {
        console.log(`✅ Found entry for ${year}/${month}/${day}: ${entry.meta.title}`);
        console.log(`   Date: ${entry.date.toISOString()}`);

        const adjacency = await getAdjacentEntries(entry.date);
        console.log("Adjacency results:");
        console.log(`- Prev: ${adjacency.prev ? adjacency.prev.meta.title : 'null'}`);
        console.log(`- Next: ${adjacency.next ? adjacency.next.meta.title : 'null'}`);

        if (adjacency.prev || adjacency.next) {
            console.log("✅ Navigation links found!");
        } else {
            console.log("❌ No navigation links found (check if other entries exist)");
        }
    } else {
        console.log(`❌ Could not find entry for ${year}/${month}/${day}`);
    }

    const all = await getAllEntries();
    console.log(`Total entries: ${all.length}`);
}

test().catch(console.error);
