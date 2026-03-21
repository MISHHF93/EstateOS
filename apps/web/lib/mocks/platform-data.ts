import type { InsightCard, Listing, Metric, NavigationItem, WorkflowStep } from '@/types/platform';

export const roleNavigation: NavigationItem[] = [
  { label: 'Home', href: '/', description: 'Marketing, trust, and product overview.', roles: ['guest', 'buyer', 'investor', 'advisor', 'admin', 'compliance'] },
  { label: 'Dashboard', href: '/dashboard', description: 'Role-aware command center for activity and next-best actions.', roles: ['buyer', 'investor', 'advisor', 'admin', 'compliance'] },
  { label: 'Search', href: '/search', description: 'Property discovery with AI-guided filtering.', roles: ['guest', 'buyer', 'investor', 'advisor'] },
  { label: 'Analytics', href: '/analytics', description: 'Investor returns, scenarios, and market intelligence.', roles: ['investor', 'advisor', 'admin'] },
  { label: 'Deals', href: '/deals/deal-room-alpha', description: 'Transaction tracking, documents, and milestones.', roles: ['buyer', 'investor', 'advisor', 'admin', 'compliance'] },
  { label: 'Admin', href: '/admin/compliance', description: 'Compliance, audit, and release governance controls.', roles: ['admin', 'compliance'] },
];

export const metrics: Metric[] = [
  { label: 'Qualified pipeline', value: '$148.2M', trend: '+12.4% QoQ' },
  { label: 'MoE confidence', value: '94%', trend: 'Explainability threshold met' },
  { label: 'Compliance SLA', value: '2.4h', trend: '-28 min improvement' },
  { label: 'Secure checkout', value: '99.97%', trend: 'PCI-segmented uptime' },
];

export const aiInsights: InsightCard[] = [
  { title: 'Portfolio diversification gap', expert: 'Investment ROI Expert', summary: 'Increase exposure to Lisbon and Abu Dhabi assets to balance currency and visa optionality.', confidence: '0.91', severity: 'informational' },
  { title: 'Residency eligibility hold', expert: 'Residency / Visa Expert', summary: 'Primary applicant qualifies, but spouse source-of-funds evidence requires review before release.', confidence: '0.88', severity: 'attention' },
  { title: 'Fraud / compliance escalation', expert: 'Payment & Fraud Expert', summary: 'Escrow beneficiary mismatch detected; route to compliance review before payment confirmation.', confidence: '0.97', severity: 'critical' },
];

export const listings: Listing[] = [
  { id: 'lisbon-terrace', slug: 'lisbon-terrace', title: 'Lisbon Alfama Smart Terrace', city: 'Lisbon', country: 'Portugal', price: '€1.42M', irr: '18.4%', yield: '5.9%', summary: 'Golden-visa-adjacent urban asset with renovation upside and strong mid-term demand.', tags: ['Residency', 'Value-add', 'AI score 92'] },
  { id: 'dubai-marina', slug: 'dubai-marina-residence', title: 'Dubai Marina Signature Residence', city: 'Dubai', country: 'UAE', price: '$2.8M', irr: '16.1%', yield: '7.1%', summary: 'High-liquidity waterfront inventory with premium tenant profile and low vacancy.', tags: ['Luxury', 'Income', 'AI score 95'] },
  { id: 'athens-courtyard', slug: 'athens-courtyard-lofts', title: 'Athens Courtyard Lofts', city: 'Athens', country: 'Greece', price: '€890K', irr: '14.7%', yield: '6.3%', summary: 'Adaptive reuse multifamily opportunity with compliance-ready document package.', tags: ['Core+', 'RBI', 'AI score 89'] },
];

export const workflow: WorkflowStep[] = [
  { title: 'Source of funds review', status: 'current', owner: 'Compliance squad', description: 'Dual-control verification against AML, sanctions, and residency thresholds.' },
  { title: 'Insurance quote bind', status: 'upcoming', owner: 'Insurance expert', description: 'Finalize hazard coverage and vacancy rider before signing.' },
  { title: 'Escrow deposit', status: 'blocked', owner: 'Payments orchestration', description: 'Awaiting fraud hold release and beneficiary reconfirmation.' },
  { title: 'Closing package', status: 'upcoming', owner: 'Document intelligence', description: 'Generate multilingual checklists and completion attestations.' },
];
