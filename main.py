from file_helper import *
from pdb import set_trace as debugger

def main(file_name):
    file = './input/%s' % file_name
    video_manager, cache_manager, endpoint_manager = read_file(file)

    print("Going through endpoints")
    for endpoint in endpoint_manager.get_sorted_endpoints():
      # print(str(endpoint.id)+' has ' +str(len(endpoint.requests)) + 'videos requested') ########################
      for request in endpoint.videos_by_popularity():
        video = video_manager.get(request[0])
        if video.size <= cache_manager.get(0).space: # check whether video exceeds max cache size
          for connection in endpoint.caches_by_latency():
            if(cache_manager.get(connection[0]).add_video(video)):
              break


    write_output(cache_manager.caches, file_name)

if __name__ == '__main__':
  # files = ['input_example.txt']
  files = ['me_at_the_zoo.in', 'trending_today.in', 'videos_worth_spreading.in']
  files = ['kittens.in']
  # files = ['kittens.in', 'me_at_the_zoo.in', 'trending_today.in', 'videos_worth_spreading.in']

  for file_name in files:
    main(file_name)




 # objective function:
 #


 # go through endpoints in descending order of latency from data center -sort
 ### go through videos in descending order of requests -sort
 ##### put each video in nearest available cache -sort


 ### Cache Manager