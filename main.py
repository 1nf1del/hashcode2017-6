from file_helper import * 

def main():
    video_manager, cache_manager, endpoint_manager = read_file('./input/input_example.txt')

    print("Going through endpoints")
    for endpoint in endpoint_manager.get_sorted_endpoints():
      print(str(endpoint.id)+' has ' +str(len(endpoint.requests)) + 'videos requested') ########################
      for request in endpoint.videos_by_popularity():
        video = video_manager.get(request[0])
        if video.size <= cache_manager.get(0).space: # check whether video exceeds max cache size
          for connection in endpoint.caches_by_latency():
            if(cache_manager.get(connection[0]).add_video(video)):
              break
        
    write_output(cache_manager.caches) 
  
 
if __name__ == '__main__': 
  main()

 
 
 
 # objective function: 
 #
 
 
 # go through endpoints in descending order of latency from data center -sort
 ### go through videos in descending order of requests -sort
 ##### put each video in nearest available cache -sort
 
 
 ### Cache Manager