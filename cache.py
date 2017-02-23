class CacheManager():
    def __init__(self):
        self.caches = []
        
    def add(self, cache):
        self.caches.append(cache)
        
    def get(self, id):
        if id < len(self.caches):
            return self.caches[id]
        else:
            print("Check id for cache manager get")
            
    def used_caches(self):
        [cache for cache in self.caches if cache.is_used()]

    def __str__(self):
        return "Cache manager has %i caches" % len(self.caches)
    

class Cache():
    def __init__(self, id, space, V):
        self.id = id
        self.space = space
        self.remaining_space = space
        self.videos = [0 for i in range(V)]
    
    def add_video(self, video):
        if self.videos[video.id] == 1:
            return True
        elif video.size <= self.remaining_space:
            self.videos[video.id] = 1
            self.remaining_space -= video.size
            return True
        else:
            return False
            
            
    def videos_in_cache(self):
        return [str(x[0]) for x in enumerate(self.videos) if x[1] == 1] 


    def is_used(self):
        if self.remaining_space == self.space:
            return False
        else:
            return True
        
        
        
        
        
        
        