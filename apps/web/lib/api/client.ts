const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000/api/v1';

type NextAwareRequestInit = RequestInit & {
  next?: {
    revalidate?: number;
  };
};

interface RequestConfig extends NextAwareRequestInit {
  path: string;
  accessToken?: string;
}

export async function apiClient<T>({ path, accessToken, headers, ...init }: RequestConfig): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json',
      ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
      ...headers,
    },
    next: { revalidate: 30, ...init.next },
  });

  if (!response.ok) {
    throw new Error(`API request failed for ${path} with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export const endpoints = {
  auth: {
    signIn: '/auth/login',
    register: '/auth/register',
  },
  listings: '/listings',
  deals: '/deals',
  documents: '/documents',
  residencyPrograms: '/residency/programs',
  insurance: '/insurance/requests',
  payments: '/payments/intents',
  aiAssess: '/ai/assess',
  complianceCase: (id: string) => `/compliance/cases/${id}`,
};
