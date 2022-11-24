from django.http import JsonResponse, HttpResponse
import requests
from movies.models import Genre, Movie, Actor, Nowplaying

# 여기에 내 api key를 넣어주세요
API_KEY = '0d169ae4fecc50f95828ef6ee1b664e9'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'
NOW_PLAYING_URL = 'https://api.themoviedb.org/3/movie/now_playing'

def tmdb_genres():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        print(genre)
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)


def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
        movie.actors.add(actor_id)
        if movie.actors.count() == 7:       # 7명의 배우 정보만 저장
            break

def movie_data(page=1):
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)

        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        get_actors(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)    

def now_playing_data(page=1): # 현재 상영중인 영화 20편 저장
    response = requests.get(
    NOW_PLAYING_URL,
    params={
        'api_key': API_KEY,
        'language': 'ko-KR',            
        }
    ).json()    
    for movie_dic in response.get('results'):
        if not movie_dic.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dic)
        now_movie = Nowplaying.objects.create(
            id=movie_dic.get('id'),
            title=movie_dic.get('title'),
            release_date=movie_dic.get('release_date'),
            popularity=movie_dic.get('popularity'),
            vote_count=movie_dic.get('vote_count'),
            vote_average=movie_dic.get('vote_average'),
            overview=movie_dic.get('overview'),
            poster_path=movie_dic.get('poster_path'),
            youtube_key=youtube_key          
        )

        # --------  현재 상형 중인 영화20개 모두 movie_data 안에 들어있어서 따로 actor / genre 저장 처리를 해줄 필요가 없음
        # for genre_id in movie_dic.get('genre_ids', []):
        #     now_movie.genres.add(genre_id)


        print('>>> 현재 상영중인 영화 ==>', now_movie.title, '==>', now_movie.youtube_key)    

def tmdb_data(request):
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    # Movie.objects.all().delete()
    Nowplaying.objects.all().delete()
    now_playing_data(1)
    tmdb_genres()
    for i in range(1, 60):
        movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')