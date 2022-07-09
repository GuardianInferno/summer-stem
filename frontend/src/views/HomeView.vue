<script setup>
import MoneyCounter from '../components/MoneyCounter.vue';
import StockViewer from '../components/StockViewer.vue';
import UserInfo from '../components/UserInfo.vue';
</script>

<template>
  <main>
    <div class="left">
      <MoneyCounter/>
      <UserInfo/>
    </div>
    <div class="right">
      <StockViewer/>
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding: 5rem;
  display: flex;
  .right {
    width: 100%;
  }
}
</style>