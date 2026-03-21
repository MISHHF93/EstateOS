LISTING_PUBLISHED = {
    'event_type': 'listing.published',
    'fields': ['listing_id', 'property_id', 'published_at'],
}

DEAL_CREATED = {
    'event_type': 'deal.created',
    'fields': ['deal_id', 'listing_id', 'buyer_user_id'],
}

PAYMENT_SUCCEEDED = {
    'event_type': 'payment.succeeded',
    'fields': ['payment_id', 'deal_id', 'amount', 'currency'],
}

RESIDENCY_ASSESSMENT_COMPLETED = {
    'event_type': 'residency.assessment.completed',
    'fields': ['application_id', 'result', 'score'],
}
