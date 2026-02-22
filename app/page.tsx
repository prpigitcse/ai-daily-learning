import { getAllEntries, groupEntries } from "@/lib/parser";
import { TimelineMonth } from "@/components/timeline/TimelineMonth";

export default async function Home() {
  const entries = await getAllEntries();
  const grouped = groupEntries(entries);

  return (
    <div id="log-container" className="space-y-12">
      {grouped.map((monthData, idx) => (
        <TimelineMonth
          key={idx}
          month={monthData.month}
          weeks={monthData.weeks}
        />
      ))}

      {entries.length === 0 && (
        <div className="text-center py-24">
          <p className="text-zinc-400 italic">No entries found yet. Keep learning!</p>
        </div>
      )}
    </div>
  );
}
