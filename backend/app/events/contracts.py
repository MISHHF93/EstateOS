LISTING_PUBLISHED = {
    'event_type': 'listing.published',
    'fields': ['listing_id', 'property_id', 'published_at', 'broker_user_id'],
}

DEAL_CREATED = {
    'event_type': 'deal.created',
    'fields': ['deal_id', 'listing_id', 'buyer_user_id', 'seller_user_id', 'stage'],
}

DOCUMENT_UPLOADED = {
    'event_type': 'document.uploaded',
    'fields': ['document_id', 'context_type', 'context_id', 'blob_path', 'uploaded_at'],
}

AI_REQUEST_ROUTED = {
    'event_type': 'ai.request.routed',
    'fields': ['ai_request_id', 'user_id', 'intent', 'selected_experts', 'release_status'],
}

PAYMENT_SUCCEEDED = {
    'event_type': 'payment.succeeded',
    'fields': ['payment_id', 'deal_id', 'amount', 'currency', 'provider_reference'],
}

RESIDENCY_ASSESSMENT_COMPLETED = {
    'event_type': 'residency.assessment.completed',
    'fields': ['application_id', 'result', 'score', 'jurisdiction', 'review_required'],
}

INSURANCE_QUOTE_REQUESTED = {
    'event_type': 'insurance.quote.requested',
    'fields': ['request_id', 'property_id', 'product_type', 'carrier_count', 'acord_version'],
}

COMPLIANCE_CASE_ESCALATED = {
    'event_type': 'compliance.case.escalated',
    'fields': ['case_id', 'severity', 'reason', 'assigned_queue'],
}
