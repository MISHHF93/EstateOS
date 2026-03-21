import { PlatformPageTemplate } from '@/components/platform/page-template';

const notifications = [
  ['Compliance review update', 'Source-of-funds package moved to reviewer queue.'],
  ['Valuation refresh', 'Market forecast expert refreshed Lisbon rental assumptions.'],
  ['Insurance quote ready', 'Carrier bundle available for review and bind.'],
];

export default function NotificationsPage() {
  return (
    <PlatformPageTemplate eyebrow="Notifications" title="Cross-workflow alerts and nudges" description="Bring together transaction milestones, AI recommendations, missing documents, policy holds, and team messages with clear severity and action affordances.">
      <div className="space-y-4">
        {notifications.map(([title, body]) => (
          <div key={title} className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
            <h3 className="font-medium text-white">{title}</h3>
            <p className="mt-1 text-sm text-slate-300">{body}</p>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
