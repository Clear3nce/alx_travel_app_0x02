from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_titles = [
            "Cozy Cottage", "Urban Loft", "Beachfront Bungalow",
            "Mountain Retreat", "Luxury Villa", "Modern Studio"
        ]
        locations = ["Cape Town", "Johannesburg", "Durban", "Pretoria", "Port Elizabeth"]

        for i in range(10):
            listing = Listing.objects.create(
                title=random.choice(sample_titles),
                description="A wonderful place to stay with all amenities.",
                location=random.choice(locations),
                price_per_night=random.uniform(50.00, 300.00),
                available=True
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
