import { PlatformPageTemplate } from '@/components/platform/page-template';

const panels = [
  ['Portfolio IRR', '18.1%', 'Consolidated target-adjusted IRR across shortlisted markets.'],
  ['Risk-adjusted yield', '6.4%', 'Net operating forecast with insurance and tax assumptions.'],
  ['Valuation drift', '+2.8%', 'MoE valuation expert indicates upside versus purchase basis.'],
  ['Market momentum', '74 / 100', 'Macro and liquidity pulse derived from market forecast signals.'],
];

export default function AnalyticsPage() {
  return (
    <PlatformPageTemplate eyebrow="Investor analytics" title="Decision-ready analytics" description="Surface valuation, ROI, market forecast, stress-testing, and diversification insights with explainable calculations and audit metadata.">
      <div className="grid gap-4 md:grid-cols-2">
        {panels.map(([title, value, description]) => (
          <div key={title} className="rounded-2xl border border-white/10 bg-slate-950/40 p-5">
            <p className="text-sm text-slate-400">{title}</p>
            <p className="mt-3 text-3xl font-semibold text-white">{value}</p>
            <p className="mt-2 text-sm text-slate-300">{description}</p>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
