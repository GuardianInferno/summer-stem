<script setup>
import Market from '../components/Market.vue';
import Items from '../components/Items.vue';
</script>

<template>
  <main class="screen">
    <Market/>
    <div class="info">
      <Items/> 
    </div>
    
  </main>
</template>

<style lang="scss">
.screen {
  width: 95%;
  margin: auto;
  margin-top: 1rem;
}
.info {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  margin-top: 1rem;
}
</style>