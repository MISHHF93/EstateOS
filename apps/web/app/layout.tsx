import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import './globals.css';
import { AppProvider } from '@/providers/app-provider';

export const metadata: Metadata = {
  title: 'EstateOS Web',
  description: 'Production-grade frontend scaffold for an AI-native real estate operating system.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AppProvider>{children}</AppProvider>
      </body>
    </html>
  );
}
