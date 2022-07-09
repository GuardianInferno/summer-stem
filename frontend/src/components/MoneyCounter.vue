<template>
  <div class="money-box">
    <p class="money-count">$123,456,789</p>
  </div>
</template>

<style lang="scss" scoped>
.money-box {
  @include border;
  padding: 1rem;
  margin-bottom: 1rem;
  .money-count {
    font-size: 5rem;
  }
}
</style>