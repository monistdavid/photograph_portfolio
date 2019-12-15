from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "portfolio/index.html"

    def get(self, request):
        return render(request, "portfolio/index.html")

    def post(self, request):
        return render(request, "portfolio/index.html")
