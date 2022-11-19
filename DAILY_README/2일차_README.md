# 2일차

# 류원창

개발목록: 유저 기능 관련
날짜: 2022년 11월 17일

할 일

- [x]  유저 정보 수정
- [x]  유저 비밀번호 수정
- [x]  유저가 선택할 프로필 이미지 구하기
- [ ]  팔로우, 팔로잉 기능 구현하기
- [x]  유저 관련 기능을 위한 장고 api만들기
- [x]  로그인, 회원가입 퍼블리싱
- [ ]  유저 정보 수정 페이지 만들기

# 유저 로그아웃

- 유저 로그아웃은 dj-rest-auth에서 제공하는 api를 사용하고,
- 현재 vuex에 저장되어 있는 token과 user정보를 없애면 될 것같다.

로그아웃 함수

![Untitled](2일차_류원창/Untitled.png)

# 유저 정보 수정

- 유저 정보 수정은 어제 만들어 놓은 유저 정보를 제공하는 api를 사용하면 될 것 같다.
- 정보 수정 함수는 메서드를 PUT으로 요청 보내고, 받은 정보를 다시 SET_USER로 정해주면 될 것같다.

유저 정보 수정 함수

![Untitled](2일차_류원창/Untitled%201.png)

## 문제 1 장고 serializer관련

- 데이터를 수정한 데이터를 보냈으나, 시리얼라이저를 다시 저장해야 한다.
- 이 과정에서 처음엔 단순히

```python
serializer = UserSerializer(person, data=request.data)
serializer.save()
return Response(serializer.data)
```

- 위와 같은 코드를 작성하였으나, serializer가 유효한지 검사하라는 에러가 떳다.

## 해결

```python
@api_view(['GET', 'PUT'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = UserSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(person, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

- GET요청과 PUT요청에 대한 기능을 나누어 준다.

![Untitled](2일차_류원창/Untitled%202.png)

![Untitled](2일차_류원창/Untitled%203.png)

## 비밀번호 변경

- 비밀번호 변경은 dj-rest-auth에서 제공하는 api로 충분하다.

문서

![Untitled](2일차_류원창/Untitled%204.png)

- 기존 비밀번호와 새로운 비밀번호를 보내면 될 것 같다.
- `LOGOUT_ON_PASSWORD_CHANGE = False` 은 비밀번호를 변경해도 로그인 상태를 유지하는 옵션인 것 같다.

비밀번호 변경 함수

```jsx
editPassword({ getters }, password) {
        // console.log(password);
        axios({
          method: 'post',
          url: `${API_URL}/accounts/password/change/`,
          headers: getters.authHead,
          data: { ...password }, 
        })
        .then(() => {
          console.log('비밀번호 변경에 성공했습니다.');
        })
        .catch(err => {
          console.log(err);
        })
      },
```

- 정상 작동한다.

# 회원가입, 로그인 사이트 퍼블리싱

- css부분은 tailwind라는 프레임워크를 사용한다.
- 회원가입과 로그인의 기능에 대해서는 이미 만들었으니 페이지를 만들고 기능을 달아주면 된다.

### 회원가입 사이트

![Untitled](2일차_류원창/Untitled%205.png)

### 로그인 사이트

![Untitled](2일차_류원창/Untitled%206.png)

- 각 사이트에서 사용하는 이미지는 달라질 수 도 있고, 랜덤으로 바뀔 수 있다. (예정)

## 회의

- 현재 작업 방식으로는 서로 뭘하는지 정확히 알 수가 없고, 체계적으로 움직이는 느낌이 아니라 회의를 했다.
- 각자 서로의 할 일을 명확히 정하고 보고하고 노션에 기록하기로 했다.

# 정보 수정 페이지 만들기

- 일단, 우리의 아이디어는 유저는 넷플릭스와 같이 정보 수정 페이지에서 자신의 프로필 이미지를 선택할 수 있다.
- 그러기 위해서는 사전 작업이 좀 필요하다.
- 현재 유저의 정보는 username, nickname, password, profile_path라는 필드를 가지고 있는데,
- 기본적으로 회원가입할 때 에는 profile_path를 받지 않는다.
- 디폴트 값으로 넣어줄 작업이 백엔드 서버에서 필요하다
- `[serializers.py](http://serializers.py)` 를 수정하면 된다.

![Untitled](2일차_류원창/Untitled%207.png)

회원 가입 후 데이터베이스 확인

![Untitled](2일차_류원창/Untitled%208.png)

- 정상 작동 된다.

### 정보 수정 페이지 프로토타입

- 우리가 만들 정보 수정페이지는 단순히 데이터를 입력 받고, 수정하는 것이 메인이 아니다.
- 중요한 점은 몇개의 이미지를 제공하여 이미지를 클릭하면, 그 이미지의 src속성을 user의 profile_path로 수정해주는게 핵심이다.
- 아래는 페이지의 프로토타입이다.

![Untitled](2일차_류원창/Untitled%209.png)

- 기본 프로필은 페이지 상단에 있는 웃고있는 얼굴이다.
- 이제, 왼쪽의 이미지를 클릭하면 그 이미지의 src를 유저의 profile_path로 수정해줘야한다.

### script 코드와 간단한 문제 상황

```jsx
<script>
import { mapActions, mapGetters } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'EditUserView',
  data() {
    return {
        username: '',
        nickname: '',
        profile_path: '',
        old_password: '',
        new_password1: '',
        new_password2: '',
        msg: '닉네임를 입력해주세요!'
    };
  },
  methods: {
    ...mapActions(accountsStore, ['editUserInfo']),
    ...mapActions(accountsStore, ['editPassword']),
    test(event) {
      console.log(event.target.getAttribute('src'));
      this.profile_path = event.target.getAttribute('src');
      
    },
  },
  computed: {
    ...mapGetters(accountsStore, ['user']),
    // eslint-disable-next-line vue/return-in-computed-property
    
  },
  created() {
    this.nickname = this.user.nickname;
    this.profile_path = this.user.profile_path;
    this.username = this.user.username;
  }
};
</script>
```

- 대충 내용은 처음에 user의 정보를 받아와서 data의 각 필드에 매칭을 시켜준다.
- 그 후 내용을 입력 받거나 프로필 이미지를 선택하면 그 값들이 데이터에 다시 매핑된다
- profile_path의 경우 src속성의 문자열인데, 길다. 좀이 아니라 많이 길다.
- 초반에 모델에 설계 할 때 profile_path필드의 max_length를 500자로 했는데,
- 500자가 넘어서 계속 상태코드 400오류가 떳다.
- max_length를 수정해야겠다.

![Untitled](2일차_류원창/Untitled%2010.png)

### 글자수 문제 해결

![Untitled](2일차_류원창/Untitled%2011.png)

- 처음에 max_length를 3000으로 넉넉하게 줬다고 생각했는데, 이 또한 초과했었다.
- max_length에 한계가 있는지 두려웠지만 10000으로 줬더니 정상작동했다.

# 유저 정보 수정 페이지 대충 완료

![Untitled](2일차_류원창/Untitled%2012.png)

- 유저 정보 수정시, getUserInfo를 통해 다시 한번 유저의 정보를 데이터베이스에 요청한다.
- 현재 username과 nickname이 수정이 가능한데, username을 수정하는 경우, 다음에 요청을 보낼때 accounts/profile/<str:username>으로 요청을 보내는데, 이 과정에서 에러가 날 것 같다.
- 유저네임은 그냥 보여주기만 하고 수정은 불가능하도록 생각 중이다.
- **유효성검사와 라우팅 가드만 설정해주면 완벽해질 것 같다. 해야한다.**

&nbsp;

# 이지은

개발목록: django, javascript, vue
날짜: 2022년 11월 17일

- [x]  vuex , module 사용
- [x]  프로필 페이지 ui
- [x]  axios를 사용하여 DB의 데이터 받아오기

# Vuex, store module 사용

### 1. 디렉토리 구조 만들기

user를 관리하기 위한 스토어와

movie를 관리하기 위한 스토어를 나눠서 관리

<aside>
💡 store
├─modules
│  ├─accountsStore.js
│  ├─moviesStore.js
└index.js

</aside>

### 2. store index에 작성한 모듈 등록

**src/store/index.js**

```jsx
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 작성한 모듈가져오기
import accountsStore from '@/store/modules/accountsStore.js'
import moviesStore from '@/store/modules/moviesStore.js'

// 키 :값 형태로 저장
const store = new Vuex.Store({
  modules: {
    accountsStore,
    moviesStore
  }
})

export default store
```

### 3. module 관리

**src/store/modules/accountsStore.js**

```jsx
const accountsStore = {
  namespaced: true,

  state: {
    name: "",
  },

  getters: {
    name: (state) => state.user.name,
  },

  mutations: {
    SET_TOKEN: (state, token) => ( state.token = token ),
    SET_NAME: (state, user) => (state.user = user),
  },

  actions: {
		set_name: ({commit}) {
		commit('SET_NAME', name)
	}
```

### 4. 다른 컴포넌트에서 vuex- module 데이터 접근

 

**src/views/TempView.vue**

```jsx
<script>
import { mapActions } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'tempView',

  data() {
    return {
      username: '',
    };
  },
  methods: {
    ...mapActions(accountsStore, ['methods_name']),
  },
};
</script>
```

### ⇒ **다른 컴포넌트에서 vuex 데이터 접근 시 유의 할 점**

=> 만약 **모듈이 독립적으로 사용되길 원한다면, namespaced: true라고 각 store에 명시**하면 된다.

하지만 **state** 접근시에는 달라진다.

`$store.state.state값 => **$store.state.명시된 store 모듈 이름.state값** 으로 접근해야한다.`

mapActions 이나 mapGetters 를 사용할 경우

 `...mapActions(accountsStore, ['methods_name']) 방식을 사용해서 접근해야한다.`

### 

## Figma 를 사용 하여 프로필 페이지 UI잡기

![Untitled](2일차_이지은/Untitled.png)