
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

# Login required mixin to restrict the pages only for logged in users
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Record

# Create your views here.

# Login View
class AppLoginView(LoginView):
    template_name = 'baseapp/login.html'
    fields = '__all__'
    redirect_authenticated_user: True
    
    def get_success_url(self):
        return reverse_lazy('records')


# List View of Records
class RecordList(LoginRequiredMixin, ListView):
    model = Record
    context_object_name = 'records'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search_input = self.request.GET.get('search-data') or ''
        if search_input:
            context['records'] = ( context['records'].filter(reg_no__icontains = search_input)
                                  or 
                                  context['records'].filter(name__icontains = search_input) )
        context['search_input'] = search_input
        return context
    
# Detailed View for a Record
class RecordDetail(LoginRequiredMixin, DetailView):
    model = Record
    context_object_name = 'record'
    template_name = 'baseapp/record.html'
    
# Create Record View
class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record
    fields = '__all__'
    success_url = reverse_lazy('records')
    
# Update Record View
class RecordUpdate(LoginRequiredMixin, UpdateView):
    model = Record
    fields = '__all__'
    success_url = reverse_lazy('records')
    
# Delete Record View
class RecordDelete(LoginRequiredMixin, DeleteView):
    model = Record
    fields = '__all__'
    success_url = reverse_lazy('records')