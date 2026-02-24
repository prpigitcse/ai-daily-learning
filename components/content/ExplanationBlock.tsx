interface ExplanationBlockProps {
    explanation: string;
}

export function ExplanationBlock({ explanation }: ExplanationBlockProps) {
    return (
        <div className="grid grid-cols-1 gap-6 mt-8">
            <h3 className="text-xs font-bold uppercase tracking-widest text-muted flex items-center gap-2">
                Code Breakdown
            </h3>

            <div className="rounded-xl border border-card-border bg-card p-6">
                <div
                    className="space-y-4 text-sm text-muted logic-breakdown markdown-content"
                    dangerouslySetInnerHTML={{ __html: explanation }}
                />
            </div>
        </div>
    );
}
