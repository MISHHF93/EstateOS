import { PageShell } from '@/components/layout/page-shell';
import { SectionHeading } from '@/components/ui/section-heading';
import { Card } from '@/components/ui/card';

export default function MarketingResidencyPage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Residency" title="Residency-by-investment journeys with human oversight" description="Explain programs, timelines, and evidence requirements in plain language before users enter protected workflows." />
      <Card>
        <p className="text-sm text-slate-300">Marketing content hands off to structured eligibility workflows, advisor scheduling, and document intake without overpromising automated outcomes.</p>
      </Card>
    </PageShell>
  );
}
