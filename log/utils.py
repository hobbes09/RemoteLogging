from .models import Log
from individual.models import Individual
from session.models import Session
import datetime

LOG_TYPES = ['A', 'D', 'E', 'I', 'V', 'W']

def validate_log(body, type, individual_ext_id, session_id):
    try:
        individual = Individual.objects.get(external_id=individual_ext_id)
        session = Session.objects.get(pk=session_id)
    except Exception:
        individual = None
        session = None

    if (individual is None) or (session is None) or (type not in LOG_TYPES):
        return False
    return True



def create_log_from_request(request):
    try:
        body = request.data['body'].__str__()
        type = request.data['type'].__str__()
        individual_ext_id = request.data['individual_ext_id'].__str__()
        session_id = request.data['session_id'].__str__()
    except Exception:
        return (None, "Fields are missing")

    validated = validate_log(body, type, individual_ext_id, session_id)

    if (validated is False):
        return (None, "Validation Failed")

    try:
        indv = Individual.objects.get(external_id=individual_ext_id)
        session = Session.objects.get(pk=session_id)
        log = Log.objects.create(body=body, type=type, individual=indv, session=session, created=datetime.datetime.utcnow())
        return (log, None)
    except Exception:
        return (None, "Not able to create log instance")
