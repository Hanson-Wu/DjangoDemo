from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StockSerializer
from .models import Stock
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse


def index(request):
	return HttpResponse(u"Welcom!")
# list and create
class StockList(APIView):
	def get(self, request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many = True)
		return Response(serializer.data)
	def post(self):
		pass



