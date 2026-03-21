import { PageShell } from '@/components/layout/page-shell';
import { ListingCard } from '@/components/platform/listing-card';
import { SectionHeading } from '@/components/ui/section-heading';
import { Input } from '@/components/ui/input';
import { listings } from '@/lib/mocks/platform-data';

export default function SearchPage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Search and discovery" title="AI-guided property discovery" description="Search inventory, compare ROI, and surface MoE recommendations with transparent underwriting and policy context." />
      <div className="grid gap-4 rounded-3xl border border-white/10 bg-white/5 p-6 lg:grid-cols-4">
        <Input placeholder="City, neighborhood, or residency market" aria-label="Search location" />
        <Input placeholder="Budget range" aria-label="Budget range" />
        <Input placeholder="Target IRR or yield" aria-label="Target returns" />
        <Input placeholder="Residency or insurance filter" aria-label="Residency filter" />
      </div>
      <section className="grid gap-4 xl:grid-cols-3">
        {listings.map((listing) => <ListingCard key={listing.id} listing={listing} />)}
      </section>
    </PageShell>
  );
}
