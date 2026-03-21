import type { ReactNode } from 'react';
import { QueryProvider } from '@/providers/query-provider';

export function AppProvider({ children }: { children: ReactNode }) {
  return <QueryProvider>{children}</QueryProvider>;
}
