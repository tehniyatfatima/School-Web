from django.views.generic import TemplateView
from .models import NavbarIcon, SliderImage

class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_icon'] = NavbarIcon.objects.first()
        context['slider_images'] = SliderImage.objects.all()
        return context
