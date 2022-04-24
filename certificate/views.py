from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user_entry.models import UserEntry
from utils import render_to_pdf


# def character_certificate(request):
#     context = {
#         'title': "Daily Attendants Sheet",
#         'nav_bar': "report_nav",
#     }
#     pdf = render_to_pdf('certificate/character_certificate.html', context)
#     return HttpResponse(pdf, content_type='application/pdf')

def character_certificate(request, pk):
    template_name = 'certificate/character_certificate_preview.html'

    context = {
        'user_data': UserEntry.objects.get(pk=pk),
        'title': "Character certificate",
        'nav_bar': "report_nav",
    }
    return render(request, template_name, context)
