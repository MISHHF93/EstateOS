import { Badge } from '@/components/ui/badge';
import { PlatformPageTemplate } from '@/components/platform/page-template';

const cases = [
  ['CASE-2041', 'Beneficiary mismatch', 'danger'],
  ['CASE-2038', 'Enhanced due diligence', 'warning'],
  ['CASE-2032', 'Release approved', 'success'],
] as const;

export default function AdminCompliancePage() {
  return (
    <PlatformPageTemplate eyebrow="Admin + compliance" title="Operational governance console" description="Expose queues, evidence packs, AI explanations, and release controls for brokers, administrators, and compliance officers.">
      <div className="space-y-4">
        {cases.map(([id, title, intent]) => (
          <div key={id} className="flex flex-col gap-3 rounded-2xl border border-white/10 bg-slate-950/40 p-4 md:flex-row md:items-center md:justify-between">
            <div>
              <p className="text-xs uppercase tracking-[0.2em] text-slate-500">{id}</p>
              <h3 className="font-medium text-white">{title}</h3>
            </div>
            <Badge intent={intent}>{intent}</Badge>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
