from django.views.generic import ListView, DetailView
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    template_name = 'list.html'



class BugDetailView(DetailView):
    model = Ticket
    template_name = 'detail.html'
