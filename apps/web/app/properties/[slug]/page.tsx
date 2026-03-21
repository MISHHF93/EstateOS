import { notFound } from 'next/navigation';
import { PageShell } from '@/components/layout/page-shell';
import { AiInsightPanel } from '@/components/platform/ai-insight-panel';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { SectionHeading } from '@/components/ui/section-heading';
import { aiInsights, listings } from '@/lib/mocks/platform-data';

export default async function ListingDetailsPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const listing = listings.find((item) => item.slug === slug);

  if (!listing) notFound();

  return (
    <PageShell>
      <SectionHeading eyebrow="Listing details" title={listing.title} description={`${listing.city}, ${listing.country} · ${listing.summary}`} />
      <section className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
        <Card className="space-y-4">
          <div className="flex flex-wrap gap-2">{listing.tags.map((tag) => <Badge key={tag}>{tag}</Badge>)}</div>
          <div className="grid gap-4 md:grid-cols-3">
            <div><p className="text-sm text-slate-400">Purchase price</p><p className="text-2xl font-semibold text-white">{listing.price}</p></div>
            <div><p className="text-sm text-slate-400">Projected IRR</p><p className="text-2xl font-semibold text-white">{listing.irr}</p></div>
            <div><p className="text-sm text-slate-400">Projected yield</p><p className="text-2xl font-semibold text-white">{listing.yield}</p></div>
          </div>
          <p className="text-sm text-slate-300">The scaffold reserves space for image galleries, maps, document rooms, due diligence packs, pricing waterfalls, and localized legal disclosures.</p>
        </Card>
        <AiInsightPanel insights={aiInsights.slice(0, 2)} />
      </section>
    </PageShell>
  );
}
