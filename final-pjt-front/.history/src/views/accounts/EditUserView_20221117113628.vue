<template>
  <div>
    <h4>회원정보수정</h4>
    <form>
      <div>
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model="nickname">
      </div>
      <div>
        <label for="profile_path">프로필 이미지</label>
        <input type="text" id="profile_path" v-model="profile_path">
      </div>
      <div>
        <button type="button" @click="editUserInfo({ nickname: nickname, profile_path: profile_path })">수정</button>
      </div>
      <div>
        <label for="old_password">현재 비밀번호</label>
        <input type="password" id="old_password" v-model="old_password">
      </div>
      <div>
        <label for="new_password">새 비밀번호</label>
        <input type="password" id="new_password1" v-model="new_password1">
      </div>
      <div>
        <label for="new_password_check">새 비밀번호 확인</label>
        <input type="password" id="new_password2" v-model="new_password2">
      </div>
      <div>
        <button type="button" @click="editPassword({ old_password: old_password, new_password1: new_password1, new_password2: new_password2 })">비밀번호 변경</button>
      </div>
    </form>
    // 프로필 이미지 모음
    <div>
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAPPklEQVR4nO2df3hU5ZXHv+e9d+YmM/kdJID8UCEkCIoVIj9XSbJ2S1fXIhvrPo/u2rVr9+kKVljLPoLudNusVkH3qdhS0N0F6a5FWnzKWlxtQlagQUBCRSBIKBb5GZKZBDKT+XXfs39MIglJJvPjvTOBp59/eLj3veecvGfen+fc9xKuQaqqquxut7uKme9j5plEdB0AGwATwBkAbzudzuVbt271pddSgNJtgGoqKiqqAPwbgFGDFA0DWFVbW/tP1ls1MCKdylXicrlEeXn5agCbEKn8QwAWCyFubm9vt0sp84loAYBfAvAD0AEsq6io2I801sM10wLKy8tXE9E/AAgAeOrOO+981eVyyf7KPvbYY7ampqYNAB7sutRQW1t7e6ps7ck14YDy8vIHiOjnAALMfN/27dv/N1r5qqoqe0tLy71EtBzAl3rcCgE4S0Rvm6a5vK6ursNKu4FrwAFVVVX21tbWowBuAPBUbW3tymjly8vL7yeilwCMG0R0WEq5qq6uztIx4qpyAG+fp2PUpZkSVAagjKW4SYKLpEnDdY0dAIGILwE4S8ApBo6C8IkQXH+44cZDi9a0vgDgiS5xBwGsI6L/Y+Y9AAxm/hWAABHdCyADAIiooaamZjqAfruzZLkqHMBHZkyTJB8F8JcArktERihMoT2faLY9h/XwoeNi+bji8pXdY0RFRcVbXbL/UFtbe0NVVZXmdrs3MvODwBdOsGSMGNIO4CPTbmES1QzcA7W2BonxjhS8Tpu4792KivK/IKK3AYRqa2vt3YUqKyuXMvNKACCiF2tqar6r0AYAQ3Qaytvn6WZj2TOSxEcM3Av1PxQ7ExYQ06/lp2UH1zzrH911Xe9ZqKamZlXX4A5mfnLevHlZiu0Yeg7gxjnZPMr7awD/gsjq1WKFmDy60FwNAETgK2+PHz/+YXStG4QQ31etfkg5gE/clicRrGPG3anUe6410sBGDpPCbJz+Gh+bkdN9b+3atSEi+p+u/96vWveQcQAfm2CYAdsWAClfEDU0agCAknEmAHpUmvwxH5v+xfpASrkRAJh5pGrdQ8YBUua9SMC81OsFtu2KjLtzbwt3XeVx0qQd4SNl9wOAzWar77qhvEscEg4INZZ9BUyPp0P31h12nDgjMKKQMXuq2fOWkwibwkenP2gYhgQAIvWTxrQ7gE/MyxDAq0jTlPhgU6QK/n6hH7rWZwzWiGnDgrs8TwAAM4dU69cHL2ItMuj9DoCb0qX/6W/4MW9aGHO+6H76YHNm8jIAIKKzqvWntQXwoclZYPxjOm0Qomff3xdmwnv1ug0AdI3fVq5ftcB4kCLzEQCF6bRhMLZ+YMOJMxpGFDLefM57RrX89I4BRN9Mq/4YOHj88hiRm8XL+MgdSn8wadsL4iNlsyVhV7r0x4qUwG8/1nt0U7RMK93zgir5aWsBkujRdOmOh75jBH9Dpfy0tAA+NNkuNcc5APnp0J8sAlRGpXv2qZGVBkzh/DKu0soHAAk5V5WstDiACA+kQ686aKYqSSl3AP/uVieABanWqxaepEpSyh1gGsbXAFYe2EgtpGwqmlIH8MEZRQQ8m0qdFlGgSlDKHBA+csc90iYbAExMlU4L0VQJSokDzMayF4l4KwDlAY00cUmVIMsdED5S9giQ3g03C7ioSpDlDiBgsdU6Ug0BJ1TJsr4Lomuiz+8FE5pUyUrFGHA+BTpSC1ODKlHWR8QIWwDb0pB9NkLGLEhbMaQYBgAQsgUidAy2wG9hC9YD6iN+liCk3KlKluWbcZ7mA39LZKyVWlHUqZswzyDT+zp0v7K/zSpaRMneIiI1ybqWtQBm1tra2n7IzEv7hLr7QWqj4M15Boa+GRkdr+PKZGQW2Yi0oplgfWyvVkThk7AHd0MP7AJJi1P6Ce+oqvyIOIvweDwrmXlpIs8avreQ0fEaAIBhR9C5EAHHA2ByRH2O2AvD9xbs3l+AEExE9aAw0QK9ZI+y2LAlDmhtbV1IRJuTkeFs/x5E6Cg681wI6/FNpLTwcTjaXRBmczIm9EeL0DyjqbgpoEqgcgcws93j8RwGMD4ZOcJsBkiDFIntewnZAqd7MYRsTcaMK/mhVrpX6Rszyqehbrd7AZKsfACQ2vCEKx8ApBgGX64LrC6bkIUUr6sS1o1yBxDR11TLTBTTNhFBh5qEZgK2080fHlMirAfKHcDM01TLTIaA8+tgEVv44dOTA1eHZLyqyqaeWNEChtSOJ5MTYWP2oOUaGjVset8+0O1jWule5VlxQArjATt37sT8+fMxf/587NqV2nSgoD16CDdsElZvysDp5oGqg14igqysrPwb1bZZ0QL6Td+rrq5Gc3MzmpubUV1drVptVFiP/krw5t/YcPKcwKnzAtx31XhBOLX1lZWVE5n5FdW2WTEGfKRaZn/E06KizaYueAj/9W6k6/EHCS1tV8zMmX5c/rDBzLwJQHaydl+JFQ7ot69csWIFhg8fjqKiIqxYsSJpPfG1qIE3Q9b8IgOdgcuVfup8ryoJCMlrhBCvAJiajL0DoXwvqKCgYIvH42kCMKHn9Tlz5mDbtm2q1cXEQIuxhkYdH+zXkeVgZBqR1vD5eYEvlXa9KUP478pF2eUALEsitmIMCBHRMtVyrySeFkWhP/S5Fhl4DQDAX/95AFPGR/I/T/UYiDe9Z98CYI06q/tiyW5ofn7+L91u90okEAvWzBMwtRsHLRdPi7IH6/tc6x54bxgpce+dIZiSsH0f8HlXFxQI0Qfrthj/DCCHmdcTkfIZEGDhNDQ/P38ZgBcHK0ccgDDPwRbYAUf79+H0fBfEXmV2EHdAD+zuda3nwPv4gwHoGlA8NrLD3D0GLFmVGUDkldljwWBwkTKDrsCyeAARSW4qeyXMI+aS9MwkDsS88Wf43oLf+YgSOwzvmyDuHSP4yWYDnQFCRVkYU4sjXU/xGBNEjPNuwvu77YFPT2p3A/BLKR/YtWvXpYqKCiX2XIllLYCbysbIMA4I89yseCofAOzezdBCnyZtgx4+Cruv96Rsf6OOHQ02ZBqMv1vg/+K6I4Nx/XUMZsKqjUb3Dt7iurq6A0kbEgXrHBDGy0gwhY8Qiuzny5aE9Qt5AZlt3wOhd5x598FIo3/oq0EMy+s9PS0eG5n9mBICwJu1tbXrEjYgVjutEszAl5N5XshWON2LoYePxv2sFm6C07Ok3+nnt6v8eO5xH+6v6JsAMHFcd6SRmwzD+FbcihMg7S9qR0PIVjjcS5HR8e8xDczEHcjoeA1ZniejRsOm32z291I2isdKaBpMgL6+bds2Zdlv0bBuEAbXMJKPDRBCMHw/h93/DsLGbATts8D6mH6C8vXQ/fV9Btx4KB5jYs6toTdcq3bsT9buWLEsKM+N00skqB4WvYrEsMx4HzMdJOBnQnevVRn/7Q9L84K4qWwMh7GKgT8DkDPoA0OPA4L0e6ik/rRVClLyluSG511zSTNfl6aImt5g0yNzcSEk7LYQMowADHsQjswAcrK9yM3qQF7ORWQY1qScDMABoXlmWtUSLHfA+udc3wTxT6BwvMnJ8uL6omaUTPgMDsMPIWJJ/UoC5kXapH2rrRBtqQPWP+96CJAbAAsO2ulieIEHk0t+j+uLkssB5qCE/L0XkAwxzglyXs6kZMJuvWTvrGRt7Q/LKmZDtWsKa7wXXQegWs34sadwx9RPoGmJZQ3K0z7IC5GujQwN2qSesRfq0Er3KA/GABatA5hBrPE6pKjyAeD4ydF4f+csdPqNhJ7nS2a0u5acmgtY5ICNL7juA6DsZeZYafHk4r0ds+DrjN/vHIzUMRkaxNjeOahMOKzEwH6wxAEm49tWyI2FS14HfrNzJgLB+DLi9Ftzod+WB21Sdq/+HwBI8s9U2tgT5Q54o/rpkQSuVC03Hi56Hfhg7+1gVjLEHRCyc60KQf2h3AFSs1daITdezl8oxKFjSaeoRhZikw9ZtvBQHxMGBk9DSxEHGyfgktcZ+wMML0AdDNSDeZEwfTOsXAUDFmzGMbhEtcxEMaXAwaMTMPv238VUXujhG6m44YLFZvXWaYHMtB1B2R8nPh8Ff2DAnM/ekJ6yaXM3FjiActXLTBxmwmenBvuiVRchyrTWmr5Y0QKG3FE051pifNFDIOUOUDYG/OhHi4zczsI3wGz9mf9x4mmLcSecZcp/PMockOsr+AHAVarkqSQQjG0MMNNwmouyLohBD6uSpRopY/szCRTjYKEOZQ6gIbD4GghdH/hs6F7wVdwCCNioSlYstLU0o+3CeXR6O6Ikn0dwOvyDlOiGr94W0OnHCmbaoUpeVBiw2Q2EQyF429vga2+LWjwvJ7YMk6u6C/qWy+W76Gy9G6DlAKLXSJxI00Qo4Ifv0kW0t7ag9dxpdHZcPjUs0NkZ9fmiQndMepiSf785XiyJiP2Hy5WhZci7AVEugSkEvhGRNMUsAHYwQ3K3AQwpJVhKSCkhpQlpmjDDYZjhEMywCR4gHkKCwJIhNB0FRSP6L0OMhV+piTWQL0UgkENTP1aXnj0IKT07+qWXnszkzy4q+Yq1puvQ7QYCPi8ys7PhzO5/AT5m5DncNSP2PCvBYjpN+jAl77kBKZ65LFnycqcgSiqFwWZkIDu/EPnXjYAjKxtGpgPOrIF2PxhTSo7HJd8UPDkZ++Il5d+Q0e3G0WDAXxpreU3ToNvtsBkZsGdkQojLvxlN15GdP3AC9k1jz6Awrz0u+4jlte0AYbP9lRYO7WOWGkgDUeTzUCQ0aJoGoWnQND3yr83Wq8LjwenwY9ot8YdyGXRHQgoTJC3fD9j4r66bTYHNKg/B7omumfjTuR9iWH5Ck7FOYfryrIyC9SQtq9eHnnYdzrS3TyPiFQCUfhhH10zcNeOjRCsfADKhZ96m0qZopP17wj/96WO2jLZR1WB+KllZTocff1K2P5nKj0C8RCvZ93Ky9sSkKhVKYmH9888+AdBKJDQuMW4aewbTbjkMw5b80ZcEvCtK985PWlBsuoYO//n8M5NHDXd/crZ5WEzliRijR5zHlJLjcc92BiEgTN8wmnzI4iMYh5gDAMBsLGN3ew5Ony3C2QvD4PVlIBC0w5QCdlsYjkw/8nIuoqjQjdEjz1uWqs7g+/TSfb+yRHgP0v4tyf4oyL2IgtyLuKVU+QlhMUOMhQAsd8CQ3cNPO0QLeN+06AeVKuCPDhiYbDObFlqt5I8OiAIxfcdqHf8PkcZT5IMXmA8AAAAASUVORK5CYII=">
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'EditUserView',
  data() {
    return {
        nickname: '',
        profile_path: '',
        old_password: '',
        new_password1: '',
        new_password2: '',
    };
  },
  methods: {
    ...mapActions(accountsStore, ['editUserInfo']),
    ...mapActions(accountsStore, ['editPassword']),
  },
};
</script>

<style scoped>

</style>