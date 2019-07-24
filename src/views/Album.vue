<template>
  <div>
    <div
      class="button"
      :class="{'box-shadow': scrollTop>50}"
    >
      <div>
        <img
          src="@/assets/arrow_left.svg"
          @click="$router.back(-1)"
        >
      </div>
      <div>
        <img
          src="@/assets/add.svg"
          @click="$router.push('/upload')"
        >
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
      <photo
        v-for="photo in photos.items"
        :key="photo"
        :to="{name: 'photo', params: { id: photo } }"
        :img="photo"
      />
    </div>
  </div>
</template>

<script>
import photo from '@/components/photo'
export default {
  components: { photo },
  data () {
    return {
      photos: [],
      scrollTop: 0
    }
  },
  mounted () {
    import('@/albums/' + this.$route.params.id + '.json').then(photos => {
      this.photos = photos
    })
    this.$nextTick(() => {
      window.addEventListener('scroll', this.onScroll)
    })
  },
  methods: {
    onScroll () {
      if (document.documentElement && document.documentElement.scrollTop) {
        this.scrollTop = document.documentElement.scrollTop
      } else if (document.body) {
        this.scrollTop = document.body.scrollTop
      }
    }
  }
}
</script>

<style scoped>
.button {
  position: fixed;
  background-color: white;
  top: 0;
  width: 100%;
  z-index: 1;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 1rem;
}
.box-shadow {
  box-shadow: #ccc 0 0 5px;
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
  font-size: 3rem;
  margin-top: 5rem;
  margin-bottom: 1rem;
}
</style>
