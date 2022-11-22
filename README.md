# 7일차

할 일

- [ ]  비디오 프레임 받아와서 디테일 페이지에 적절히 배치하기

# 유튜브 영상 받아오기

- 친절히도 tmdb에서는 영화에 대한 video를 제공해주는 api가 있다.

![Untitled](7일차_류원창/Untitled.png)

- 적절히 보내서 영화의 비디오에 대한 정보를 가져오면 되겠다.

![Untitled](7일차_류원창/Untitled%201.png)

- 영화의 비디오 정보를 요청해서 데이터에 저장한다.
- 이 때 지금 컴포넌트의 컴포넌트를 불러오는 구조로 되어있어 vuex가 필요하다
- vuex에 데이터를 저장해서 사용해야 될 것 같다.
- 이제 각 비디오에 대한 리스트를 만들고 그걸 누르면 재생이 되는 모달을 띄우면 될 것같은데
- 썸네일을 사용해야 할 것 같은데 썸네일에 관한 정보는 제공해주지 않는다.
- 방법을 찾아보자

### 썸네일을 찾을 수 있을 것 같다.

- tmdb의 영화 디테일의 트레일러 재생 a태그를 살펴보니 backgroud이미지의 주소를 알아냈다.
- 아래는 tmdb의 태그

```html
<div class="wrapper" style="background-image: url('https://i.ytimg.com/vi/1pbjFu6aIZg/hqdefault.jpg');">
  <a class="no_click play_trailer" href="/video/play?key=1pbjFu6aIZg" data-site="YouTube" data-id="1pbjFu6aIZg" data-title="[블랙 아담] 코믹콘 영상"><div class="play_background"><span class="glyphicons_v2 play invert svg"></span></div></a>
</div>
```

- 저 주소에 iframe재생을 위한 키를 vi/여기/ 에 입력했더니 가져오는 것 같다
- 썸네일은 저 주소를 이용해 접근하면 될 것 같다.

### 영화 비디오 요청 문제 및 해결

- created에 영화 비디오 가져오는 함수를 호출하고, console에 data에 있는 영화비디오정보를 찍어봤다.
- 근데, 순서가 이상하다. 비동기 처리가 되어서 비디오를 가져오기 전에 호출되는 것 같다.

![Untitled](7일차_류원창/Untitled%202.png)

- 위의 예시를 보면, 코드는 분명히 데이터를 가져오는 함수를 먼저 호출하고, 데이터를 출력했는데
- response가 더 늦게 오는 걸 확인했다.
- setTimeout을 활용하면 되겠다.

![Untitled](7일차_류원창/Untitled%203.png)

![Untitled](7일차_류원창/Untitled%204.png)

- 시간을 1초정도로 주면 될 것 같다. 후에 다른 영화 확인 후 더 필요하면 추가하도록 한다.

![Untitled](7일차_류원창/Untitled%205.png)

![Untitled](7일차_류원창/Untitled%206.png)

- 일단 하나 해결

# 내일의 나에게

- 일단 영화 디테일 페이지에서 비디오 정보까지 받아서 vuex에 저장했으니 적절히 활용하도록 해

![Untitled](7일차_류원창/Untitled%207.png)

- 대충 이런식으로 짜고 저거 누르면 iframe포함한 모달 띄울거야
- [`https://i.ytimg.com/vi/ZS_8btMjx2U/hqdefault.jpg`](https://i.ytimg.com/vi/ZS_8btMjx2U/hqdefault.jpg) 이게 썸네일 가져오는 url
- 일단 난 온보딩 스크롤 이벤트좀 해야될듯

# 영화 프레임

- 영화 프레임은 위와 같은 디자인으로 만든다.
- 저 이미지를 클릭하면, 모달로 유튜브 프리뷰가 띄어지게 할 것이다.

![Untitled](7일차_류원창/Untitled%208.png)

- 위의 주소가 썸네일을 가져오는 주소가 맞았다.
- 이제 가운데에 누르면 재생할 것 같은 버튼을 넣었어야 되는데, 적절한 이미지를 가져왔다.
- 이 과정에서 css의 position에 관한 지식을 좀 배웠다.
- 일단은, 저런 형식으로 씌울려면 유튜브 버튼이 자식이고 저 썸네일이 부모다
- 이제 부모의 포지션을 related로 주고, 자식의 포지션을 absolute로 주어 top과 left를 조절하면 된다.

![Untitled](7일차_류원창/Untitled%209.png)

- 시간이 없어서 태그들이 너무 보기가 싫다.
- 다음부턴 체계적으로 정리하기로 한다.

### 프리뷰 모달창 완료

- 모달 창 자체는 저번에 만들어논 삭제 버튼을 누르면 나타나는 모달을 재활용했다.
- 영화 썸네일은 v-for로 계속 돌며 이중 하나를 클릭하면 clickVideo함수에 그 상태의 video.key를 매개변수로 전해준다.
- 이 매개변수를 데이터에 저장하여 ifram의 url주소로 활용한다.
- 코드는 아래의 이미지를 참조

![Untitled](7일차_류원창/Untitled%2010.png)

![Untitled](7일차_류원창/Untitled%2011.png)

![Untitled](7일차_류원창/Untitled%2012.png)

# 영화 찜 api만들기

- 영화 찜 하는 api만드는 것은 생각보다 간단했다.
- 기존에 존재하는 영화 디테일을 조회하는 url에 post요청으로 추가하면 된다.
- 자세한건 아래 코드 참고

```python
# 영화 디테일 조회(GET), 영화 찜하기(POST)
# 찜할 때는 메서드는 그냥 POST로 data없이 보내면 된다. (보낼 때의 토큰이 해당 유저와 매칭시킨다.)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 조회(GET)일 경우
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # 찜하기(POST)일 경우
    elif request.method == 'POST':
        # 찜하기는 로그인한 유저만 가능하다.
        # 찜하기를 누른 유저가 이미 찜을 눌렀는지 확인
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            movie_like = False
        else:
            movie.like_users.add(request.user)
            movie_like = True
        context = {
            'msg': '찜하기 or 찜취소 접근 성공',
            'movie_like': movie_like,
        }
        return Response(context, status=status.HTTP_201_CREATED)
```

![Untitled](7일차_류원창/Untitled%2013.png)

# 페이지에서 찜하기 또는 취소 요청보내기

- 영화 디테일 페이지에서 현재 로그인된 유저가 요청을 보낼 수 있어야 한다.
- 페이지의 적절한 곳에 찜하기, 취소하기 버튼을 만들어야 한다.

![Untitled](7일차_류원창/Untitled%2014.png)

![Untitled](7일차_류원창/Untitled%2015.png)

- 버튼을 만들었고 함수도 정상적으로 실행이된다.
- 근데 좀 이게 생각보다 복잡하다. 일단, 처음 위시리스트 모델을 가져와야 되고, 그 모델에 맞는 유저가
- 위시리스트에 담았는지 확인하고 어떤 버튼을 보여줄지 정해야 한다.
- 일단, 전체 위시리스트를 가져와서 moviesStore에 저장하는 함수를 만들어야한다.
- 먼저 백엔드에서 전체 위시리스트를 조회할 수 있는 api를 만들어야한다.

# manytomany로 연결된 모델 가져오기

- 현재 manytomany라는 데이베이스는 만들어졌지만, 이에 대한 모델은 없어서
- 가져오려면 영화 전체 데이터를 조회해서 그 안에서 필터를 돌려야 한다.
- 하지만 이 방법은 너무 비효율적이다. 또한, 양이 적은 user테이블에서 정보를 가져오려고 했는데,
- dj-rest-auth의 방식이 제공을 안하는 것인지 역참조가 조회가 되지 않는다.
- 그래서 찾은 방법이 중간 모델을 이요하면 될 것 같다. 아래의 블로그를 보며 따라해보면 될 것 같다.

![Untitled](7일차_류원창/Untitled%2016.png)

- 위의 방법이 사용이 잘 안된다. 애초에 User모델은 다른 앱에 있다. 그리고 다른 에러도 뜬다.
- 그래서 생각나는대로 코드를 짜봤는데, 전체 위시리스트를 조회하는 것이 아닌
- 특정 유저의 위시리스트에 담은 영화 정보를 조회하는 것이다.

![Untitled](7일차_류원창/Untitled%2017.png)

![Untitled](7일차_류원창/Untitled%2018.png)

![Untitled](7일차_류원창/Untitled%2019.png)

- 이정도로 될 것 같다.

## 위의 것 변경

- 위의 api는 토큰을 통해 현재 유저가 위시리스트에 담은 정보를 보여준다.
- 다른 유저가 위시리스트에 담은것은 보지 못한다.
- 아래는 수정본이다. 자신이 아닌 특정 유저가 위시리스트에 담은 영화를 조회할 수 있다.

![Untitled](7일차_류원창/Untitled%2020.png)

![Untitled](7일차_류원창/Untitled%2021.png)

## 디테일 페이지 다듬기

![Untitled](77일차_류원창/Untitled%2022.png)

- 이정도면 될 것 같다..

## 위시리스트 관련 함수, vuex만들기

- 특정 유저의 위시리스트를 조회할 수 있는 api를 만들었으니, vue에서 사용하도록 한다.

![Untitled](7일차_류원창/Untitled%2023.png)

![Untitled](7일차_류원창/Untitled%2024.png)

- 이제 이 현재 페이지의 영화를 찜 했는지 확인이 필요하다.
- 찜 했을 경우와 아닐 경우에 보여줄 버튼이 다르기 때문이다.
- axios요청이 제대로 오면 함수를 실행하도록 하자
- 생각한대로 머리랑 몸이 안따라준다.