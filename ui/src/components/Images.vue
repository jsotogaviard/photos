<template>
  <div id="image">
    <div class="imagecss">IMAGES</div>
    <div>
      <font-awesome-icon
        class="circle"
        :icon="['fas', 'plus-circle']"
        @click="this.atTopOfWindow"
      />
      <img
        v-for="(image, i) in visibleImages"
        :key="i"
        class="image"
        :src="config.s3.url + image + '_quality_20.jpg'"
        @click="index = i"
      />
      <font-awesome-icon
        class="circle"
        :icon="['fas', 'plus-circle']"
        @click="this.atBottomOfWindow"
      />
    </div>
    <vue-gallery-slideshow
      :images="slideShowImages(visibleImages)"
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
    return {
      index: null,
      start: 0,
      end: this.config.infiniteScroll.initial,
    };
  },
  props: {
    images: {
      default: function () {
        return [];
      },
      type: Array,
    },
    config: {
      default: function () {
        return {};
      },
      type: Object,
    },
  },
  mounted() {
    window.onscroll = () => {
      const bottomOfWindow =
        document.documentElement.scrollTop + window.innerHeight ===
        document.documentElement.offsetHeight;
      const topOfWindow = document.documentElement.scrollTop === 0;
      if (bottomOfWindow) {
        console.log("bottomOfWindow");
        this.atBottomOfWindow();
      } else if (topOfWindow) {
        console.log("topOfWindow");
        this.atTopOfWindow();
      }
    };
  },
  computed: {
    visibleImages() {
      if (!this.images) {
        return [];
      } else {
        const visibleImages = this.images.slice(this.start, this.end);
        return visibleImages;
      }
    },
  },
  methods: {
    atBottomOfWindow() {
      if (this.images.length > this.end - this.start) {
        this.start += this.config.infiniteScroll.step;
        this.end += this.config.infiniteScroll.step;
        window.scrollTo(0, 50);
      }
    },
    atTopOfWindow() {
      if (this.start > this.config.infiniteScroll.step) {
        this.start -= this.config.infiniteScroll.step;
        this.end -= this.config.infiniteScroll.step;
        window.scrollTo(
          0,
          document.documentElement.offsetHeight - window.innerHeight - 50
        );
      } else {
        this.start = 0;
        this.end = this.config.infiniteScroll.initial;
      }
    },
    slideShowImages(keys = []) {
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
  width: 200px;
  height: 200px;
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
.circle {
  color: blue;
  display: block;
}
</style>
