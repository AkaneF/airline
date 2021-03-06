from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    context = {
      "flights": Flight.objects.all()
    }
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
        # pk = primary key it is like id
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
        #exclude all the passenger have flight id already
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
  try:
      passenger_id = int(request.POST["passenger"])
      passenger = Passenger.objects.get(pk=passenger_id)
      flight = Flight.objects.get(pk=flight_id)
  except KeyError:
      return render(request, "flights/error.html", {"message": "No selection"})
  except Flight.DoesNotExist:
      return render(request, "flights/error.html", {"message": "No flights."})
  except Passenger.DoesNotExist:
      return render(request, "flights/error.html", {"message": "No passenger."})

  passenger.flights.add(flight)
  return HttpResponseRedirect(reverse("flight", args=(flight_id)))
