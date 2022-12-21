from versionedPago.v2.serializers import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from versionedPago.models import Services, ExpiredPayments, PaymentUser
from versionedPago.v2.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class ServicesView(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    http_method_names = ['get']

    permission_classes = [IsAuthenticated]
    throttle_scope = 'services'

class PaymentUsersView(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUsersSerializers
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']

    permission_classes = [AllowAny]

    throttle_scope = 'pagos'

from django.shortcuts import get_object_or_404
class ExpiredPaymentView(ModelViewSet):
    queryset = ExpiredPayments.objects.all()
    #serializer_class = ExpiredPaymentsSerializers
    pagination_class = SimplePagination
    #http_method_names = ['get','post']
    #permission_classes = [AllowAny]
    throttle_scope = 'expired'

    def get_serializer_class(self):
        return ExpiredPaymentsSerializers

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = ExpiredPaymentsSerializers(data=request.data, many = True)
        else:
            serializer = ExpiredPaymentsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializers(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializers(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializers(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)