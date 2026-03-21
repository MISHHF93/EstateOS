import { PageShell } from '@/components/layout/page-shell';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { SectionHeading } from '@/components/ui/section-heading';

export default function SignInPage() {
  return (
    <PageShell>
      <div className="mx-auto w-full max-w-xl">
        <Card className="space-y-6">
          <SectionHeading eyebrow="Authentication" title="Secure session initiation" description="Sign in with enterprise-grade session handling, MFA-ready controls, and redirect-safe route protection." />
          <div className="space-y-4">
            <Input type="email" placeholder="name@company.com" aria-label="Email address" />
            <Input type="password" placeholder="••••••••" aria-label="Password" />
            <Button className="w-full">Continue to workspace</Button>
          </div>
        </Card>
      </div>
    </PageShell>
  );
}
