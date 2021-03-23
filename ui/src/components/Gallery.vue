<template>
  <div id="gallery">
    <Albums
      :albums="data.albums"
      :config="awsConfig"
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

const changeGallery = async (newGallery) => {
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
    if (isImage(image)) {
      const key = getKey(image);
      if (result.images.indexOf(key) == -1) {
        result.images.push(key);
      }
    }
  }
  return result;
};

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
    // List root data
    this.data = await changeGallery(null);
  },
  methods: {
    async onGalleryChanged(newGallery) {
      this.data = await changeGallery(newGallery);
      this.gallery = newGallery
    },
  },
};

function isImage(file) {
  return (
    file.endsWith(".jpg") || file.endsWith(".mp4") || file.endsWith(".mov")
  );
}

function getKey(file) {
  const name = file.split(".")[0];
  var key = name.replace("_quality_20", "");
  key = key.replace("_quality_60", "");
  return key;
}
</script>
