from django.shortcuts import render
from studenci.forms import UserLoginForm

def index(request):
    return render(request,'users/index.html')

def loguj_user(request):
    """Widok wyświetlający formularz logowania"""
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()

    kontekst = {'form': form}
    return render(request, 'users/login.html', kontekst)
