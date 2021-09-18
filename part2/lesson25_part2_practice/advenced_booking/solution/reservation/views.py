import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView

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


@method_decorator(csrf_exempt, name='dispatch')
class DestinationCreateView(CreateView):
    model = Destination
    fields = ["name", "visa_id", "covid_status"]

    def post(self, request, *args, **kwargs):
        destination_data = json.loads(request.body)

        destination = Destination()
        destination.name = destination_data["name"]
        destination.visa_id = destination_data["visa_id"]
        destination.covid_status = destination_data["covid_status"]

        try:
            destination.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        destination.save()
        return JsonResponse({
            "id": destination.id,
            "name": destination.name,
            "visa_id": destination.visa_id,
            "covid_status": destination.covid_status,
        })



@method_decorator(csrf_exempt, name='dispatch')
class DestinationUpdateView(UpdateView):
    model = Destination
    fields = ["name", "visa_id", "covid_status"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        destination_data = json.loads(request.body)
        self.object.name = destination_data["name"]
        self.object.visa_id = destination_data["visa_id"]
        self.object.covid_status = destination_data["covid_status"]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "visa_id": self.object.visa_id,
            "covid_status": self.object.covid_status,
        })


@method_decorator(csrf_exempt, name='dispatch')
class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)