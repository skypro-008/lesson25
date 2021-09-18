from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from reservation.models import Destination


# views.py
class DestinationListView(ListView):
    model = Destination

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for destination in self.object_list:
            # TODO
            pass

        return JsonResponse(response, safe=False)


class DestinationDetailView(DetailView):
    pass
