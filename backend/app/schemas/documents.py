from app.schemas.common import APIModel


class DocumentPresignRequest(APIModel):
    file_name: str
    category: str
    context_type: str
    context_id: str


class DocumentPresignResponse(APIModel):
    upload_url: str
    document_id: str


class DocumentCompleteRequest(APIModel):
    checksum: str


class DocumentCompleteResponse(APIModel):
    document_id: str
    status: str
    checksum: str
