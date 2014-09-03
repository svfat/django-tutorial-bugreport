from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    template_name = 'list.html'

class BugDetailView(DetailView):
    model = Ticket
    template_name = 'detail.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')
