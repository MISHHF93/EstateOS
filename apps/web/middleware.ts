import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const protectedPrefixes = ['/dashboard', '/favorites', '/saved-searches', '/analytics', '/deals', '/documents', '/payments', '/notifications', '/admin', '/ai-workspace', '/residency', '/insurance'];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const session = request.cookies.get('__Secure-estateos.session');
  const locale = request.cookies.get('estateos.locale')?.value ?? 'en';

  if (pathname === '/') {
    const response = NextResponse.next();
    response.cookies.set('estateos.locale', locale, { sameSite: 'lax', secure: true, path: '/' });
    return response;
  }

  if (protectedPrefixes.some((prefix) => pathname.startsWith(prefix)) && !session) {
    const signInUrl = new URL('/sign-in', request.url);
    signInUrl.searchParams.set('redirectTo', pathname);
    return NextResponse.redirect(signInUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
