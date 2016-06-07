
STATUS_INDIVIDUAL = (
    ('ON', 'LOGGING_ON'),
    ('OFF', 'LOGGING_OFF')
)
class IndividualStatus:

    def __init__(self, individual_id, session_id, status, type):
        self.individual_id = individual_id
        self.session_id = session_id
        self.status = status
        self.type = type


