from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from reservation.models import Destination

class DestinationListView(ListView):
    model = Destination

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for destination in self.object_list:
            response.append({
                "id": destination.id,
                "name": destination.name,
            })

        return JsonResponse(response, safe=False)


class DestinationDetailView(DetailView):
    model = Destination

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "visa_id": self.object.visa_id,
            "covid_status": self.object.covid_status,
        })
