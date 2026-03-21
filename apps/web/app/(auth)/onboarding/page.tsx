import { PageShell } from '@/components/layout/page-shell';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { SectionHeading } from '@/components/ui/section-heading';

export default function OnboardingPage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Onboarding" title="Progressive profile and trust setup" description="Collect investment goals, residency interests, insurance constraints, languages, and communication preferences through accessible, step-based forms." />
      <Card className="space-y-4">
        <div className="flex gap-2"><Badge intent="success">ISO 27701 ready</Badge><Badge>Consent capture</Badge><Badge>Role-aware prompts</Badge></div>
        <div className="grid gap-4 md:grid-cols-2">
          <Input placeholder="Preferred markets" aria-label="Preferred markets" />
          <Input placeholder="Target return profile" aria-label="Target return profile" />
          <Input placeholder="Residency goal" aria-label="Residency goal" />
          <Input placeholder="Preferred language" aria-label="Preferred language" />
        </div>
      </Card>
    </PageShell>
  );
}
