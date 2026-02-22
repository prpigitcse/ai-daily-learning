interface ExplanationBlockProps {
    explanation: string;
}

export function ExplanationBlock({ explanation }: ExplanationBlockProps) {
    return (
        <div className="grid grid-cols-1 gap-6 mt-8">
            <h3 className="text-xs font-bold uppercase tracking-widest text-muted flex items-center gap-2">
                Logic Breakdown
            </h3>

            <div
                className="space-y-4 text-sm text-foreground logic-breakdown"
                dangerouslySetInnerHTML={{ __html: explanation }}
            />
        </div>
    );
}
