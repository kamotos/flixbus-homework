from adaptor.model import CsvDbModel, CsvModel, SkipRow
from adaptor import fields

from flixbus.flixbus.models import Segment, RouteSegment, Ride, Ticket


class SegmentCSV(CsvModel):
    id = fields.IntegerField()
    from_stop = fields.IntegerField()
    to_stop = fields.IntegerField()
    distance = fields.DecimalField()

    class Meta:
        has_header = True
        delimiter = ','


class RouteSegmentCSV(CsvModel):
    route_id = fields.IntegerField()
    segment_id = fields.IntegerField()
    sequence = fields.IntegerField()

    class Meta:
        has_header = True
        delimiter = ','


class RideCSV(CsvModel):
    id = fields.IntegerField()
    from_stop = fields.IntegerField()
    to_stop = fields.IntegerField()
    route_id = fields.IntegerField()

    class Meta:
        has_header = True
        delimiter = ','


class TicketCSV(CsvModel):
    ride_id = fields.IntegerField()
    from_stop = fields.IntegerField()
    to_stop = fields.FloatField()
    date = fields.DateField(format="%Y-%m-%d")
    description = fields.CharField()
    transaction_has = fields.CharField()
    price = fields.DecimalField()

    class Meta:
        has_header = True
        delimiter = ','

    def prepare_to_stop(self, stop_id):
        if not stop_id:
            raise SkipRow
        return int(stop_id)


