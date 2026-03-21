from app.schemas.common import APIModel


class ListingCreateRequest(APIModel):
    title: str
    description: str = ''
    price: float
    currency: str
    city: str
    country: str
    property_type: str
    bedrooms: int = 0
    bathrooms: int = 0
    area_value: float | None = None
    area_unit: str | None = None


class FavoriteCreateRequest(APIModel):
    listing_id: str


class ListingSummary(APIModel):
    id: str
    title: str
    price: float
    currency: str
    city: str
    bedrooms: int
    bathrooms: int
    thumbnail_url: str


class ListingListResponse(APIModel):
    items: list[ListingSummary]
    total: int


class PropertyDetail(APIModel):
    bedrooms: int
    bathrooms: int
    area_value: float | None = None
    area_unit: str | None = None


class AddressDetail(APIModel):
    city: str
    country: str
    latitude: float = 25.08
    longitude: float = 55.14


class BrokerDetail(APIModel):
    id: str
    name: str


class ListingDetailResponse(APIModel):
    id: str
    title: str
    description: str
    price: float
    currency: str
    property: PropertyDetail
    address: AddressDetail
    media: list[dict]
    broker: BrokerDetail
