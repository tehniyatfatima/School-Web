from django.views.generic import FormView
from .models import ContactForm
from .forms import ContactFormForm

class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactFormForm
    success_url = '/thank-you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
