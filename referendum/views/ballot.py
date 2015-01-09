from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from referendum.models import Referendum

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
    pass
