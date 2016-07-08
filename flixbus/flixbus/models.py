from django.db import models


class Segment(models.Model):
    from_stop = models.IntegerField()
    to_stop = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)


class Route(models.Model):
    segments = models.ManyToManyField(Segment, through='RouteSegment')


class RouteSegment(models.Model):
    route = models.ForeignKey(Route)
    segment = models.ForeignKey(Segment)
    sequence = models.PositiveSmallIntegerField(db_index=True)

    class Meta:
        ordering = ('route', 'sequence', )


class Ride(models.Model):
    from_stop = models.IntegerField()
    to_stop = models.IntegerField()
    route = models.ForeignKey(Route)


class Ticket(models.Model):
    ride = models.ForeignKey(Ride)
    from_stop = models.IntegerField()
    to_stop = models.IntegerField()
    date = models.DateField()
    description = models.TextField()
    transaction_has = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

