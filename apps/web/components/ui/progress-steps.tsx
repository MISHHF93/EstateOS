import { Badge } from '@/components/ui/badge';
import type { WorkflowStep } from '@/types/platform';

export function ProgressSteps({ steps }: { steps: WorkflowStep[] }) {
  return (
    <ol className="space-y-4">
      {steps.map((step, index) => (
        <li key={step.title} className="flex gap-4 rounded-2xl border border-white/10 bg-slate-950/40 p-4">
          <div className="flex h-8 w-8 items-center justify-center rounded-full border border-white/10 bg-white/5 text-sm font-semibold text-white">{index + 1}</div>
          <div className="space-y-2">
            <div className="flex flex-wrap items-center gap-3">
              <h3 className="font-medium text-white">{step.title}</h3>
              <Badge intent={step.status === 'done' ? 'success' : step.status === 'blocked' ? 'danger' : step.status === 'current' ? 'warning' : 'default'}>{step.status}</Badge>
            </div>
            <p className="text-sm text-slate-300">{step.description}</p>
            <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Owner · {step.owner}</p>
          </div>
        </li>
      ))}
    </ol>
  );
}
