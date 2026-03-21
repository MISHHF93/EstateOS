EVENT_CATALOG = {
    'listing.published.v1': {
        'topic': 'estateos.listings',
        'event_type': 'listing.published',
        'fields': ['listing_id', 'property_id', 'published_at', 'broker_user_id'],
    },
    'deal.created.v1': {
        'topic': 'estateos.deals',
        'event_type': 'deal.created',
        'fields': ['deal_id', 'listing_id', 'buyer_user_id', 'seller_user_id', 'stage'],
    },
    'document.uploaded.v1': {
        'topic': 'estateos.documents',
        'event_type': 'document.uploaded',
        'fields': ['document_id', 'context_type', 'context_id', 'blob_path', 'uploaded_at'],
    },
    'ai.request.routed.v1': {
        'topic': 'estateos.ai',
        'event_type': 'ai.request.routed',
        'fields': ['ai_request_id', 'user_id', 'intent', 'selected_experts', 'release_status'],
    },
    'payment.succeeded.v1': {
        'topic': 'estateos.payments',
        'event_type': 'payment.succeeded',
        'fields': ['payment_id', 'deal_id', 'amount', 'currency', 'provider_reference'],
    },
    'residency.assessment.completed.v1': {
        'topic': 'estateos.residency',
        'event_type': 'residency.assessment.completed',
        'fields': ['application_id', 'result', 'score', 'jurisdiction', 'review_required'],
    },
    'insurance.quote.requested.v1': {
        'topic': 'estateos.insurance',
        'event_type': 'insurance.quote.requested',
        'fields': ['request_id', 'property_id', 'product_type', 'carrier_count', 'acord_version'],
    },
    'compliance.case.escalated.v1': {
        'topic': 'estateos.compliance',
        'event_type': 'compliance.case.escalated',
        'fields': ['case_id', 'severity', 'reason', 'assigned_queue'],
    },
    'notification.dispatched.v1': {
        'topic': 'estateos.notifications',
        'event_type': 'notification.dispatched',
        'fields': ['notification_id', 'user_id', 'channel', 'template_key', 'priority'],
    },
    'integration.webhook.accepted.v1': {
        'topic': 'estateos.integrations',
        'event_type': 'integration.webhook.accepted',
        'fields': ['provider', 'event_type', 'routing_key', 'received_at'],
    },
    'ledger.entry.posted.v1': {
        'topic': 'estateos.ledger',
        'event_type': 'ledger.entry.posted',
        'fields': ['entry_id', 'payment_intent_id', 'entry_type', 'amount', 'immutable_hash'],
    },
}

LISTING_PUBLISHED = EVENT_CATALOG['listing.published.v1']
DEAL_CREATED = EVENT_CATALOG['deal.created.v1']
DOCUMENT_UPLOADED = EVENT_CATALOG['document.uploaded.v1']
AI_REQUEST_ROUTED = EVENT_CATALOG['ai.request.routed.v1']
PAYMENT_SUCCEEDED = EVENT_CATALOG['payment.succeeded.v1']
RESIDENCY_ASSESSMENT_COMPLETED = EVENT_CATALOG['residency.assessment.completed.v1']
INSURANCE_QUOTE_REQUESTED = EVENT_CATALOG['insurance.quote.requested.v1']
COMPLIANCE_CASE_ESCALATED = EVENT_CATALOG['compliance.case.escalated.v1']
