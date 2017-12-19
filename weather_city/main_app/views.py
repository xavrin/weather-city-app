from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse
from django.conf import settings
from main_app import forms
from main_app import countries_api
from main_app import weather_api

class MainView(FormView):
    template_name = 'search.html'
    form_class = forms.SearchForm

    def form_valid(self, form):
        country = form.cleaned_data['country']
        return HttpResponseRedirect(reverse('weather', kwargs={'country': country}))

class WeatherView(TemplateView):
    template_name = 'weather.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not countries_api.is_country_valid(context['country']):
            raise Http404()
        capital = countries_api.get_capital(context['country'])
        weather_html = weather_api.get_weather(capital)
        context['weather'] = weather_html
        context['city'] = capital
        context['map_key'] = settings.MAPS_API_KEY
        return context
