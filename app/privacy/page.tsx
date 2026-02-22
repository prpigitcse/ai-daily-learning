import { ArticleSection } from "@/components/content/ArticleSection";

export const metadata = {
    title: "Privacy Policy — AI Logbook",
    description: "Privacy policy and analytics disclosure for AI Logbook.",
};

export default function PrivacyPage() {
    return (
        <article>
            <ArticleSection title="Privacy Policy">
                <div className="space-y-6 text-zinc-600">
                    <p>
                        At AI Logbook, we value your privacy. This page explains how we handle data and what services we use.
                    </p>

                    <h3 className="text-zinc-900 font-semibold text-lg">Analytics Disclosure</h3>
                    <p>
                        We use <strong>Vercel Analytics</strong> and <strong>Vercel Speed Insights</strong> to understand how our visitors interact with the site and to monitor performance. This helps us improve the user experience and ensure the site remains fast and accessible.
                    </p>
                    <p>
                        These tools collect anonymous information such as:
                    </p>
                    <ul className="list-disc pl-6 space-y-2">
                        <li>Page views and visit duration</li>
                        <li>Browser type and device category</li>
                        <li>Referral sources</li>
                        <li>General geographic location (country/region level)</li>
                    </ul>

                    <h3 className="text-zinc-900 font-semibold text-lg">Cookies</h3>
                    <p>
                        We do not use tracking cookies for advertising. Vercel's analytics are privacy-focused and do not track individual users across different websites.
                    </p>

                    <h3 className="text-zinc-900 font-semibold text-lg">Data Usage</h3>
                    <p>
                        No personal information (like names or email addresses) is collected unless explicitly provided by you (e.g., if we add a newsletter in the future). Currently, the site is purely informational.
                    </p>

                    <p className="pt-4 text-sm italic">
                        Last updated: February 22, 2026
                    </p>
                </div>
            </ArticleSection>
        </article>
    );
}
