import { Badge } from '@/components/ui/badge';
import { PlatformPageTemplate } from '@/components/platform/page-template';

const docs = [
  ['Passport copy', 'Uploaded', 'OCR complete · awaiting sanctions check'],
  ['Source of funds letter', 'Review', 'Missing notarization metadata'],
  ['Title deed', 'Ready', 'Validated against listing-service packet'],
  ['Insurance schedule', 'Pending', 'Carrier response expected within 2h'],
];

export default function DocumentsPage() {
  return (
    <PlatformPageTemplate eyebrow="Documents" title="Secure upload and review flows" description="Segment document handling into governed stages spanning upload, extraction, review, compliance, and release decisions.">
      <div className="space-y-4">
        {docs.map(([title, status, note]) => (
          <div key={title} className="flex flex-col gap-3 rounded-2xl border border-white/10 bg-slate-950/40 p-4 md:flex-row md:items-center md:justify-between">
            <div>
              <h3 className="font-medium text-white">{title}</h3>
              <p className="text-sm text-slate-300">{note}</p>
            </div>
            <Badge intent={status === 'Ready' || status === 'Uploaded' ? 'success' : status === 'Review' ? 'warning' : 'default'}>{status}</Badge>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
