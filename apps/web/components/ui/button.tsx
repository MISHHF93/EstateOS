import Link from 'next/link';
import type { AnchorHTMLAttributes, ButtonHTMLAttributes, ReactNode } from 'react';
import { cn } from '@/lib/utils/cn';

const styles = {
  primary: 'bg-accent text-slate-950 hover:bg-teal-300',
  secondary: 'border border-white/15 bg-white/5 hover:bg-white/10',
  ghost: 'hover:bg-white/10',
};

interface CommonProps {
  children: ReactNode;
  variant?: keyof typeof styles;
  className?: string;
}

export function Button({ children, variant = 'primary', className, ...props }: CommonProps & ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={cn('inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent', styles[variant], className)}
      {...props}
    >
      {children}
    </button>
  );
}

export function ButtonLink({ children, variant = 'primary', className, ...props }: CommonProps & AnchorHTMLAttributes<HTMLAnchorElement> & { href: string }) {
  return (
    <Link
      className={cn('inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent', styles[variant], className)}
      {...props}
    >
      {children}
    </Link>
  );
}
