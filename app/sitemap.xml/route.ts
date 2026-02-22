import { getAllEntries } from "@/lib/parser";

export async function GET() {
    const entries = await getAllEntries();
    const baseUrl = "https://ai.ppradosh.com";

    const staticPages = [
        "",
        "/privacy",
        "/sitemap",
    ];

    const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  ${staticPages
            .map((page) => `
  <url>
    <loc>${baseUrl}${page}</loc>
    <changefreq>daily</changefreq>
    <priority>${page === "" ? "1.0" : "0.8"}</priority>
  </url>`)
            .join("")}
  ${entries
            .map((entry) => `
  <url>
    <loc>${baseUrl}/${entry.slug}</loc>
    <lastmod>${entry.date.toISOString().split("T")[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>`)
            .join("")}
</urlset>`;

    return new Response(xml, {
        headers: {
            "Content-Type": "application/xml",
        },
    });
}
