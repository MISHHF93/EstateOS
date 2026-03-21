export interface OpenApiOperationDescriptor {
  service: string;
  path: string;
  method: 'GET' | 'POST' | 'PUT' | 'PATCH';
  summary: string;
}

export const openApiCatalog: OpenApiOperationDescriptor[] = [
  { service: 'listing-service', path: '/listings', method: 'GET', summary: 'Search and filter global property inventory.' },
  { service: 'document-service', path: '/documents/presign', method: 'POST', summary: 'Generate secure upload URLs for due diligence artifacts.' },
  { service: 'payment-service', path: '/payments/intents', method: 'POST', summary: 'Create escrow, reservation, or insurance payment intents.' },
  { service: 'ai-orchestrator', path: '/ai/assess', method: 'POST', summary: 'Request governed MoE insights, recommendations, and next-best actions.' },
];
