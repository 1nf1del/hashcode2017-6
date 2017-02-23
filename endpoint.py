class EndpointManager():
    def __init__(self):
        self.endpoints = []

    def add(self, endpoint):
        self.endpoints.append(endpoint)

    def get_sorted_endpoints(self):
        self.endpoints.sort(key = lambda x: x.weight(), reverse=True)
        return self.endpoints

    def get(self, id):
        if id < len(self.endpoints):
            return self.endpoints[id]
        else:
            print("Check id for endpoint manager get")

    def __str__(self):
        return "Endpoint manager has %i endpoints" % len(self.endpoints)

class Endpoint():
    def __init__(self, id, dc_latency):
        self.id = id
        self.dc_latency = dc_latency
        self.connections = []
        self.requests = []

    def weight(self):
        """ Instead of only relying on dc_latency, we also need to know
        how many requests are coming from this endpoint.
        """
        num_of_request = sum([x[1] for x in self.requests])
        return num_of_request * self.dc_latency

    def add_cache(self, cache_id, cache_latency):
        self.connections.append((cache_id, cache_latency))


    def add_request(self, video_id, quantity):
        self.requests.append((video_id, quantity))

    def __str__(self):
        return "Endpoint = %i, Number of caches: %i" % (self.id, len(self.connections))

    def videos_by_popularity(self):
        self.requests.sort(key = lambda x: x[1], reverse=True)
        return self.requests

    def caches_by_latency(self):
        self.connections.sort(key = lambda x: x[1])
        return self.connections