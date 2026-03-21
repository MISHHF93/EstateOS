import { PageShell } from '@/components/layout/page-shell';
import { SectionHeading } from '@/components/ui/section-heading';
import { Card } from '@/components/ui/card';

export default function InvestorsPage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Investors" title="Institutional clarity for investors and advisors" description="Present portfolio intelligence, scenario modeling, and diligence controls in a language suitable for family offices, private banks, and operators." />
      <Card>
        <p className="text-sm text-slate-300">The investor marketing layer can route into analytics, deal rooms, and AI valuation narratives while preserving trust messaging and auditability expectations.</p>
      </Card>
    </PageShell>
  );
}
