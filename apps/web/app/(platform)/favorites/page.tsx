import { ListingCard } from '@/components/platform/listing-card';
import { PlatformPageTemplate } from '@/components/platform/page-template';
import { listings } from '@/lib/mocks/platform-data';

export default function FavoritesPage() {
  return (
    <PlatformPageTemplate eyebrow="Favorites" title="Curated shortlist" description="Persist favorite listings with transparent AI rationale, document completeness indicators, and next-best actions.">
      <div className="grid gap-4 lg:grid-cols-2">{listings.slice(0, 2).map((listing) => <ListingCard key={listing.id} listing={listing} />)}</div>
    </PlatformPageTemplate>
  );
}
