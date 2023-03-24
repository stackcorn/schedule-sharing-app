from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = 'account/top.html'