from django.shortcuts import render
from rest_framework import generics
from .mutant import mutant
from rest_framework.response import Response



class MutantsappViewSet(generics.CreateAPIView):
    def post(self, request):
        dna = request.data["dna"]
        if mutant(dna):
            return Response(None, status=200)
        return Response(None, status=403)
    

    
    
