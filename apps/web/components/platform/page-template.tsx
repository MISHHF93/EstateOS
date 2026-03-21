import type { ReactNode } from 'react';
import { PageShell } from '@/components/layout/page-shell';
import { AiInsightPanel } from '@/components/platform/ai-insight-panel';
import { Card } from '@/components/ui/card';
import { SectionHeading } from '@/components/ui/section-heading';
import { aiInsights } from '@/lib/mocks/platform-data';

export function PlatformPageTemplate({ eyebrow, title, description, children }: { eyebrow: string; title: string; description: string; children: ReactNode }) {
  return (
    <PageShell>
      <SectionHeading eyebrow={eyebrow} title={title} description={description} />
      <section className="grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
        <Card className="space-y-5">{children}</Card>
        <AiInsightPanel insights={aiInsights} />
      </section>
    </PageShell>
  );
}
