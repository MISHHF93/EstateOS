from fastapi import APIRouter, status

from app.schemas.documents import DocumentCompleteRequest, DocumentCompleteResponse, DocumentPresignRequest, DocumentPresignResponse
from app.services.document_service import DocumentService

router = APIRouter()
document_service = DocumentService()


@router.post('/presign', response_model=DocumentPresignResponse, status_code=status.HTTP_201_CREATED)
async def presign_document(payload: DocumentPresignRequest) -> DocumentPresignResponse:
    return document_service.presign_upload(payload)


@router.post('/{document_id}/complete', response_model=DocumentCompleteResponse)
async def complete_document(document_id: str, payload: DocumentCompleteRequest) -> DocumentCompleteResponse:
    return document_service.complete_upload(document_id, payload)
