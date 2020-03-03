from movies_io import *
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
# test end-to-end, pass in single TMDb ID and return two lists: the box office info, and the IMDb info
tmdb_id = 466282
imdb_id = get_imdb_ID(tmdb_id)
box_office = get_box_office(imdb_id)
imdb_info = get_imdb_info(imdb_id)

print(imdb_id)
print(box_office)
print(imdb_info)