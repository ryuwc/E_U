# 4일차

# 류원창

개발목록: 리뷰 좋아요 싫어요 모델링
날짜: 2022년 11월 19일

할 일

- [x]  영화 정보 axios요청 매번 보내는거 개선 필요 회의
- [x]  리뷰 좋아요, 싫어요 재 모델링

# 리뷰 생성 serializer, view수정

- 기존 작성되있던 방식 보다 더 알맞은 방법이 필요하다는 것을 느꼇고 수정하였다.

![Untitled](4일차_류원창/Untitled.png)

![Untitled](4일차_류원창/Untitled%201.png)

- movies/<int:movie_pk>/review/ 로 post요청을 보내면 된다.
- 이때 필드는 content, user, movie, rank 를 보낸다

# 리뷰 좋아요, 싫어요 모델링

- 이 프로젝트는 리뷰에 대해 좋아요와 싫어요 기능을 구현할 것 인데,
- 좋아요 한 유저와 싫어요 한 유저의 모델링이 서로 뒤바뀌었다.

![Untitled](4일차_류원창/Untitled%202.png)

- 현재는 이 상황인데, bad_user_id가 여러개일 수 있다.
- 생각해보니 포린키가 아닌 매니투매니가 맞는거같다.

### 모델 필드 수정

![Untitled](4일차_류원창/Untitled%203.png)

![Untitled](4일차_류원창/Untitled%204.png)

- 이러한 방식의 모델이 더 적절하다.

### 리뷰 좋아요, 싫어요 api만들기

### url

![Untitled](4일차_류원창/Untitled%205.png)

### view

![Untitled](4일차_류원창/Untitled%206.png)

### 포스트맨

![Untitled](4일차_류원창/Untitled%207.png)

### 모델

![Untitled](4일차_류원창/Untitled%208.png)

- url은 위에 적힌대로 보내고 post로 유저의 정보만 보내면
- 좋아요와 싫어요과 토글링 된다.

### 작은 에러

- 새로운 폴더에 작업 파일을 넣고 npm run serve를 돌렸는데 아래와 같은 에러가 뜸

![Untitled](4일차_류원창/Untitled%209.png)

### 해결

- 폴더명 경로중에 특수문자가 들어 있어서 안되었다. 폴더명 바꾸니 해결

# 유저 회원가입후 영화 찜 하는 페이지

- 기본적으로 유저는 회원가입 후 첫 로그인시 몇개의 영화를 보여주며 찜 하라고 한다.
- 이때 이 페이지에서 영화 데이터에 접근 할 수 있도록 해야겠다.

![Untitled](4일차_류원창/Untitled%2010.png)

- 기본적으로 n개의 영화를 페이지 렌더링 되자마자 띄운다.
- 더 보기 버튼을 누르면 n개의 영화가 다시 추가되며 렌더링 된다.

![Untitled](4일차_류원창/Untitled%2011.png)

- 지금 보니 영화의 포스터가 저화질이다.
- 개선 가능한지 확인해봐야겠다.

## 고화질 포스터 패스 관련

- tmdb에서는 기본적으로 poster_path를 /asdfawefasdsafd.jpg 형태로 제공한다.

![Untitled](4일차_류원창/Untitled%2012.png)

- 직접된 영화의 포스터는 앞에 특정 tmdb사이트의 url을 적어줘야 한다.
- 이 과정에서 w-숫자 라는 url이 있는데 이 부분을 original으로 적어주면 고화질의 포스터를 얻을 수 있다.

![Untitled](4일차_류원창/Untitled%2013.png)

![Untitled](4일차_류원창/Untitled%2014.png)

- 기존보다 훨씬 좋다.

&nbsp;

&nbsp;

# 이지은

개발목록: 영화 디테일 페이지

- [x]  영화 디테일 페이지 레이아웃 및 UI

## 

# 영화 디테일 페이지 레이아웃 및 UI

![Untitled](4일차_이지은/Untitled.png)

- **다테일 페이지 상단 Nav 바**
- **디테일 페이지 컴포넌트 구조**
    
    **MovieDetailInfo**
    
    **└MovieDetailR**
    
    **│  ├MovieReview**
    
    **│  ├MovieClup**
    

## MovieDetailInfo

- MovieDetailInfo  좌측에서 2/3 까지 영화에 대한 상세 정보 안내 페이지
- 배경은 movie의 poster_path + 반투명 어두운 배경
- 하단에 해당 영화의 이미지 나열 ⇒ 가로 스크롤바 적용
- + 이미지 TMDB의 movie_Image 사용

==⇒ TMDB 에서 영화 이미지에 대한 axios 요청을 통해 그때 마다 영화이미지 불러오기 / dump 데이터 저장 X

## MovieDetailR

 

- MovieDetailInfo 페이지 , 우측으로 부터 1/3 지점
- 영화 평점 및 리뷰 | 무비클립 버튼
- 버튼을 바꿔 누를 때 마다 보여지는 컴포넌트가 바뀜

```python
<template>
  <div>
    <h1>MovieDetailR</h1>
    <div>
        <button @click="currentTab = 'MovieReview'">리뷰 및 평점</button>
        <button @click="currentTab = 'MovieClip'">무비 클립</button>
        <component :is="currentTabComponent"></component>
    </div>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue'
import MovieClip from '@/components/MovieClip'
export default {
    name: 'MovieDetailR',
    components: {
        MovieReview,
        MovieClip
    },
    data() {
        return {
            currentTab: 'review'
        }
    },
    computed: {
        currentTabComponent() {
            return this.currentTab
        }
    }
}
```

**`v-on / v-bind 사용`**
