from django.urls import path
from api import views

urlpatterns = [
    path("",views.ListView.as_view(),name="list"),
    path("<int:pk>/",views.RetrieveView.as_view(),name="read"),
    path("create/", views.CreateView.as_view(),name="create"),
    path("update/<int:pk>/",views.UpdateView.as_view(),name="update"),
    path("delete/<int:pk>/",views.DeleteView.as_view(),name="delete")
]