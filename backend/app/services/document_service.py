from app.models.entities import Document
from app.repositories.in_memory import repo
from app.schemas.documents import DocumentCompleteRequest, DocumentCompleteResponse, DocumentPresignRequest, DocumentPresignResponse
from app.services.base import AuditedService


class DocumentService(AuditedService):
    def presign_upload(self, payload: DocumentPresignRequest) -> DocumentPresignResponse:
        document = Document(
            file_name=payload.file_name,
            category=payload.category,
            context_type=payload.context_type,
            context_id=payload.context_id,
        )
        repo.save('documents', document.id, document)
        self.audit('document', document.id, 'presigned')
        return DocumentPresignResponse(upload_url=document.upload_url, document_id=document.id)

    def complete_upload(self, document_id: str, payload: DocumentCompleteRequest) -> DocumentCompleteResponse:
        self.audit('document', document_id, 'uploaded', {'checksum': payload.checksum})
        return DocumentCompleteResponse(document_id=document_id, status='uploaded', checksum=payload.checksum)
