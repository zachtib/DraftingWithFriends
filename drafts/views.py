import uuid

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Draft, DraftEntry, DraftSeat


@login_required
def my_drafts(request):
    entries = DraftEntry.objects.filter(player=request.user)
    seats = DraftSeat.objects.filter(user=request.user)

    response = ['My Drafts:']
    for entry in entries:
        response.append(f'Entry in {entry.draft}')
    for seat in seats:
        response.append(f'Seat #{seat.position} of {seat.draft}')
    return HttpResponse('\n'.join(response))


def draft_detail(request, draft_id: uuid):
    draft = get_object_or_404(Draft, uuid=draft_id)

    return HttpResponse(f'''
    {draft.name}
    Players: {draft.entries.count()}/{draft.max_players}
    '''.strip())


@login_required
def draft_join(request, draft_id: uuid):
    draft = get_object_or_404(Draft, uuid=draft_id)
    join_success = draft.join(request.user)
    if join_success:
        return HttpResponse('OK')
    else:
        return HttpResponse('Error')


@login_required
def draft_leave(request, draft_id: uuid):
    return render(request, '')
