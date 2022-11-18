# 3일차

개발목록: django
날짜: 2022년 11월 18일

- [x]  django - vue 연동하여 movie detail  정보 불러오기
- [x]  django review 모델 정의 ⇒
- [ ]  11.19 에 good_user / bad_user 다시 정의
- [x]  review CRUD
- [ ]  django - vue 연동하여 movie detail  페이지에서 리뷰 CRUD → 조회만 완성
- [x]  README_ 3일차 소감 📕

## DB → Vue / movie detail  정보 불러오기

### …mapActions 인자 넘기기 문제 해결

movie detail 페이지로 이동 시 `mapActions에 ‘movieId’` 인자 함께 넘겨주기

```jsx
const moviesStore = 'moviesStore'

export default {
  name: 'MovieDetailInfoView',
  computed: {
    ...mapGetters(moviesStore, ['movie']),
  },
  methods: {
    ...mapActions(moviesStore, ['getMovieDetail']),
  },
  created() {
    const movieId = this.$route.params.id
    this.getMovieDetail(movieId)
  }
}
```

params로 넘겨 받은 인자를 store/modules/moviesStore의 actions 인자로 넘겨 주기.

 변수로 선언 후에   `this.getMovieDetail(movieId)` 처리

## Review 모델 정의

**back-end/movies/models.py**

```python
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    good_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='good_reviews')
    bad_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='bad_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

![Untitled](3일차_이지은/Untitled.png)

movie - review ⇒

- review-movie ⇒ 1:N
- reivew-user ⇒ 1:N
- review-good_user ⇒ 1:N
- review-bad_user ⇒ 1:N

rank ⇒ 영화 평점

good_user ⇒ 리뷰 좋아요를 누른 사용자

bad_user ⇒ 리뷰 싫어요를 누른 사용자 

—>유저가 N / review 가 1 dls 1:N 관계 =⇒ User Model 에서 FK 다시 정의 

## Review(CRUD)

**back-end/movies/views.py**

```python

# movie_Detail -> 전체 리뷰 조회(GET) 리뷰 생성(POST)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.filter(movie_id=movie_pk)
    # 외래키의 movie_id가 movie_pk와 일치하는 경우 .filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    # 복수 객체
    return Response(serializer.data)
  else:
  # 생성(POST)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        # user, movie 외래키 참조 객체 설정
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_detail(request, review_pk):
# movie_Detail -> 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        if request.user == review.user:
            # 작성자와 같은 경우
            if request.method == 'DELETE':
                review.delete()
                data = {
                    f'{review_pk}번 리뷰가 삭제되었습니다.'
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            if request.method == 'PUT':
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
            # 작성자와 다른 경우
```

## postman 을 이용하여 DB에 review 작성하기

### ****Error Response****

**HTTP Status Code**

`401 Unauthorized`

-로그인 되지 않은 사용자에게 요청이 들어올 경우 / 로그인 정보가 잘못된 경우

```
{
"detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
}

```

### ERR 해결 방안

### **Permission**

`IsAuthenticatedOrReadOnly`

인증된 user만 요청에 성공 할 수 있으며,  인증되지 않은 user는 읽기(method `GET`)만 가능합니다.

**Token인증 방법**

아래와 같이 헤더에 Token값을 입력하여 요청을 보냅니다.

![Untitled](3일차_이지은/Untitled%201.png)

![Untitled](3일차_이지은/Untitled%202.png)

**⇒ 정상 응답 확인**

→ 이 때 good_user 과 bad_user의 FK 에 null=True 를 해 줄 경우 빈 값 사용 가능

## 

## 📕3일차 소감

 3일차가 되어서야 프로젝트 진행에 탄력을 받은 느낌이다. 

1, 2 일차에는 프로젝트 진행 속도가 느렸고 README 정리도 생각한 만큼 잘 하지 못했다.

집에서 프로젝트한 것이 강의실에서 보다 업무 효율이 더 높았고, 이번 온라인 수업을 통해 재택근무가 내게 더 맞지 않을까 하는 생각이 들었다.

페어프로그래밍 진행도 강의실에서보다 원활히 진행되었다. 

페어인 원창님과 디스코드 화면 공유를 통해 프로젝트에 대해 이야기를 나누고 서로의 코드를 리뷰, 합병하는 것이 앞선 이틀의 페어프로그래밍 보다 더 잘되었다. 

  

**-배운 것**

Review-Movie-User 모델의 관계를 정리하며 1:N  or N:M 관계의 모델들이 서로 어떤 식으로 데이터를 참조하는지 정리가 되었다.