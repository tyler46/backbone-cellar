from wines.models import Wine
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    """Returns a list of all wines."""
    return render_to_response('index.html', { 'wines': Wine.objects.all()})

def detail(request, wine_id):
    """Returns the details for a specific wine."""
    wine = get_object_or_404(Wine, id=wine_id)
    return render_to_response('wine_detail.html', {'wine': wine})
