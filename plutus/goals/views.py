from django.http import HttpResponse, JsonResponse


# from goals.models
def view_levels(request):
    return JsonResponse(
  {
    "1": "0-50",
    "2": "50-100",
    "3": "150-300",
    "4": "300-500",
    "5": "500-750",
    "6": "750-1050",
    "7": "1050-1400",
    "8": "1400-1800",
    "9": "1800-2250",
    "10": "2250-2750",
    "11": "2750-3300",
    "12": "3300-3900"
  }
)
def giveme10(request):
    return JsonResponse({"1":"0"})