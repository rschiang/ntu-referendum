import hashlib
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from referendum.models import Referendum, Option, Ballot, Record

@login_required
def vote(request, ref_id):
    referendum = get_object_or_404(Referendum, id=ref_id)
    if not referendum.valid():
        return redirect('referendum.views.home')

    record = Record.objects.filter(user=request.user, referendum=referendum)
    if record.exists():
        # Skipped or already voted
        return redirect('referendum.views.next_ballot')

    try:
        if request.POST.get('skip'):
            choice = -1
            option = None
        else:
            choice = int(request.POST.get('choice'))
            option = Option.objects.get(referendum=referendum, id=choice)
    except (ValueError, Record.DoesNotExist):
        # Invalid parameter
        return redirect('referendum.views.ballot', ref_id)

    record = Record(referendum=referendum, user=request.user)
    record.state = Record.VOTED
    record.save()

    # Generate verification token
    now = timezone.now()
    base_str = '&'.join((str(ref_id), str(choice), now.isoformat(), request.get_host(), settings.VOTE_VALIDATION_KEY))
    token = hashlib.sha256(base_str.encode()).hexdigest().upper()

    ballot = Ballot(referendum=referendum, option=option)
    ballot.token = token
    ballot.save()

    return redirect('referendum.views.next_ballot')
