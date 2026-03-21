import type { ReactNode } from 'react';
import { TopNav } from '@/components/layout/top-nav';

export function PageShell({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-aurora">
      <TopNav />
      <main className="mx-auto flex max-w-7xl flex-col gap-10 px-6 py-10">{children}</main>
    </div>
  );
}
