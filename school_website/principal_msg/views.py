from django.views.generic import TemplateView
from .models import PrincipalMessage

class PrincipalMessageView(TemplateView):
    template_name = 'principal_msg/principal_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['principal_message'] = PrincipalMessage.objects.first()
        return context
