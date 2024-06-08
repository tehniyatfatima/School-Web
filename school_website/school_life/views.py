from django.views.generic import ListView
from .models import SchoolLifeImage

class SchoolLifeView(ListView):
    model = SchoolLifeImage
    template_name = 'school_life/school_life.html'
    context_object_name = 'images'
    paginate_by = 6
