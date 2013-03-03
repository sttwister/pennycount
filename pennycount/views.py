import simplejson

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response

from .models import Friend

@login_required
def index(request):
    return render_to_response('index.html')

@login_required
def friends(request):
    if not request.is_ajax():
        return HttpResponseBadRequest

    q = request.GET.get('term')
    results = [
            {
                'name': '%s (%s)' % (friend.friend.get_full_name(), friend.friend.email),
                'id': friend.friend.id
            }
            for friend in Friend.objects.filter(user=request.user).filter(
                    Q(friend__first_name__icontains=q) |
                    Q(friend__last_name__icontains=q) |
                    Q(friend__email__icontains=q)
            )
    ]

    return HttpResponse(simplejson.dumps(results), content_type="application/json")
