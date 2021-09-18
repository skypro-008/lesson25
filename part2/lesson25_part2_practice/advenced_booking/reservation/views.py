from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    pass


@method_decorator(csrf_exempt, name='dispatch')
class DestinationCreateView(CreateView):
    pass



@method_decorator(csrf_exempt, name='dispatch')
class DestinationUpdateView(UpdateView):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class DestinationDeleteView(DeleteView):
    pass
