from .models import Individual
from client.models import Client

def validate_individual(external_id, client_slug, os, version):
    cl = Client.objects.get(slug=client_slug)
    if (cl is None) or (external_id is None) or (os is None) or (version is None):
        return False
    else:
        return True

def create_individual_from_request(request):
    try:
        external_id = request.data['external_id'].__str__()
        client_slug = request.data['client_slug'].__str__()
        os = request.data['os'].__str__()
        version = request.data['version'].__str__()
    except Exception:
        return None

    validated = validate_individual(external_id, client_slug, os, version)

    if(validated is False):
        return None

    try:
        cl = Client.objects.get(slug=client_slug)
        individual = Individual.objects.create(external_id=external_id, client=cl, os=os, version=version)
        return individual
    except Exception:
        return None
