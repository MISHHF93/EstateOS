import { Hero } from '@/components/marketing/hero';
import { ModuleGrid } from '@/components/platform/module-grid';
import { AiInsightPanel } from '@/components/platform/ai-insight-panel';
import { PageShell } from '@/components/layout/page-shell';
import { SectionHeading } from '@/components/ui/section-heading';
import { aiInsights } from '@/lib/mocks/platform-data';
import { openApiCatalog } from '@/lib/api/openapi';
import { Card } from '@/components/ui/card';

export default function HomePage() {
  return (
    <PageShell>
      <Hero />
      <section className="space-y-6">
        <SectionHeading
          eyebrow="Platform foundation"
          title="Scaffolded for public journeys, secure workspaces, and governed AI outputs."
          description="This starter organizes marketing surfaces, authenticated application flows, analytics, transactions, compliance, and notifications into a cohesive Next.js App Router architecture ready to consume OpenAPI services."
        />
        <ModuleGrid />
      </section>
      <section className="grid gap-6 xl:grid-cols-[1fr_1fr]">
        <AiInsightPanel insights={aiInsights} />
        <Card className="space-y-4">
          <SectionHeading
            eyebrow="API integration"
            title="OpenAPI-driven service catalog"
            description="Typed fetch wrappers and service descriptors make it straightforward to generate SDKs or bind to backend contracts as the modular monolith evolves into discrete services."
          />
          <div className="space-y-3">
            {openApiCatalog.map((operation) => (
              <div key={`${operation.service}-${operation.path}`} className="rounded-2xl border border-white/10 bg-slate-950/40 p-4 text-sm text-slate-300">
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <p className="font-medium text-white">{operation.service}</p>
                  <span className="rounded-full bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-accent">{operation.method}</span>
                </div>
                <p className="mt-2 font-mono text-xs text-slate-400">{operation.path}</p>
                <p className="mt-2">{operation.summary}</p>
              </div>
            ))}
          </div>
        </Card>
      </section>
    </PageShell>
  );
}
