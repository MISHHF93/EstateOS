from app.schemas.common import APIModel


class UserProfileView(APIModel):
    first_name: str = 'Ava'
    last_name: str = 'Stone'
    country_of_residence: str = 'Canada'


class UserMeResponse(APIModel):
    id: str
    email: str
    roles: list[str]
    profile: UserProfileView


class UserPreferenceUpdate(APIModel):
    budget_min: float | None = None
    budget_max: float | None = None
    preferred_cities: list[str] = []
    property_types: list[str] = []
    residency_interest: bool = False
    insurance_interest: bool = False
    investment_goal: str | None = None


class UserPreferenceView(UserPreferenceUpdate):
    user_id: str
