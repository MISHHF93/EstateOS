import { BarChart3, Bell, Building2, CreditCard, FileText, Globe2, Heart, Home, Scale, Shield, Sparkles, UserRoundCheck } from 'lucide-react';
import { Card } from '@/components/ui/card';

const modules = [
  { icon: Home, title: 'Public marketing pages', description: 'Trust-forward product storytelling, conversion pathways, and multilingual content architecture.' },
  { icon: UserRoundCheck, title: 'Auth and onboarding', description: 'Secure session starts, identity capture, preferences, and progressive profile completion.' },
  { icon: Building2, title: 'Property discovery', description: 'Role-aware search, AI-guided filters, saved searches, and favorites orchestration.' },
  { icon: BarChart3, title: 'Investor analytics', description: 'Returns, stress tests, valuation, market forecasts, and portfolio diversification signals.' },
  { icon: FileText, title: 'Deal rooms and documents', description: 'Milestone tracking, document upload/review, and decision-ready checklists.' },
  { icon: Globe2, title: 'Residency + insurance', description: 'Eligibility journeys, insurance bind flows, and localized guidance.' },
  { icon: CreditCard, title: 'Payments and checkout', description: 'PCI-sensitive UI segmentation for reservation fees, escrow, and insurance payments.' },
  { icon: Sparkles, title: 'AI insight panels', description: 'Recommendations, valuation insights, fraud alerts, and next-best actions with confidence signals.' },
  { icon: Bell, title: 'Notifications', description: 'Cross-channel nudges, SLA alerts, release status, and exceptions.' },
  { icon: Scale, title: 'Admin / compliance portals', description: 'Audit evidence, screening reviews, and intervention workflows.' },
  { icon: Shield, title: 'Enterprise controls', description: 'Accessibility, privacy, auditability, and explainability woven into every surface.' },
  { icon: Heart, title: 'Human-centered UX', description: 'ISO 9241-210 aligned information architecture, plain language, and assisted decision support.' },
];

export function ModuleGrid() {
  return (
    <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      {modules.map(({ icon: Icon, title, description }) => (
        <Card key={title} className="space-y-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/10 bg-white/5 text-accent">
            <Icon className="h-5 w-5" />
          </div>
          <h3 className="text-lg font-semibold text-white">{title}</h3>
          <p className="text-sm text-slate-300">{description}</p>
        </Card>
      ))}
    </section>
  );
}
