<template>
  <div>
    <div class="title container">
      <div>
        309 · 相册
      </div>
      <div class="">
        <img
          src="@/assets/add.svg"
          @click="$router.push('/upload')"
        >
        <img
          src="@/assets/download.svg"
          @click="$router.push('download')"
        >
      </div>
    </div>
    <div class="main container">
      <photo
        v-for="album in albums"
        :key="album.title"
        :to="{ name: 'album', params: { id: album.title }}"
        :img="album.cover"
        :title="album.title"
        :count="album.count"
      />
    </div>
  </div>
</template>

<script>
import albums from '@/albums/index.json'

import photo from '@/components/photo'
export default {
  components: { photo },
  data () {
    return {
      albums: albums
    }
  }
}
</script>

<style scoped>
.title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 1rem;

  font-family: 'Roboto', '隶书', Helvetica, Arial, sans-serif;
  text-align: left;
  font-size: 1.5rem;
  height: 3rem;
  line-height: 3rem;
  margin-bottom: 2rem;
}
.title img {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  padding: 10px;
}
.title img:hover {
  background-color: #eee;
  cursor: pointer;
}
</style>
