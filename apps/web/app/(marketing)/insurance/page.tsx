import { PageShell } from '@/components/layout/page-shell';
import { SectionHeading } from '@/components/ui/section-heading';
import { Card } from '@/components/ui/card';

export default function MarketingInsurancePage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Insurance" title="Property and transaction protection flows" description="Set user expectations for underwriting inputs, quote comparisons, and bind steps with transparent caveats and coverage language." />
      <Card>
        <p className="text-sm text-slate-300">This scaffold keeps educational content and sensitive bind/payment interactions separated to support trust and regulatory boundaries.</p>
      </Card>
    </PageShell>
  );
}
