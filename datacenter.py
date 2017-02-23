from endpoint import *

class Datacenter():
    def __init__(self, endpoints): 
        endpoints.sort(key = lambda x: x.dc_latency, reverse=True)
        self.endpoints = endpoints
        
        
        
if __name__ == '__main__':
    ls = [Endpoint(1, 10), Endpoint(2, 100)]
    dc = Datacenter(ls)
    for ep in dc.endpoints: 
        print(ep.id)
    
    