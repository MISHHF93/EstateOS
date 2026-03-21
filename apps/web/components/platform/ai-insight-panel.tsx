import { AlertTriangle, CheckCircle2, Siren } from 'lucide-react';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import type { InsightCard } from '@/types/platform';

const severityConfig = {
  informational: { icon: CheckCircle2, badge: 'success' as const, label: 'Release ready' },
  attention: { icon: AlertTriangle, badge: 'warning' as const, label: 'Needs review' },
  critical: { icon: Siren, badge: 'danger' as const, label: 'Hold' },
};

export function AiInsightPanel({ insights }: { insights: InsightCard[] }) {
  return (
    <Card className="space-y-5">
      <div className="flex items-center justify-between gap-4">
        <div>
          <p className="text-sm uppercase tracking-[0.25em] text-slate-500">Mixture-of-Experts</p>
          <h2 className="text-2xl font-semibold text-white">Explainable AI guidance</h2>
        </div>
        <Badge>Governed release</Badge>
      </div>
      <div className="space-y-4">
        {insights.map((insight) => {
          const config = severityConfig[insight.severity];
          const Icon = config.icon;
          return (
            <div key={insight.title} className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div className="space-y-2">
                  <div className="flex items-center gap-2 text-white">
                    <Icon className="h-4 w-4 text-accent" />
                    <h3 className="font-medium">{insight.title}</h3>
                  </div>
                  <p className="text-sm text-slate-300">{insight.summary}</p>
                </div>
                <div className="space-y-2 text-right">
                  <Badge intent={config.badge}>{config.label}</Badge>
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">{insight.expert}</p>
                  <p className="text-xs text-slate-400">Confidence {insight.confidence}</p>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </Card>
  );
}
