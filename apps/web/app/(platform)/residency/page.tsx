import { PlatformPageTemplate } from '@/components/platform/page-template';

export default function ResidencyPage() {
  return (
    <PlatformPageTemplate eyebrow="Residency-by-investment" title="Eligibility orchestration" description="Guide applicants through program comparison, suitability scoring, document preparation, and advisor escalation with localized content and clear policy boundaries.">
      <div className="space-y-4 text-sm text-slate-300">
        <p>Program comparison cards, family eligibility summaries, source-of-funds readiness, and evidence requirements are scaffolded for OpenAPI-backed residency services.</p>
        <p>The page reserves space for multilingual summaries, timeline estimators, and explicit human-review gates when automated confidence is low.</p>
      </div>
    </PlatformPageTemplate>
  );
}
