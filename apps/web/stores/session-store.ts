'use client';

import { create } from 'zustand';
import type { UserRole } from '@/types/platform';

type SessionState = {
  role: UserRole;
  locale: 'en' | 'ar';
  setRole: (role: UserRole) => void;
  setLocale: (locale: 'en' | 'ar') => void;
};

export const useSessionStore = create<SessionState>((set) => ({
  role: 'investor',
  locale: 'en',
  setRole: (role) => set({ role }),
  setLocale: (locale) => set({ locale }),
}));
