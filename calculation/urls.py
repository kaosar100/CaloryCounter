from django.urls import path
from .api_views import CalculationAPIView

urlpatterns = [
    path(
        "api/calculation/",
        CalculationAPIView.as_view(),
        name="api_calculation",
    ),
]