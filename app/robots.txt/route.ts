export async function GET() {
    const robots = `User-agent: *
Allow: /

Sitemap: https://ai.ppradosh.com/sitemap.xml
`;

    return new Response(robots, {
        headers: {
            "Content-Type": "text/plain",
        },
    });
}
