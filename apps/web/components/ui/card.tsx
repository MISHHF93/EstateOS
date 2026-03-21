import type { ReactNode } from 'react';
import { cn } from '@/lib/utils/cn';

export function Card({ children, className }: { children: ReactNode; className?: string }) {
  return <section className={cn('rounded-3xl border border-white/10 bg-white/5 p-6 shadow-glow backdrop-blur', className)}>{children}</section>;
}
