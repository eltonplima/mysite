from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# https - protocol
# docs.djangoproject.com - fqdn(Fully Qualified Domain Name)
# /pt-br/4.0/intro/tutorial01/ - path
