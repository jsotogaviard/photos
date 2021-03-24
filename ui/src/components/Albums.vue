<template>
  <div id="albums">
    <div class="album">ALBUMS</div>
    <a class="folder" @click="up()">
      <font-awesome-icon :icon="['fas', 'folder']" />
      ..
    </a>
    <br />
    <a
      class="folder"
      v-for="(album, i) in albums"
      :key="i"
      @click="changeGallery(album)"
    >
      <font-awesome-icon :icon="['fas', 'folder']" />
      {{ album }}
      <br />
    </a>
  </div>
</template>

<script>
export default {
  name: "Albums",
  props: {
    albums: {
      default: function () {
        return []
      },
      type: Array,
    },
    gallery: {
      default:null,
      type: String,
    },
  },
  methods: {
    changeGallery(newGallery) {
      this.$emit("onGalleryChanged", newGallery);
    },
    up() {
      if (this.gallery && this.gallery.length > 1) {
        const path = this.gallery.substring(0, this.gallery.length -1) 
        const pathArray = path.split("/")
        const newGallery = pathArray
          .slice(0, pathArray.length - 1)
          .join("/");
        this.changeGallery(newGallery + "/");
      }
    },
  },
};
</script>


<style>
.folder {
  font-size: 18px;
  color: blue;
  cursor: pointer;
}
.album {
  color: #060354;
  font-family: "Raleway", sans-serif;
  font-size: 62px;
  font-weight: 800;
  line-height: 72px;
  margin: 0 0 24px;
  text-transform: uppercase;
}
</style>
