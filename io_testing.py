from movies_io import *
import time
'''
# test getting single IMDb ID from a TMDb ID
tmdb_id = 475303
imdb_id = get_imdb_ID(tmdb_id)
print(imdb_id)
'''
'''
# test getting box office numbers from a single IMDb ID
imdb_id = 'tt1502397'
box_office = get_box_office(imdb_id)
print(box_office)
'''
'''
# test getting IMDb info from a single IMDb ID
imdb_id = 'tt1502397'
imdb_info = get_imdb_info(imdb_id)
print(imdb_info)
'''
'''
# test end-to-end, pass in single TMDb ID and return two lists: the box office info, and the IMDb info
tmdb_id = 8835
imdb_id = get_imdb_ID(tmdb_id)
box_office = get_box_office(imdb_id)
imdb_info = get_imdb_info(imdb_id)

print(imdb_id)
print(box_office)
print(imdb_info)
'''

# test end-to-end, pass in multiple TMDb IDs and return multiple sets of two lists: the box office info, and the IMDb info

tmdb_ids = [458897, 8835, 512200, 399174]
for id in tmdb_ids:
    imdb_id = get_imdb_ID(id)
    movie_details = get_movie_details(id)
    box_office = get_box_office(imdb_id)
    imdb_info = get_imdb_info(imdb_id)

    print(imdb_id)
    print(movie_details)
    print(box_office)
    print(imdb_info)
    time.sleep(1)
