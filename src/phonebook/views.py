from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import CreatePersoneForm 
from .models import Phone

class HomePageView(TemplateView):
    template_name="phonebook/home.html"

class AddPhoneFormView(CreateView):
    template_name="phonebook/add_persone.html"
    form_class = CreatePersoneForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()
