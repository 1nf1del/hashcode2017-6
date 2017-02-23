class VideoManager():
    def __init__(self):
        self.videos = []
        
    def add(self, video):
        self.videos.append(video)
        
    def get(self, id):
        if id < len(self.videos):
            return self.videos[id]
        else:
            print ("Check for len video manager")
            
    def __str__(self):
        return "Video Manager of %i videos" % len(self.videos)

class Video():
    def __init__(self, id, size):
        self.id = id
        self.size = size
        
    def __str__(self):
        return "Video %i, size = %i" % (self.id, self.size)
        
        
        