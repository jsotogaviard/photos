<template>
  <div id="gallery">
    <Albums
      :albums="data.albums"
      :gallery="gallery"
      @onGalleryChanged="onGalleryChanged($event)"
    />
    <Images :images="data.images" :config="awsConfig" />
  </div>
</template>

<script>
import config from "../../config";
import AWS from "aws-sdk";
import Images from "./Images.vue";
import Albums from "./Albums.vue";

AWS.config.update(config.s3);
const s3 = new AWS.S3();

export default {
  name: "Gallery",
  components: {
    Images,
    Albums,
  },
  data() {
    return {
      data: {},
      gallery: null,
    };
  },
  computed: {
    awsConfig: function () {
      return config;
    },
  },
  async mounted() {
    this.data = await this.changeGallery(null);
  },
  methods: {
    async onGalleryChanged(newGallery) {
      this.data = await this.changeGallery(newGallery);
      this.gallery = newGallery;
      console.log(this.gallery)
    },
    isImage(file) {
      return (
        file.endsWith(".jpg") || file.endsWith(".mp4") || file.endsWith(".mov")
      );
    },
    getKey(file) {
      const name = file.split(".")[0];
      var key = name.replace("_quality_20", "");
      key = key.replace("_quality_60", "");
      return key;
    },
    async changeGallery(newGallery) {
      const result = {
        albums: [],
        images: [],
      };

      const params = {
        Bucket: config.s3.bucket,
        Prefix: newGallery,
        Delimiter: "/",
      };

      const data = await s3.listObjects(params).promise();
      for (var i in data.CommonPrefixes) {
        const name = data.CommonPrefixes[i].Prefix;
        result.albums.push(name);
      }

      // Retrieve files
      for (var j in data.Contents) {
        const image = data.Contents[j].Key;
        if (this.isImage(image)) {
          const key = this.getKey(image);
          if (result.images.indexOf(key) == -1) {
            result.images.push(key);
          }
        }
      }
      return result;
    },
  },
};
</script>
