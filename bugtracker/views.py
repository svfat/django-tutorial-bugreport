from django.views.generic import ListView
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    template_name = 'list.html'
