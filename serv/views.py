from django.shortcuts import render

# Create your views here.
def serve(request):
    context = {'services': 'active'}
    return render(request, 'serv/services.html', context)