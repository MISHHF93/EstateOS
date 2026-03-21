from app.models.entities import Listing
from app.repositories.in_memory import repo
from app.schemas.listings import AddressDetail, BrokerDetail, FavoriteCreateRequest, ListingCreateRequest, ListingDetailResponse, ListingListResponse, ListingSummary, PropertyDetail
from app.services.base import AuditedService


class ListingService(AuditedService):
    def __init__(self) -> None:
        if not repo.list('listings'):
            seed = Listing(
                title='Marina Apartment',
                description='Modern waterfront apartment',
                price=550000,
                currency='USD',
                city='Dubai',
                property_type='apartment',
                bedrooms=2,
                bathrooms=2,
            )
            repo.save('listings', seed.id, seed)

    def list_listings(self, page: int, page_size: int, city: str | None, min_price: float | None, max_price: float | None, property_type: str | None) -> ListingListResponse:
        items = repo.list('listings')
        filtered = [item for item in items if (city is None or item.city == city) and (property_type is None or item.property_type == property_type) and (min_price is None or item.price >= min_price) and (max_price is None or item.price <= max_price)]
        start = (page - 1) * page_size
        page_items = filtered[start : start + page_size]
        return ListingListResponse(items=[self._summary(item) for item in page_items], total=len(filtered))

    def create_listing(self, payload: ListingCreateRequest) -> ListingDetailResponse:
        listing = Listing(
            title=payload.title,
            description=payload.description,
            price=payload.price,
            currency=payload.currency,
            city=payload.city,
            property_type=payload.property_type,
            bedrooms=payload.bedrooms,
            bathrooms=payload.bathrooms,
        )
        repo.save('listings', listing.id, listing)
        self.audit('listing', listing.id, 'created', {'city': payload.city, 'country': payload.country})
        return self._detail(listing, payload.country, payload.area_value, payload.area_unit)

    def get_listing(self, listing_id: str) -> ListingDetailResponse:
        listing = repo.get('listings', listing_id)
        if listing is None:
            listing = repo.list('listings')[0]
        return self._detail(listing, 'UAE', 110, 'sqm')

    def favorite_listing(self, payload: FavoriteCreateRequest) -> ListingSummary:
        listing = repo.get('listings', payload.listing_id) or repo.list('listings')[0]
        self.audit('favorite', payload.listing_id, 'created')
        return self._summary(listing)

    def _summary(self, listing: Listing) -> ListingSummary:
        return ListingSummary(
            id=listing.id,
            title=listing.title,
            price=listing.price,
            currency=listing.currency,
            city=listing.city,
            bedrooms=listing.bedrooms,
            bathrooms=listing.bathrooms,
            thumbnail_url=listing.thumbnail_url,
        )

    def _detail(self, listing: Listing, country: str, area_value: float | None, area_unit: str | None) -> ListingDetailResponse:
        return ListingDetailResponse(
            id=listing.id,
            title=listing.title,
            description=listing.description,
            price=listing.price,
            currency=listing.currency,
            property=PropertyDetail(
                bedrooms=listing.bedrooms,
                bathrooms=listing.bathrooms,
                area_value=area_value,
                area_unit=area_unit,
            ),
            address=AddressDetail(city=listing.city, country=country),
            media=[],
            broker=BrokerDetail(id='broker-demo-001', name='Broker Name'),
        )
