from django.conf import settings

def global_constants(request):
    return {
        'DEPLOYMENT_ENVIRONMENT': settings.DEPLOYMENT_ENVIRONMENT,
        'HEAP_ENV_ID': settings.HEAP_ENV_ID,
    }
