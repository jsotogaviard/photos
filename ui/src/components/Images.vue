<template>
  <div id="image">
    <div class="imagecss">IMAGES</div>
    <img
      v-for="(image, i) in images"
      :key="i"
      class="image"
      :src="config.s3.url + image + '_quality_20.jpg'"
      @click="index = i"
    />
    <vue-gallery-slideshow
      :images="toto(images)"
      :index="index"
      @close="index = null"
    />
  </div>
</template>

<script>
import VueGallerySlideshow from "vue-gallery-slideshow";

export default {
  name: "Images",
  components: {
    VueGallerySlideshow,
  },
  data() {
    return { index: null };
  },
  props: ["images", "config"],
  methods: {
    toto(keys = []) {
      const result = [];
      keys.forEach((key) => {
        result.push(this.config.s3.url + key + "_quality_60.jpg");
      });
      return result;
    },
  },
};
</script>


<style>
.image {
  width: 100px;
  height: 100px;
  background-size: cover;
  cursor: pointer;
  margin: 5px;
  border-radius: 3px;
  border: 1px solid lightgray;
  object-fit: contain;
}
.imagecss {
  color: #060354;
  font-family: "Raleway", sans-serif;
  font-size: 62px;
  font-weight: 800;
  line-height: 72px;
  margin: 0 0 24px;
  text-transform: uppercase;
}
</style>
