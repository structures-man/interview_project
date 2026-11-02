<script setup lang="ts">
// vue 3 语法糖 不用注册=组件 export default 面向对象写法
// export default {}
// composition api 组合式API
import FileUploader from "./components/FileUploader.vue";
</script>

<template>
  <div class="min-h-screen bg-gray-50 px-4 py-10">
    <FileUploader />
  </div>
</template>

