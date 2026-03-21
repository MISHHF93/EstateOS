import { ProgressSteps } from '@/components/ui/progress-steps';
import { PlatformPageTemplate } from '@/components/platform/page-template';
import { workflow } from '@/lib/mocks/platform-data';

export default async function DealRoomPage({ params }: { params: Promise<{ dealId: string }> }) {
  const { dealId } = await params;

  return (
    <PlatformPageTemplate eyebrow="Deal room" title={`Transaction control room · ${dealId}`} description="Track milestones, participants, approvals, conditions, and document requests with real-time AI-assisted exception handling.">
      <ProgressSteps steps={workflow} />
    </PlatformPageTemplate>
  );
}
