from django.urls import path

from mgr import customer, medicine, sign_in_out, test

urlpatterns = [
    path('customers',customer.dispatcher),
    path('medicines',medicine.dispatcher),
    path('signin',sign_in_out.signin),
    path('signout',sign_in_out.signout),
    path('test',test.url_test)
]
