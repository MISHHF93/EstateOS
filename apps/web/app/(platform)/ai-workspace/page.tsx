import { PlatformPageTemplate } from '@/components/platform/page-template';
import { openApiCatalog } from '@/lib/api/openapi';

export default function AiWorkspacePage() {
  return (
    <PlatformPageTemplate eyebrow="AI workspace" title="MoE orchestration visibility" description="Inspect expert routing, confidence, evidence, and next-best-action recommendations before releasing guided decisions into downstream workflows.">
      <div className="space-y-4">
        {openApiCatalog.map((operation) => (
          <div key={operation.path} className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
            <p className="font-medium text-white">{operation.service}</p>
            <p className="mt-1 text-sm text-slate-300">{operation.summary}</p>
          </div>
        ))}
      </div>
    </PlatformPageTemplate>
  );
}
