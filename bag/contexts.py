from decimal import Decimal
from django.shortcuts import get_object_or_404
from services.models import Service
from checkout.models import Discount


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

    # Initialise discount variables for context
    discount = None
    discount_amount = 0
    discount_id = request.session.get('discount_id')

    if discount_id and total > 0:
        try:
            discount = Discount.objects.get(pk=discount_id, active=True)
            discount_amount = round(
                total * Decimal(discount.percentage / 100), 2)
        except Discount.DoesNotExist:
            request.session.pop('discount_id', None)
            discount = None
            discount_amount = 0

    grand_total = total - discount_amount

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'discount': discount,
        'discount_amount': discount_amount,
        'grand_total': grand_total,
    }

    return context
