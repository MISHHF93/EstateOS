import type { UserRole } from '@/types/platform';

export interface SessionUser {
  name: string;
  email: string;
  role: UserRole;
  locale: 'en' | 'ar';
}

export const demoSession: SessionUser = {
  name: 'Nadia Rahman',
  email: 'nadia@estateos.ai',
  role: 'investor',
  locale: 'en',
};

export function getSecureSessionCookieName() {
  return '__Secure-estateos.session';
}
