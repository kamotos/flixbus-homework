from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from flixbus.flixbus.models import Segment, Ticket, RouteSegment, Route


@api_view()
def pax(request, segment_id):
    get_object_or_404(Segment, id=segment_id)
    routes = RouteSegment.objects.filter(segment=segment_id).values_list('route')
    pax = Ticket.objects.filter(ride__route__in=routes).count()
    return Response({'segment_id': int(segment_id), 'pax': pax})


@api_view()
def revenue(request, segment_id):
    segment = get_object_or_404(Segment, id=segment_id)

    # Getting all routes with their total distances
    routes_distances = Route.objects.values('id').annotate(
        total_distance=Sum('segments__distance')
    )
    segment_percentage = {
        route_distance['id']: segment.distance / route_distance['total_distance']
        for route_distance in routes_distances
    }
    revenue_per_route = Ticket.objects.values('ride__route').annotate(
        total_price=Sum('price')
    )
    total_revenue = 0
    for route_revenue in revenue_per_route:
        total_revenue += route_revenue['total_price'] * segment_percentage[route_revenue['ride__route']]
    return Response({'segment_id': int(segment_id), 'revenue': total_revenue})
