from dataclasses import dataclass


@dataclass(frozen=True)
class AuthContext:
    user_id: str
    roles: tuple[str, ...]
    kyc_status: str = 'pending'


def get_demo_auth_context() -> AuthContext:
    return AuthContext(user_id='user-demo-001', roles=('buyer',))
