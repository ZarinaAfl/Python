import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import rest_framework
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, FormView, CreateView

from music.forms import ArtistForm, LoginForm
from music.models import City, Artist, History


#@login_not_required - ToDo
def do_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if "next" in request.GET:
                return HttpResponseRedirect(request.GET["next"])
            else:
                return HttpResponseRedirect(reverse("artists"))
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(
            request,
            "music/login.html",
            {"f": LoginForm()}
        )
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect(reverse("artists"))
    else:
        form = UserCreationForm
    return render(request, 'music/signup.html', {'form':form})

class HelloView(TemplateView):
    template_name = "music/hello.html"


class ListCityView(ListView):
    template_name = "music/list_of_cities.html"
    model = City
    context_object_name = "cities"


class ListArtistView(ListView):
    template_name = "music/list_of_artists.html"
    model = Artist
    context_object_name = "artists"


class ListHistoryView(ListView):
    template_name = 'history.html'
    model = History
    context_object_name = "history"



@login_required#(login_url=reverse_lazy("login"))
def add_new_artist(request):
    if request.user.has_perm("misic.add_artist"):

        if request.method == "POST":
            f = ArtistForm(data=request.POST)
            f.save()
            h = History(user=request.user, artist=f.name, time=datetime.datetime.now())
            h.save()
            return HttpResponseRedirect(reverse("artists"))
        else:
            return render(request,
                          "music/add_new_artist.html",
                          {"f": ArtistForm()}
            )
    else:
        return HttpResponseRedirect(reverse("artists"))

def show_history(request):
    if request.method == "GET":
        history = History.objects.all()
        context = {'history': history}
        template = loader.get_template('history.html')
        return HttpResponse(template.render(context))


@method_decorator(login_required, name="dispatch")
class AddNewArtistView(CreateView):
    template_name = "music/add_new_artist.html"
    form_class = ArtistForm
    success_url = reverse_lazy("artists")

    #@method_decorator(login_required) - before django 1.9
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("misic.add_artist"):
            return super(AddNewArtistView, self).dispatch(request, *args, **kwargs)


    #def post(self, request, *args, **kwargs):
    #    f = ArtistForm(request.POST)
    #    f.save()
    #    return HttpResponseRedirect(AddNewArtistView.success_url)