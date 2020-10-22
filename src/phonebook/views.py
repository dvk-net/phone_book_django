from django.views.generic import TemplateView, CreateView, DeleteView
from django.urls import reverse_lazy


from .forms import CreatePersoneForm 
from .models import Phone, Persone

class HomePageView(TemplateView):
    template_name="phonebook/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = 'All phones'
        if search_by in ['phone', 'name'] and search_by:
            if search_by == 'name':
                persons = Persone.objects.filter(name=query)
                search_message = f'Searching for "name" by "{query}"'
            else:
                persons = Persone.objects.filter(phones__phone=query)
                search_message = f'Searching for "phones" by "{query}"'
        else:
            persons = Persone.objects.all()
        context["persons"] = persons
        context["search_message"] = search_message
        return context
    

class AddPhoneFormView(CreateView):
    template_name="phonebook/add_persone.html"
    form_class = CreatePersoneForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()

class DeletePhoneView(DeleteView):
    model = Persone
    template_name="phonebook/delete_persone.html"
    success_url = reverse_lazy('home')