from trip import models as trip_models


class Trip:
    def __init__(self, page_size):
        self.page_size = page_size

    def get_ongoing_requests(self):
        record_requests = trip_models.TripRequest.objects.\
            filter(status="ONGOING").order_by('-date_created')
        response_info = {
            'count': record_requests.count(),
            'query_set': record_requests,
            'all_requests': record_requests
        }
        return response_info

    def get_completed_requests(self):
        record_requests = trip_models.TripRequest.objects.\
            filter(status="COMPLETED").order_by('-date_created')
        response_info = {
            'count': record_requests.count(),
            'query_set': record_requests,
            'all_requests': record_requests
        }
        return response_info
