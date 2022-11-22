<template>
  <div>
    <div 
    style="width: 492px; max-height: 275px; overflow: hidden; border: 1px solid gray; cursor: pointer;"
    class="rounded-lg"
    >
      <img src="https://i.ytimg.com/vi/ZS_8btMjx2U/hqdefault.jpg" alt="준비 중.."
      style="max-height: initial; margin-top: -10%;"
      class="w-full"
      >
      <img 
      src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAFXElEQVR4nO3cT2wUVRzA8e/bP7RYxLYUWyigrSRoihysF8RGSAiJMfFETfTGwYsxJXrgRtDExItR/qhEIx4MkchFTYgH9NBAqX9iQ4z1D5pSLaWtoYEqloV22edhd2EPOO/NzOvOdOf3ucw0+2bnl/n1zfw6fe+BEEIIIYQQQgghhBBCCCGEELVMVfuEegcNXKOdNK1oVlKgkRRNFGhE0Qg0Ak2lbT2wtLTFY/86kCvt50o/V+7ngBngSmlb3Ne39i9RYBLNhPr61vdUhdME6G6y1LGOLJ1oOtE8AKwG1qBpRdEO3O3ynAtgBpgApoCLaC6iOA+cRzNKhjHVT97VyUIlQPewCsVzaHqAh4F1QMZJZPGVB8aAH9GcIsPHqp+poF8WKAF6M81keA14ntq/4CbzaN4H9qoBrvg92HcCdA+bgM+B+/0eW+NGSfO06mfYz0G+EqC3sp48Ayha/cWWGNMUeFyd4ZztASnbhrqLJeT5VC6+pxZSHNddLLE9wDoBNPEiio2BwkqWTTTzgm1jq1uQ7iXNFKPA2sBhJcsYp+lQUDA1tOsBU3QjF9+PdWzhEZuGtregLSGCSaYUPXbNbCgeDBVMMj1k08guAVoSEIDTBGwIFUoyuUmA3kGD1P6BrNCbaTY1MveAOal+Astyn6mJOQF51jgJJqg3v4SOrkhDCKHD1MDmGRBtD3h0Oxw5C30HoOGeSEPxrWB+YWmTgNUOQgknk4WdffDJCOzcDSn7NyiRUm4SsNJBKG4sXwF9++G972DjY1FHY6bNxYs5ASmanATj0oZueGcAXj0O98a6RjD+8poToM2lVCSUgm29cPQX2PUKZOuijuhOHCSAGPaASvUNsGsffDRcTEicKFpMTRZ/Asra1xdvSfEqW1u04ZW/TQIaHAVTHfEqWzN0s9SrgU0CrP+9FhtxKluX4vlwqs0ElMWhbM2ET0DWUSjRibZsrff6sLZ7QKWoytb5JN+C7qTaZasK3wNqk9ZwowoDoVPeIyNsxnXOYbiPLSrXZ+HYG3D0dZi/UY0z/uv1YXISoDWcPAqH98DlwIOZ/csz6/WxTQLmHYUSnXNDcKAPhgerf+5l4RMw5yiU6rs8BR/ugxMfQME4SG0haE56z7ipzQTk5+Gzw3BkL8z+E2UkOdPwRJsEeD5EYuf7r+Dgbvjj56gjgeJ0J082CfA96yMS47/D2y/D4ImoI6l0ydTAJgGXHQSycKpfVvoxbWqweHtAVGWlPzWagCjLSj+0iwRopqs/nft/RF9W+uXgGZBiHO0kmODiU1b6NWZqYNMDxp2EEtQ3X8Chl+DCb5GGEYhykYAC45G+M93zVIQnD0lzwdTEfGkbIu4Bi5cmZ752xgSok8yi+ctNTIkyqYa4ZmpkO0fs19DhJI22my1vmwDrqfeixPKa2c4Rkx7gn1XZZlvfnAkRSDJpTtk0s1uqoDjteJTigkzC7E9O0+lsqYLSF+0PHVZSKN6yufjgZ1hKmkPA2aAxJcgPzPKubWPrBKh+8tykV/4m8HQJzTNqyH4gg6+XDGqQETJsB877Dq32jVBgmxqwq37KfL/lUf0Mk6YbOEQtDFkJbx7FQeroVmf4ye/B4Zat3EobN3kWeILispVrqYXR1N5uL1sJ/cxxTH0b/LbsduHWrWSANRTopDhLvANYi6YNaAfagBUuz7kA/qa4cOsk5YVbYRRKi7fGaeHWIPST1JFjFQVWAy2Ulym+vXRxedniRmAZijSa5aXDs8Cy0n4dcFdpv3K54lluj2W6CuTRXCPFDJoZVMWSxeVtmmkUk1xlwuYFmhBCCCGEEEIIIYQQQgghhBDC1n9OVmxVMC95FwAAAABJRU5ErkJggg=="
      class="bg-cover"
      >
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
    computed: {
        ...mapGetters(moviesStore, ['nowMovieVideo']),
        videos() {
          return JSON.parse(JSON.stringify(this.nowMovieVideo))
        },
    },
}
</script>

<style>

</style>