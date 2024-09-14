from rest_framework import viewsets
from .models import ChecklistItem
from .serializers import ChecklistItemSerializer

class ChecklistItemViewSet(viewsets.ModelViewSet):
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer