from django.urls import path
from .views import (AllBookVIew,
                    FirstTypeAllProductView,
                    SecondTypeAllProductView,
                    ThirdTypeAllProductView,
                    FourthTypeAllProductView,
                    DetailFirstTypeProductView,
                    DetailSecondTypeProductView,
                    DetailThirdTypeProductView,
                    DetailFourthTypeProductView)
urlpatterns = [
    path('', AllBookVIew.as_view()),
    path('first/',FirstTypeAllProductView.as_view()),
    path('second/',SecondTypeAllProductView.as_view()),
    path('third/',ThirdTypeAllProductView.as_view()),
    path('fourth/',FourthTypeAllProductView.as_view()),
    path('first/<int:product_id>/',DetailFirstTypeProductView.as_view()),
    path('second/<int:product_id>/',DetailSecondTypeProductView.as_view()),
    path('third/<int:product_id>/',DetailThirdTypeProductView.as_view()),
    path('fourth/<int:product_id>/',DetailFourthTypeProductView.as_view())

]