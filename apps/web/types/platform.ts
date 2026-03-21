export type UserRole = 'guest' | 'buyer' | 'investor' | 'advisor' | 'admin' | 'compliance';

export interface NavigationItem {
  label: string;
  href: string;
  description: string;
  roles: UserRole[];
}

export interface InsightCard {
  title: string;
  expert: string;
  summary: string;
  confidence: string;
  severity: 'informational' | 'attention' | 'critical';
}

export interface Metric {
  label: string;
  value: string;
  trend: string;
}

export interface WorkflowStep {
  title: string;
  status: 'done' | 'current' | 'upcoming' | 'blocked';
  owner: string;
  description: string;
}

export interface Listing {
  id: string;
  slug: string;
  title: string;
  city: string;
  country: string;
  price: string;
  irr: string;
  yield: string;
  summary: string;
  tags: string[];
}
