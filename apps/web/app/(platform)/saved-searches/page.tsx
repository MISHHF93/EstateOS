import { Badge } from '@/components/ui/badge';
import { PlatformPageTemplate } from '@/components/platform/page-template';

const searches = [
  ['Portugal value-add', 'Lisbon, Porto · €700k–€1.5M · RBI optionality'],
  ['Dubai income assets', 'Marina, Downtown · $1M–$3M · Yield > 6%'],
  ['Family residency pathways', 'Greece, Portugal, UAE · Multilingual advisor handoff'],
];

export default function SavedSearchesPage() {
  return (
    <PlatformPageTemplate eyebrow="Saved searches" title="Reusable discovery workflows" description="Saved searches preserve filters, alerts, multilingual presentation, and MoE recommendation preferences across teams.">
      <div className="space-y-4">
        {searches.map(([title, description]) => (
          <div key={title} className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
            <div className="flex items-center justify-between gap-4">
              <div>
                <h3 className="font-medium text-white">{title}</h3>
                <p className="mt-1 text-sm text-slate-300">{description}</p>
              </div>
              <Badge>Alert enabled</Badge>
            </div>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
