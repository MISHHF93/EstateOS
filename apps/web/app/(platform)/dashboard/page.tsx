import { DashboardOverview } from '@/components/platform/dashboard-overview';
import { PageShell } from '@/components/layout/page-shell';
import { SectionHeading } from '@/components/ui/section-heading';

export default function DashboardPage() {
  return (
    <PageShell>
      <SectionHeading eyebrow="Dashboard" title="Role-aware operating workspace" description="Coordinate recommendations, listings, deal stages, compliance tasks, insurance actions, and payment holds from one unified command center." />
      <DashboardOverview />
    </PageShell>
  );
}
