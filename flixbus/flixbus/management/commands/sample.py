import csv

from django.core.management.base import BaseCommand

from flixbus.flixbus.models import Ticket


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.import_tickets()

    def import_tickets(self):
        with open('homework_tickets.csv') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            [Ticket.objects.create(
                ride_id=int(float(row[0])),
                from_stop=int(float(row[1])),
                to_stop=int(float(row[2])),
                date=row[3],
                description=row[4],
                transaction_has=row[5],
                price=row[6]
            ) for row in reader if row[2]]
            # Ticket.objects.bulk_create([
            #     Ticket(
            #         ride_id=int(float(row[0])),
            #         from_stop=int(float(row[1])),
            #         to_stop=int(float(row[2])),
            #         date=row[3],
            #         description=row[4],
            #         transaction_has=row[5],
            #         price=row[6]
            #     ) for row in reader if row[2]
            # ])

