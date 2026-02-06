from django.shortcuts import get_object_or_404
from services.models import Service


def bag_contents(request):
    """
    Returns context data for the shopping bag containing services.
    """
    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id in bag.keys():
        service = get_object_or_404(Service, pk=item_id)
        total += service.price
        service_count += 1
        bag_items.append({
            'item_id': item_id,
            'service': service,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
