import { Badge } from '@/components/ui/badge';
import { PlatformPageTemplate } from '@/components/platform/page-template';

export default function PaymentsPage() {
  return (
    <PlatformPageTemplate eyebrow="Payments and checkout" title="Escrow-aware payment experience" description="Use segmented checkout surfaces for reservation fees, escrow deposits, and insurance premiums while exposing fraud/compliance holds in plain language.">
      <div className="space-y-4">
        <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-5">
          <p className="text-sm text-slate-400">Next payment</p>
          <p className="mt-2 text-3xl font-semibold text-white">$125,000 reservation deposit</p>
          <p className="mt-2 text-sm text-slate-300">Tokenized payment intent, escrow beneficiary verification, and fraud checks remain outside the primary marketing shell.</p>
        </div>
        <div className="flex gap-2"><Badge intent="warning">Manual release required</Badge><Badge>PCI-segmented UI zone</Badge></div>
      </div>
    </PlatformPageTemplate>
  );
}
