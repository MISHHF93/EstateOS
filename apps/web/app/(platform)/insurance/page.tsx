import { PlatformPageTemplate } from '@/components/platform/page-template';

export default function InsurancePage() {
  return (
    <PlatformPageTemplate eyebrow="Insurance journey" title="Coverage recommendation and bind workflow" description="Collect property and borrower signals, compare quote bundles, and explain exclusions, premiums, and bind requirements with insurer-ready document states.">
      <div className="space-y-4 text-sm text-slate-300">
        <p>Coverage cards, claim sensitivity explanations, and bind prerequisites are organized to support cross-border property and residency contexts.</p>
        <p>UI boundaries separate sensitive payment entry from quote review to preserve PCI-aligned checkout patterns.</p>
      </div>
    </PlatformPageTemplate>
  );
}
