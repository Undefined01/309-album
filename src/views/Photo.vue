<template>
  <div>
    <div class="button">
      <div>
        <img
          src="@/assets/arrow_left.svg"
          @click="$router.back(-1)"
        >
      </div>
      <div>
        <img
          src="@/assets/download.svg"
          @click="$router.push('/download')"
        >
      </div>
    </div>
    <div class="title container">
      {{ $route.params.id }}
    </div>
    <div class="main container">
      <img
        v-if="!isVideo"
        :src="src"
      >
      <video
        v-else
        :src="src"
        controls="controls"
        autoplay="autoplay"
      />
    </div>
  </div>
</template>

<script>
import settings from '@/settings.json'

export default {
  computed: {
    src () {
      return settings.CDN.main + this.$route.params.id
    },
    isVideo () {
      return this.src.substr(-3) === 'mp4'
    }
  }
}
</script>

<style scoped>

.button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 1rem;
}
.button img {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  padding: 10px;
}
.button img:hover {
  background-color: #eee;
  cursor: pointer;
}
.title {
  font-family: 'Roboto', '隶书', Helvetica, Arial, sans-serif;
  text-align: left;
  font-size: 2rem;
  margin-bottom: 1rem;
}
.main {
  text-align: center;
}
.main img {
  max-width: 100%;
}
</style>
