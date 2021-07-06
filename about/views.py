from about.models import AboutPage
from django.views.generic.base import TemplateView
class AboutUs(TemplateView):
    model = AboutPage
    # context_object_name = 'about'
    template_name = 'about/aboutus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutpages'] = AboutPage.objects.get(id=1)
        return context