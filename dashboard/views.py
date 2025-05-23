from django.shortcuts import render

# Create your views here.
def ver_dashboard(request):
    return render(request, "dashboard/dashboard_template.html")