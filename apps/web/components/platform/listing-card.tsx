import { MapPin, TrendingUp } from 'lucide-react';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { ButtonLink } from '@/components/ui/button';
import type { Listing } from '@/types/platform';

export function ListingCard({ listing }: { listing: Listing }) {
  return (
    <Card className="space-y-4">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm text-accent">{listing.price}</p>
          <h3 className="mt-2 text-xl font-semibold text-white">{listing.title}</h3>
          <p className="mt-2 flex items-center gap-2 text-sm text-slate-400"><MapPin className="h-4 w-4" /> {listing.city}, {listing.country}</p>
        </div>
        <Badge intent="success"><TrendingUp className="mr-1 inline h-3 w-3" /> {listing.irr} IRR</Badge>
      </div>
      <p className="text-sm text-slate-300">{listing.summary}</p>
      <div className="flex flex-wrap gap-2">
        {listing.tags.map((tag) => <Badge key={tag}>{tag}</Badge>)}
      </div>
      <div className="flex items-center justify-between text-sm text-slate-400">
        <span>Projected yield {listing.yield}</span>
        <ButtonLink href={`/properties/${listing.slug}`} variant="secondary">View details</ButtonLink>
      </div>
    </Card>
  );
}
