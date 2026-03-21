from fastapi import APIRouter

from app.api.v1 import ai, auth, compliance, deals, documents, insurance, listings, payments, residency, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(listings.router, prefix='/listings', tags=['listings'])
api_router.include_router(deals.router, prefix='/deals', tags=['deals'])
api_router.include_router(documents.router, prefix='/documents', tags=['documents'])
api_router.include_router(residency.router, prefix='/residency', tags=['residency'])
api_router.include_router(insurance.router, prefix='/insurance', tags=['insurance'])
api_router.include_router(payments.router, prefix='/payments', tags=['payments'])
api_router.include_router(compliance.router, prefix='/compliance', tags=['compliance'])
api_router.include_router(ai.router, prefix='/ai', tags=['ai'])
