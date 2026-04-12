import { notFound } from "next/navigation";
import {
  getAllEntries,
  groupEntriesByWeek,
  groupWeeksByMonth,
} from "@/lib/parser";
import { TimelineMonth } from "@/components/timeline/TimelineMonth";
import { Pagination } from "@/components/ui/Pagination";

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const { page } = await searchParams;
  const currentPage = parseInt(page || "1", 10);
  const weeksPerPage = 2;

  const entries = await getAllEntries();
  const allWeeks = groupEntriesByWeek(entries);
  const totalPages = Math.ceil(allWeeks.length / weeksPerPage);

  const isValidPage = !page || /^[1-9]\d*$/.test(page);
  const noEntries = allWeeks.length === 0;
  if (
    !isValidPage ||
    currentPage < 1 ||
    (noEntries ? currentPage > 1 : currentPage > totalPages)
  ) {
    notFound();
  }

  const startIndex = (currentPage - 1) * weeksPerPage;
  const endIndex = startIndex + weeksPerPage;
  const paginatedWeeks = allWeeks.slice(startIndex, endIndex);
  const hasMore = allWeeks.length > endIndex;

  const grouped = groupWeeksByMonth(paginatedWeeks);

  const prevWeek = currentPage > 1 ? allWeeks[startIndex - 1] : null;
  const nextWeek = hasMore ? allWeeks[endIndex] : null;

  return (
    <div className="relative space-y-12">
      <div className="flex justify-center items-center gap-3 flex-wrap">
        <a
          href="https://github.com/prpigitcse/ai-daily-learning"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="13"
            height="13"
            viewBox="0 0 24 24"
            fill="currentColor"
          >
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23A11.51 11.51 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.29-1.552 3.297-1.23 3.297-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12" />
          </svg>
          GitHub
        </a>
        <a
          href="https://github.com/prpigitcse/ai-daily-learning/issues"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="13"
            height="13"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
          </svg>
          Issues
        </a>
        <a
          href="https://github.com/prpigitcse/ai-daily-learning/discussions"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="13"
            height="13"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
          Discussions
        </a>
      </div>

      {totalPages > 1 && (
        <div className="flex justify-center border-b border-card-border pb-10">
          <Pagination
            prev={
              prevWeek
                ? {
                    href: `/?page=${currentPage - 1}`,
                    label: prevWeek.weekRange,
                  }
                : null
            }
            next={
              nextWeek
                ? {
                    href: `/?page=${currentPage + 1}`,
                    label: nextWeek.weekRange,
                  }
                : null
            }
            currentPage={currentPage}
            totalPages={totalPages}
          />
        </div>
      )}

      <div id="log-container" className="space-y-12 pb-12">
        {grouped.map((monthData, idx) => (
          <TimelineMonth
            key={idx}
            month={monthData.month}
            weeks={monthData.weeks}
          />
        ))}

        {entries.length === 0 && (
          <div className="text-center py-24">
            <p className="text-muted italic">
              No entries found yet. Keep learning!
            </p>
          </div>
        )}
      </div>

      {totalPages > 1 && (
        <div className="flex justify-center border-t border-card-border pt-12">
          <Pagination
            prev={
              prevWeek
                ? {
                    href: `/?page=${currentPage - 1}`,
                    label: prevWeek.weekRange,
                  }
                : null
            }
            next={
              nextWeek
                ? {
                    href: `/?page=${currentPage + 1}`,
                    label: nextWeek.weekRange,
                  }
                : null
            }
            currentPage={currentPage}
            totalPages={totalPages}
          />
        </div>
      )}
    </div>
  );
}
