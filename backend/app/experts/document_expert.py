class DocumentExpert:
    def completeness(self, uploaded_documents: int, required_documents: int) -> float:
        if required_documents == 0:
            return 1.0
        return uploaded_documents / required_documents
