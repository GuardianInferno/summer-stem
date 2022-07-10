<script setup>
import MoneyCounter from '../components/MoneyCounter.vue';
import StockViewer from '../components/StockViewer.vue';
import UserInfo from '../components/UserInfo.vue';
import StockList from '../components/StockList.vue';
import UserSettings from '../components/UserSettings.vue';
</script>

<template>
  <main>
    <div class="left">
      <MoneyCounter/>
      <UserInfo/>
      <UserSettings/>
    </div>
    <div class="right">
      <StockViewer/>
      <StockList/>
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding: 5rem;
  display: flex;
  height: 100vh;
  gap: 1rem;
  .left {
    display: grid;
    grid-template-rows: 0fr 1fr 0fr;
    grid-row-gap: 1rem; 
  }
  .right {
    width: 100%;
    display: grid;
    grid-template-rows: 1fr 1fr;
    grid-column-gap: 1rem;
    grid-row-gap: 1rem; 
  }
}
</style>