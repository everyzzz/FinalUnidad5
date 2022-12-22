from versionedPago.v2.serializers import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from versionedPago.models import Services, ExpiredPayments, PaymentUser
from versionedPago.v2.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# TODO: User
class ServicesViewUser(ModelViewSet):
    """"Esta es una vista para el usuario"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    http_method_names = ['get']

    permission_classes = [IsAuthenticated]
    throttle_scope = 'services'

class PaymentUsersViewUser(ModelViewSet):
    """"Esta es una vista para el usuario"""
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUsersSerializers
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    throttle_scope = 'pagos'

class ExpiredPaymentViewUser(ModelViewSet):
    """"Esta es una vista para el usuario"""
    queryset = ExpiredPayments.objects.all()
    #serializer_class = ExpiredPaymentsSerializers
    pagination_class = SimplePagination
    http_method_names = ['get','post']
    permission_classes = [IsAuthenticated]
    throttle_scope = 'expired'


# TODO: Admin
class ServicesViewAdmin(ModelViewSet):
    """"Esta es una vista para el admin"""
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    #http_method_names = ['get']

    permission_classes = [IsAdminUser]
    throttle_scope = 'services'

class PaymentUsersViewAdmin(ModelViewSet):
    """"Esta es una vista para el admin"""
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUsersSerializers
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'expiration_date']

    permission_classes = [IsAdminUser]

    throttle_scope = 'pagos'

class ExpiredPaymentViewAdmin(ModelViewSet):
    """"Esta es una vista para el admin"""
    queryset = ExpiredPayments.objects.all()
    #serializer_class = ExpiredPaymentsSerializers
    pagination_class = SimplePagination
    #http_method_names = ['get','post']
    permission_classes = [IsAdminUser]
    throttle_scope = 'expired'