from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return render_to_response(
                    'profile/personal.html',
                    {'user': request.user})

@login_required
def user_profile(request,id):
    user = get_object_or_404(User,id=id)
    profile = get_object_or_404(Profile,user=user)
    return render_to_response(
                  'profile/user_profile.html',
                  {'user':request.user,'profile':profile})