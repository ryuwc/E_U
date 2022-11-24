<template>
  <div>
    <!-- 개별 영화 썸네일 -->
    <div style="position: relative; cursor: pointer; margin-bottom: 13px; margin-left: 100px;" v-for="(video, index) in videos" :key="index"
      data-bs-toggle="modal"
      data-bs-target="#exampleModal"
      @click="clickVideo(video.key)"
    >
      <div style="width: 492px; max-height: 275px; overflow: hidden; border: 1px solid gray" class="rounded-lg">
        <img :src="`https://i.ytimg.com/vi/${video.key}/hqdefault.jpg`" alt="준비 중.." style="max-height: initial; margin-top: -10%" class="w-full" />
      </div>
      <img
        style="position: absolute; top: 90px; left: 190px"
        src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAFXElEQVR4nO3cT2wUVRzA8e/bP7RYxLYUWyigrSRoihysF8RGSAiJMfFETfTGwYsxJXrgRtDExItR/qhEIx4MkchFTYgH9NBAqX9iQ4z1D5pSLaWtoYEqloV22edhd2EPOO/NzOvOdOf3ucw0+2bnl/n1zfw6fe+BEEIIIYQQQgghhBBCCCGEELVMVfuEegcNXKOdNK1oVlKgkRRNFGhE0Qg0Ak2lbT2wtLTFY/86kCvt50o/V+7ngBngSmlb3Ne39i9RYBLNhPr61vdUhdME6G6y1LGOLJ1oOtE8AKwG1qBpRdEO3O3ynAtgBpgApoCLaC6iOA+cRzNKhjHVT97VyUIlQPewCsVzaHqAh4F1QMZJZPGVB8aAH9GcIsPHqp+poF8WKAF6M81keA14ntq/4CbzaN4H9qoBrvg92HcCdA+bgM+B+/0eW+NGSfO06mfYz0G+EqC3sp48Ayha/cWWGNMUeFyd4ZztASnbhrqLJeT5VC6+pxZSHNddLLE9wDoBNPEiio2BwkqWTTTzgm1jq1uQ7iXNFKPA2sBhJcsYp+lQUDA1tOsBU3QjF9+PdWzhEZuGtregLSGCSaYUPXbNbCgeDBVMMj1k08guAVoSEIDTBGwIFUoyuUmA3kGD1P6BrNCbaTY1MveAOal+Astyn6mJOQF51jgJJqg3v4SOrkhDCKHD1MDmGRBtD3h0Oxw5C30HoOGeSEPxrWB+YWmTgNUOQgknk4WdffDJCOzcDSn7NyiRUm4SsNJBKG4sXwF9++G972DjY1FHY6bNxYs5ASmanATj0oZueGcAXj0O98a6RjD+8poToM2lVCSUgm29cPQX2PUKZOuijuhOHCSAGPaASvUNsGsffDRcTEicKFpMTRZ/Asra1xdvSfEqW1u04ZW/TQIaHAVTHfEqWzN0s9SrgU0CrP+9FhtxKluX4vlwqs0ElMWhbM2ET0DWUSjRibZsrff6sLZ7QKWoytb5JN+C7qTaZasK3wNqk9ZwowoDoVPeIyNsxnXOYbiPLSrXZ+HYG3D0dZi/UY0z/uv1YXISoDWcPAqH98DlwIOZ/csz6/WxTQLmHYUSnXNDcKAPhgerf+5l4RMw5yiU6rs8BR/ugxMfQME4SG0haE56z7ipzQTk5+Gzw3BkL8z+E2UkOdPwRJsEeD5EYuf7r+Dgbvjj56gjgeJ0J082CfA96yMS47/D2y/D4ImoI6l0ydTAJgGXHQSycKpfVvoxbWqweHtAVGWlPzWagCjLSj+0iwRopqs/nft/RF9W+uXgGZBiHO0kmODiU1b6NWZqYNMDxp2EEtQ3X8Chl+DCb5GGEYhykYAC45G+M93zVIQnD0lzwdTEfGkbIu4Bi5cmZ752xgSok8yi+ctNTIkyqYa4ZmpkO0fs19DhJI22my1vmwDrqfeixPKa2c4Rkx7gn1XZZlvfnAkRSDJpTtk0s1uqoDjteJTigkzC7E9O0+lsqYLSF+0PHVZSKN6yufjgZ1hKmkPA2aAxJcgPzPKubWPrBKh+8tykV/4m8HQJzTNqyH4gg6+XDGqQETJsB877Dq32jVBgmxqwq37KfL/lUf0Mk6YbOEQtDFkJbx7FQeroVmf4ye/B4Zat3EobN3kWeILispVrqYXR1N5uL1sJ/cxxTH0b/LbsduHWrWSANRTopDhLvANYi6YNaAfagBUuz7kA/qa4cOsk5YVbYRRKi7fGaeHWIPST1JFjFQVWAy2Ulym+vXRxedniRmAZijSa5aXDs8Cy0n4dcFdpv3K54lluj2W6CuTRXCPFDJoZVMWSxeVtmmkUk1xlwuYFmhBCCCGEEEIIIYQQQgghhBDC1n9OVmxVMC95FwAAAABJRU5ErkJggg=="
      />
    </div>
    <!-- 영호 썸네일 끝 -->
    <!-- 비디오를 띄우는 모달 -->

    <div
      class="fixed top-0 left-0 hidden w-full h-full overflow-x-hidden overflow-y-auto outline-none modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="relative w-auto pointer-events-none modal-dialog"
        style="width: 1280px; height: 720px; margin-left: auto; margin-right: 1100px; margin-top: 100px;"
      >
        <div
          class="relative bg-white border-none rounded-md shadow-lg outline-none pointer-events-auto modal-content bg-clip-padding"
          style="width: 1280px; height: 720px;"
        >
        <iframe
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            id="ytplayer"
            type="text/html"
            width="720"
            height="405"
            :src="nowUrl"
            frameborder="0"
            allowfullscreen="allowfullscreen"></iframe>
        </div>
      </div>
      
    </div>
  </div>
  <!-- 유튜브 iframe사용 예시 -->
  <!-- <iframe
            id="ytplayer"
            type="text/html"
            width="720"
            height="405"
            src="https://www.youtube.com/embed/6JnN1DmbqoU"
            frameborder="0"
            allowfullscreen="allowfullscreen"></iframe> -->
</template>

<script>
import { mapGetters } from 'vuex';

const moviesStore = 'moviesStore';
export default {
  name: 'MovieClip',
  data() {
    return {
      nowUrl: '',
    }
  },
  computed: {
    ...mapGetters(moviesStore, ['nowMovieVideo']),
    videos() {
      // nowMovieVideo 데이터 3개만 받아오기
      return this.nowMovieVideo.slice(0, 3);
    },
  },
  methods: {
    clickVideo(urlKey) {
      this.nowUrl = `https://www.youtube.com/embed/${urlKey}?autoplay=1&mute=1`;
      // console.log(this.nowUrl);
    },
  }
};
</script>

<style></style>
