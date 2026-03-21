import { AiInsightPanel } from '@/components/platform/ai-insight-panel';
import { ListingCard } from '@/components/platform/listing-card';
import { ProgressSteps } from '@/components/ui/progress-steps';
import { Card } from '@/components/ui/card';
import { aiInsights, listings, workflow } from '@/lib/mocks/platform-data';

export function DashboardOverview() {
  return (
    <section className="grid gap-6 xl:grid-cols-[1.4fr_0.9fr]">
      <div className="space-y-6">
        <AiInsightPanel insights={aiInsights} />
        <div className="grid gap-4 lg:grid-cols-2">
          {listings.slice(0, 2).map((listing) => <ListingCard key={listing.id} listing={listing} />)}
        </div>
      </div>
      <Card className="space-y-6">
        <div>
          <p className="text-sm uppercase tracking-[0.25em] text-slate-500">Deal progression</p>
          <h2 className="text-2xl font-semibold text-white">Transaction timeline</h2>
        </div>
        <ProgressSteps steps={workflow} />
      </Card>
    </section>
  );
}
