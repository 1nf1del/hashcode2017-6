from video import *
from cache import *
from endpoint import *

def read_file(file_path):

    with open(file_path, 'r') as input:

        first_line = input.readline()

        V, E, R, C, X = [int(x) for x in first_line.split(' ')]

        second_line = input.readline()
        video_manager = VideoManager()

        size_videos = [int(x) for x in second_line.split(' ')]
        for (id, size) in enumerate(size_videos):
            video_manager.add(Video(id, size))

        # create caches
        cache_manager = CacheManager()
        for i in range(C):
            current_cache = Cache(i, X, V)
            cache_manager.add(current_cache)

        # create endpoint manager
        endpoint_manager = EndpointManager()

        # handle the endpoint
        endpoint_id = 0
        while(endpoint_id < E):
            row = input.readline()

            dc_latency, num_of_connected_caches = [int(x) for x in row.split(' ')]
            current_endpoint = Endpoint(endpoint_id, dc_latency)
            endpoint_id += 1

            i = 0

            while(i < num_of_connected_caches):
                row = input.readline()
                cache_id, cache_latency = [int(x) for x in row.split(' ')]
                current_endpoint.add_cache(cache_id, cache_latency)
                i += 1

            endpoint_manager.add(current_endpoint)


        # handle the request
        i = 0
        while(i < R):
            row = input.readline()
            vid_id, endpoint_id, quantity = [int(x) for x in row.split(' ')]
            endpoint = endpoint_manager.get(endpoint_id).add_request(vid_id, quantity)


            i += 1
    return video_manager, cache_manager, endpoint_manager


def write_output(ls_of_caches, file_name):
    file_name = './output3/%s.out' % file_name
    with open(file_name, 'w') as output:
        used_caches = [cache for cache in ls_of_caches if cache.is_used()]
        nr_caches = len(used_caches)
        output.write("{}\n".format(nr_caches))

        for cache in used_caches:
            print(cache.videos_in_cache())
            videos_id = " ".join([str(x) for x in cache.videos_in_cache()])
            output.write("{} {}\n".format(cache.id, videos_id))

    return