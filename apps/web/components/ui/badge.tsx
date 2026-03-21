import type { ReactNode } from 'react';
import { cn } from '@/lib/utils/cn';

export function Badge({ children, intent = 'default' }: { children: ReactNode; intent?: 'default' | 'success' | 'warning' | 'danger' }) {
  const intentStyles = {
    default: 'bg-white/10 text-slate-200',
    success: 'bg-emerald-500/15 text-emerald-200',
    warning: 'bg-amber-500/15 text-amber-200',
    danger: 'bg-orange-500/15 text-orange-200',
  } as const;

  return <span className={cn('inline-flex rounded-full px-3 py-1 text-xs font-medium', intentStyles[intent])}>{children}</span>;
}
