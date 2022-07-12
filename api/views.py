from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from api.serializers import RecipeSerializer
from api.models import Recipes

# Create your views here.
class ListView(ListAPIView):
    """This endpoint list all of the available recipes from the database"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
class RetrieveView(RetrieveAPIView):
    """This endpoint lists 1 recipe from the database"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class CreateView(CreateAPIView):
    """This endpoint allows for creation of a recipe"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class UpdateView(UpdateAPIView):
    """This endpoint allows for updating a specific recipe by passing in the id of the recipe to update"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class DeleteView(DestroyAPIView):
    """This endpoint allows for deletion of a specific recipe from the database"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer