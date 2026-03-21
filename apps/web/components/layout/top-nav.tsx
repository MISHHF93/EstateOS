'use client';

import { Bell, Globe, ShieldCheck } from 'lucide-react';
import { roleNavigation } from '@/lib/mocks/platform-data';
import { useSessionStore } from '@/stores/session-store';
import { ButtonLink } from '@/components/ui/button';

export function TopNav() {
  const role = useSessionStore((state) => state.role);
  const locale = useSessionStore((state) => state.locale);
  const setLocale = useSessionStore((state) => state.setLocale);

  const navigation = roleNavigation.filter((item) => item.roles.includes(role) || item.roles.includes('guest'));

  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-surface/80 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-6 px-6 py-4">
        <div>
          <p className="text-lg font-semibold text-white">EstateOS</p>
          <p className="text-xs uppercase tracking-[0.3em] text-slate-500">MoE real estate command center</p>
        </div>
        <nav className="hidden items-center gap-2 lg:flex">
          {navigation.map((item) => (
            <ButtonLink key={item.href} href={item.href} variant="ghost" className="text-slate-300">
              {item.label}
            </ButtonLink>
          ))}
        </nav>
        <div className="flex items-center gap-2">
          <button aria-label="Switch locale" onClick={() => setLocale(locale === 'en' ? 'ar' : 'en')} className="rounded-full border border-white/10 p-2 text-slate-300 transition hover:bg-white/10">
            <Globe className="h-4 w-4" />
          </button>
          <button aria-label="View notifications" className="rounded-full border border-white/10 p-2 text-slate-300 transition hover:bg-white/10">
            <Bell className="h-4 w-4" />
          </button>
          <div className="flex items-center gap-2 rounded-full border border-emerald-400/15 bg-emerald-400/10 px-3 py-2 text-xs text-emerald-100">
            <ShieldCheck className="h-4 w-4" />
            ISO / PCI aligned
          </div>
        </div>
      </div>
    </header>
  );
}
