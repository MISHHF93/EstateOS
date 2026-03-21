import { ArrowRight, LockKeyhole, Sparkles } from 'lucide-react';
import { ButtonLink } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { metrics } from '@/lib/mocks/platform-data';

export function Hero() {
  return (
    <section className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
      <div className="space-y-6 rounded-[2rem] border border-white/10 bg-white/5 p-8 shadow-glow">
        <p className="inline-flex items-center gap-2 rounded-full border border-accent/20 bg-accent/10 px-4 py-2 text-sm text-accent">
          <Sparkles className="h-4 w-4" />
          AI-native operating system for property, capital, compliance, and residency journeys
        </p>
        <div className="space-y-4">
          <h1 className="max-w-4xl text-4xl font-semibold leading-tight text-white md:text-6xl">
            Build trusted, auditable, multilingual real estate workflows around a Mixture-of-Experts core.
          </h1>
          <p className="max-w-3xl text-lg text-slate-300">
            EstateOS unifies discovery, investor analytics, deal rooms, documents, residency programs, insurance, payments, and compliance into one enterprise-grade experience with explainable AI outputs and release controls.
          </p>
        </div>
        <div className="flex flex-wrap gap-3">
          <ButtonLink href="/dashboard">Launch workspace <ArrowRight className="ml-2 h-4 w-4" /></ButtonLink>
          <ButtonLink href="/search" variant="secondary">Explore portfolio inventory</ButtonLink>
        </div>
        <div className="grid gap-4 md:grid-cols-4">
          {metrics.map((metric) => (
            <Card key={metric.label} className="p-4">
              <p className="text-sm text-slate-400">{metric.label}</p>
              <p className="mt-2 text-2xl font-semibold text-white">{metric.value}</p>
              <p className="mt-1 text-xs text-accent">{metric.trend}</p>
            </Card>
          ))}
        </div>
      </div>
      <Card className="space-y-6">
        <div className="flex items-center gap-3 text-white">
          <LockKeyhole className="h-5 w-5 text-accent" />
          <h2 className="text-xl font-semibold">Trust architecture</h2>
        </div>
        <ul className="space-y-4 text-sm text-slate-300">
          <li>Role-aware navigation, secure session boundaries, and human approval gates for sensitive decisions.</li>
          <li>OpenAPI-driven service integration patterns for auth, listings, documents, payments, insurance, residency, and compliance.</li>
          <li>Accessibility-first interfaces tuned for ISO 9241-210 usability and ISO/IEC 25010 product quality attributes.</li>
          <li>Privacy-conscious UI patterns that support ISO/IEC 27001, ISO/IEC 27701, and PCI DSS-sensitive checkout experiences.</li>
        </ul>
      </Card>
    </section>
  );
}
