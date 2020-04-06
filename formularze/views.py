from django.shortcuts import render
from django.views.generic import ListView, DetailView
from formularze.models import Pytanie, Odpowiedz

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


class ListaPytan(ListView):
    model = Pytanie
    template_name = 'formularze/lista_pytan.html'
    context_object_name = 'pytania'

    def get_queryset(self):
        return Pytanie.objects.order_by('-data_d')[:10]


class LiczbaGlosow(DetailView):
    model = Pytanie
    template_name = 'formularze/liczba_glosow.html'
    context_object_name = 'pytanie'


@login_required()
def pytanie_glosuj(request, pid):
    pytanie = get_object_or_404(Pytanie, pk=pid)
    if request.method == 'POST':
        try:
            odpowiedz = pytanie.odpowiedz_set.get(pk=request.POST['odpowiedz'])
        except (KeyError, Odpowiedz.DoesNotExist):
            return render(request, 'formularze/pytanie_glosuj.html', {
                'pytanie': pytanie,
                'komunikat_bledu': 'Nie wybrałeś odpowiedzi!',
            })
        else:
            odpowiedz.glosy += 1
            odpowiedz.save()
            return redirect(reverse('formularze:liczba-glosow', args=(pytanie.id,)))
    else:
        return render(request, 'formularze/pytanie_glosuj.html', {'pytanie': pytanie})