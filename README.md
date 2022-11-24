# 8일차

# 류원창

# 랜덤 영화 추천 페이지

- 랜덤 영화 추천 페이지는 처음 생각은 버튼을 누르면 아래에 영화 카드가 나오는 방식을 생각했는데,
- 이 과정이 생각보다 쉽지않다.
- 현재 영화 카드에 스타일이 잔뜩 들어가 있는데 내가 원하는 사이즈로 변경하는게 쉽지가 않다.
- 그래서 생각한 결론은 버튼을 누르면 랜덤으로 영화 디테일 페이지로 이동시키는 것이다.

![Untitled](8일차_류원창/Untitled.png)

# 페이지 다듬기

- 현재 페이지의 디테일적인 부분이 다듬어 지지 않았다.
- 시간이 없기 때문에 계획한 페이지들을 만들지 못할것같다.
- 또한 네브바의 늦은 도입으로 네브바의 style을 전역으로 사용하는데, 이 때 다른 컴포넌트에도 영향을 주기 때문에
- 현재 만들어진 페이지들을 전체적으로 다듬어야겠다.

# 장르별 영화 페이지 만들기 및 무한스크롤

- 장르별로 영화를 보여주는 페이지를 만들었고, 무한스크롤을 구현했다.
- 무한스크롤을 구현하는 쉬운 방식 중 하나는 inter어쩌구 api를 쓰는 것이었는데, 문서 보기가 시간이 없어서
- 그냥 현재 스크롤 위치와 전체 높이로 대충 계산해서 data에 영화정보를 가지고있는 배열에 넣어준다.

### 문제는 this

- mounted안에서 this는 vue를 가르키지만, mounted안의 이벤트리스너안은 this가 윈도우를 가르켜서 계속 오류가 떳다.
- 그래서, 이벤트리스너를 익명함수로 사용하였더니 this가 제대로 vue를 가르키고, 함수 또한 제대로 실행 되었다.

![Untitled](8일차_류원창/Untitled%201.png)

![Untitled](8일차_류원창/Untitled%202.png)

- 스크롤이 밑에 쪽에 있으면 계속 영화의 정보를 data에 넣어준다.

# 영화 조회 페이지 진행중

- 영화를 장르별 또는 전체를 보여주는 페이지를 만들어야하는데, 디자인은 강의실에서 좀 해놨다.
- 적절한 정보만 추가하면 될 것 같다.

![Untitled]8일차_류원창/Untitled%203.png)

- 왼쪽의 네비게이션은 급하게 생각나서 만든거라 이미 전체 카드의 배치의 틀을 잡아버렸는데,
- 추가적으로 네비게이션을 추가하기에는 시간이 오래걸린다.
- 포지션을  absolute로 잡아버려서 조정하는 수 밖에 없다. 지금은..

# 정리 완료

![Untitled](8일차_류원창/Untitled%204.png)

# 다듬기 거의 완료 오늘 마무리

![Untitled](8일차_류원창/Untitled%205.png)

&nbsp;
---
&nbsp;


# 이지은

- [x]  프로필 페이지 접근
- [x]  프로필 페이지에 찜 목록 / 방명록 기능 만들기
- [x]  소감 📕

# 프로필 페이지

### 방명록 기능

comments**/models.py**

```python
class Profile(models.Model):
    usernumber = models.IntegerField()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
```

`Profile, Comment 모델 정의`

- 로그인 후 Intropage 에 들어오면 **Profile usernumber DB** 가 저장되는 함수 작성하기
- usernumber이 저장되어 있어야 사용자가 usernumber을 id로 갖는 user 프로필에 접근해 댓글을 남길 수 있다.
- 그동안 계속해서 배웠던 article_id 에 접근해 comment 를 남기는 article-comment 관계를
- usernumber-comment 관계로 재정의
- usernumber는 하나의 게시글 번호와 같은 것이다
    
    ←- 유저_id 끼리 참조하는 방법을 몰라서 일단 이렇게 사용하기로 했다 —>
    

### 작업 순서

### 1.  회원가입 한 user_id / server의 [comments.app](http://comments.app) → Profile Models에 저장

- 회원가입을 한 사용자는 자동 로그인 후 TasteMovie.vue 로 이동하게 된다.
- TasteMovie 에서 가입한 유저의 id 를 db에 저장

1. `Vue` SignUp ****<  → methods → mapAction() > →
2.    **accountsStore**  → <actios(axios)> → 
3. `Django` → url → DB →
4. `Vue` →  **accountsStore** → getters → state

TastMovie.vue

```jsx
computed: {
    ...mapGetters(accountsStore, ["user", 'authHead']),
  },

  methods: {
    ...mapActions(commentsStore, ['createProfileUser'])
  },

  created() {
    console.log(this.user)
    this.createProfileUser({ usernumber: this.user.id,  authHead: this.authHead})
  },

```

```jsx
accountsStore

// 프로필 페이지 유저 정보 갖고오기
      getProfileUser( {commit, getters }, profileUserId ) {
        axios({
          method: "get",
          url: `${API_URL}/accounts/profile/${profileUserId.user}`,
          headers: getters.authHead,
        })
        .then((res) => {
          console.log('@@@@@@',res.data);
          commit('GET_PROFILE_USER', res.data.id)
        })
        .catch((err) => {
          console.log(err);
        });
      },
```

**comments-profile-DB**

| id | usernumber |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| … | … |

## 📕`DB에 이런 식으로 저장하는 이유`

현재 로그인 중인 사용자 A (  user_pk = 1) 가 사용자 B( user_id = 10 ) 의 프로필 페이지에 접근하여 댓글을 작성한다면 총 2개의 user data 가 필요하다.

하나의 모델에 두개의 유저 데이터를 쓰는 방법을 생각하지 못했다. 

모델 관계를 어떻게 정의 할 지 몰라서 일단은 회원가입 한 user의 id 를 username에 모두 저장해 두었다.

A가 B의 프로필 페이지에 들어가 댓글을 단다면 Comment.Model의 profile = 10 , user_id=1 이 된다.  이렇게 되면 Article-Comment 모델 처럼 쉽게 CRUD가 가능해진다.

프로젝트 기간이 촉박하여 두 유저가 직접 연결될 수 있는 방법을 생각하지는 못했지만, 플젝이 끝나고 해결책을 다시 한번 생각해보고싶다.  

 

### 2. Serverer < - > Clint  ⇒  CRUD

**Django comments/urls**

```python
urlpatterns = [
    # 프로필 유저 생성
    path('profileuser/', views.profileuser_list, name='profileuser_list'),
  
    # 프로필 유저 전체 댓글 조회(GET)
    path('profileuser/<int:profile_pk>/comments/', views.comment_list, name='comment_list'),
    # 프로필 유저 댓글 생성(POST)
    path('profileuser/<int:profile_pk>/comment/', views.comment_create, name='comment_create'),
    # 프로필 유저 댓글 삭제 (DELETE)
    path('profileuser/<int:profile_pk>/comment/<int:comment_pk>/', views.comment_delete, name = 'comment_delete'),
]
```

**Django comments/views**

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from comments.serializers import ProfileSerializer, CommentSerializer, ProfileListSerializer
from comments.models import Comment, Profile
from django.contrib.auth import get_user_model

# 회원가입 한 유저id 조회(GET), 생성(POST)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profileuser_list(request):
    print(request)
    if request.method == 'GET':
        profiles = get_list_or_404(Profile.objects.order_by('-pk'))
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 유저 프로필 페이지 댓글 조회(GET), 생성(POST), 삭제(DELETE)

@api_view(['GET'])
def comment_list(request, profile_pk):
# 프로필 유저 전체 댓글 조회(GET)
    profile = get_object_or_404(Profile, pk=profile_pk)
    comments = profile.comment_set.all()
    # 역참조 profile : comment 1:N
    serializers = CommentSerializer(comments, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_create(request, profile_pk):
# 프로필 유저 댓글 생성(POST)
    profile = get_object_or_404(Profile, pk=profile_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, profile = profile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_delete(request, profile_pk, comment_pk):

    comment = get_object_or_404(Comment, pk=comment_pk)
    # 상세 댓글 .filter(pk=comment_pk)
    if request.user == comment.user:
    # 댓글 작성자와 같은 경우 
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)
```

**VUE commentsStore**

```jsx
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const commentssStore = {
  namespaced: true,
  state: {
    comments: null,
  },

  getters: {
    comments: (state) => state.comments,
  },

  mutations: {
    CREATE_COMMENT: (state, comment) => (state.comments.unshift(comment)),
    GET_COMMENTS: (state, comments) => (state.comments = comments),
  },

  actions:{
  createProfileUser( { commit }, profileUser ) {
    axios({  
      method: "post",
      url: `${API_URL}/comments/profileuser/`,
      data: {...profileUser},
      headers: profileUser.authHead
    })
    .then((res) => {
      commit
      console.log( '프로필 유저 생성 완료', res.data)
    })
    .catch((err) => {
      console.log(err)
    })
  },

  // 댓글 생성 
  createComment( { commit }, commentItem) {
    axios({
      method: "post",
      url: `${API_URL}/comments/profileuser/${commentItem.profile}/comment/`,
      data: {content: commentItem.content},
      headers: commentItem.authHead,
    })
    .then((res) => {
      alert('댓글 작성 완료!.')
      commit('CREATE_COMMENT', res.data)
      commit
    })
    .catch((err) => {
      console.log(err)
    })
  },

  // 댓글 조회(GET)
  getComments( { commit }, profileItem) {
    axios({
      method: "get",
      url: `${API_URL}/comments/profileuser/${profileItem.id}/comments/`,
      headers: profileItem.token,
    })
    .then((res) => {
      commit("GET_COMMENTS", res.data);
    })
    .catch((err) => {
      console.log(err)
    })
  },
```