from dataclasses import dataclass
from typing import Callable

from fastapi import Depends, Header, HTTPException, status


@dataclass(frozen=True)
class AuthContext:
    user_id: str
    roles: tuple[str, ...]
    scopes: tuple[str, ...] = ()
    kyc_status: str = 'pending'
    privacy_tier: str = 'standard'


ROLE_SCOPE_MAP = {
    'platform_admin': {'platform:read', 'platform:write', 'audit:read'},
    'broker': {'listing:write', 'listing:read', 'deal:read'},
    'buyer': {'listing:read', 'deal:write', 'document:write'},
    'compliance_officer': {'compliance:read', 'compliance:write', 'audit:read'},
    'finance_operator': {'payment:read', 'payment:write', 'ledger:read'},
}


def get_demo_auth_context() -> AuthContext:
    roles = ('platform_admin', 'buyer')
    scopes = tuple(sorted({scope for role in roles for scope in ROLE_SCOPE_MAP.get(role, set())}))
    return AuthContext(user_id='user-demo-001', roles=roles, scopes=scopes, kyc_status='verified', privacy_tier='enhanced')


async def get_current_auth_context(x_demo_roles: str | None = Header(default=None, alias='X-Demo-Roles')) -> AuthContext:
    if not x_demo_roles:
        return get_demo_auth_context()
    roles = tuple(role.strip() for role in x_demo_roles.split(',') if role.strip())
    scopes = tuple(sorted({scope for role in roles for scope in ROLE_SCOPE_MAP.get(role, set())}))
    return AuthContext(user_id='user-demo-001', roles=roles, scopes=scopes, kyc_status='verified', privacy_tier='enhanced')


def require_roles(*required_roles: str) -> Callable[[AuthContext], AuthContext]:
    async def dependency(context: AuthContext = Depends(get_current_auth_context)) -> AuthContext:
        if not set(required_roles).intersection(set(context.roles)):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Missing required role')
        return context

    return dependency
