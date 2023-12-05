from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('', include('smart_home.urls'))
]



# from django.contrib import admin
# from django.urls import path
#
# from main.views import cars_list, CreateCarView, CarsListView, SaleDetails
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/cars/', CarsListView.as_view()),
#     path('api/v1/cars/create/', CreateCarView.as_view()),
#     path('api/v1/sales/<int:pk>/', SaleDetails.as_view())
# ]