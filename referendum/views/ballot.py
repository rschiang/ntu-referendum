from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from referendum.models import Referendum, Record

@login_required
def ballot(request, ref_id):
    referendum = get_object_or_404(Referendum, id=ref_id)
    if not referendum.valid():
        return redirect('referendum.views.home')

    return render(request, 'ballot.html', {
        'referendum': referendum,
        'options': referendum.options.order_by('number', 'id'),
    })

@login_required
def next_ballot(request):
    now = timezone.now()
    voted_entries = Record.objects
                    .filter(user=request.user)
                    .values_list('id', flat=True)
    available_ref = Referendum.objects
                    .filter(enabled=True, starts_on__gte=now, ends_on__lte=now)
                    .exclude(id__in=voted_entries)
                    .order_by('number', 'ends_on')

    if not available_ref:
        return redirect('referendum.views.done')
    else:
        return redirect('referendum.views.ballot', ref_id=available_ref.first().id)
