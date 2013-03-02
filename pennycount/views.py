import simplejson

from django.contrib.auth.decorators import login_required
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

    results = [{'name': friend.friend.get_full_name(), 'id': friend.friend.id} for friend in
            Friend.objects.filter(user=request.user)]

    return HttpResponse(simplejson.dumps(results), content_type="application/json")
