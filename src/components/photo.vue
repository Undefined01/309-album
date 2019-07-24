<template>
  <div
    class="photo col-lg-3 col-sm-6"
    @click="route"
  >
    <div class="play">
      <img
        v-if="isVideo"
        src="@/assets/play.svg"
      >
    </div>
    <div>
      <img
        v-lazy="src"
        class="photo-img"
      >
      <div
        v-if="title !== undefined"
        class="title"
      >
        <span class="name">{{ title }}</span>
        <span class="count">{{ count }} 项</span>
      </div>
    </div>
  </div>
</template>

<script>
import settings from '@/settings.json'

export default {
  name: 'Photo',
  props: {
    to: {
      type: Object,
      default: undefined
    },
    img: {
      type: String,
      required: true
    },
    title: {
      type: String,
      default: undefined
    },
    count: {
      type: Number,
      default: undefined
    }
  },
  computed: {
    src () {
      if (this.isVideo) return settings.CDN.snap + this.img.substr(0, this.img.length - 3) + 'jpg'
      return settings.CDN.snap + this.img
    },
    isVideo () {
      return this.img.substr(-3) === 'mp4'
    }
  },
  methods: {
    route () {
      if (this.to) this.$router.push(this.to)
    }
  }
}
</script>

<style scoped>
.photo {
  position: relative;
  display: inline-block;
  margin-bottom: 2rem;
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  font-size: .875rem;
  font-weight: 500;
  cursor: pointer;
}
.play {
  position: absolute;
  float: right;
}
.play img {
  height: 20px;
  width: 20px;
}
.count {
  color: #888;
}
.title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.photo-img {
  border-radius: 5%;
  width: 100%;
  max-height: 247.5px;
}
.photo-img:hover {
  box-shadow: #ccc 0 0 10px;
}
</style>
