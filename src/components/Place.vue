<template>
     <div class="Place">
    <img :src="location.img" width="235" height="300"/>
    <slot></slot>
    <p>{{ location.desc }}</p>
  </div>
</template>
<script>
export default {
  name: 'Place',
  components: { 
  }
}
</script>