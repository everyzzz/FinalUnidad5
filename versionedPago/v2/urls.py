from rest_framework.routers import DefaultRouter
from versionedPago.v2.api import ExpiredPaymentViewUser, PaymentUsersViewUser, ServicesViewUser
from versionedPago.v2.api import ExpiredPaymentViewAdmin, PaymentUsersViewAdmin, ServicesViewAdmin

route = DefaultRouter()
# Todo: User
route.register("services/user", ServicesViewUser, basename = "services-user")
route.register("payment-users/user", PaymentUsersViewUser, basename = "payment-user-user")
route.register("expired-payment/user", ExpiredPaymentViewUser, basename = "expired-payment-user")

# Todo: Admin
route.register("services/admin", ServicesViewAdmin, basename = "services-admin")
route.register("payment-users/admin", PaymentUsersViewAdmin, basename = "payment-user-admin")
route.register("expired-payment/admin", ExpiredPaymentViewAdmin, basename = "expired-payment-admin")

urlpatterns = route.urls