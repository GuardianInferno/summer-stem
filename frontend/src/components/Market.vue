<script setup>
import Handle from './Handle.vue';
</script>

<template>
<div class="market-view" v-drag="'.handle'">
  <Handle class="handle"/>
</div>
</template>

<style lang="scss">
.market-view {
  border: 1px solid $red;
  height: 40rem;
  background-color: $white;
}
</style>