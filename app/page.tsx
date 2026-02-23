import { getAllEntries, groupEntriesByWeek, groupWeeksByMonth } from "@/lib/parser";
import { TimelineMonth } from "@/components/timeline/TimelineMonth";
import { Pagination } from "@/components/ui/Pagination";

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const { page } = await searchParams;
  const currentPage = parseInt(page || "1");
  const weeksPerPage = 2;

  const entries = await getAllEntries();
  const allWeeks = groupEntriesByWeek(entries);
  const totalPages = Math.ceil(allWeeks.length / weeksPerPage);

  const startIndex = (currentPage - 1) * weeksPerPage;
  const endIndex = startIndex + weeksPerPage;
  const paginatedWeeks = allWeeks.slice(startIndex, endIndex);
  const hasMore = allWeeks.length > endIndex;

  const grouped = groupWeeksByMonth(paginatedWeeks);

  const prevWeek = currentPage > 1 ? allWeeks[startIndex - 1] : null;
  const nextWeek = hasMore ? allWeeks[endIndex] : null;

  return (
    <div className="relative flex flex-col md:flex-row gap-8">
      <div id="log-container" className="flex-grow space-y-12 pb-12">
        {grouped.map((monthData, idx) => (
          <TimelineMonth
            key={idx}
            month={monthData.month}
            weeks={monthData.weeks}
          />
        ))}

        {entries.length === 0 && (
          <div className="text-center py-24">
            <p className="text-muted italic">No entries found yet. Keep learning!</p>
          </div>
        )}
      </div>

      {totalPages > 1 && (
        <aside className="shrink-0 pt-2 flex flex-col justify-between pb-12">
          <div className="sticky top-24">
            <Pagination
              prev={prevWeek ? { href: `/?page=${currentPage - 1}`, label: prevWeek.weekRange } : null}
              next={nextWeek ? { href: `/?page=${currentPage + 1}`, label: nextWeek.weekRange } : null}
              currentPage={currentPage}
              totalPages={totalPages}
            />
          </div>
          <div className="sticky bottom-12">
            <Pagination
              prev={prevWeek ? { href: `/?page=${currentPage - 1}`, label: prevWeek.weekRange } : null}
              next={nextWeek ? { href: `/?page=${currentPage + 1}`, label: nextWeek.weekRange } : null}
              currentPage={currentPage}
              totalPages={totalPages}
            />
          </div>
        </aside>
      )}
    </div>
  );
}
