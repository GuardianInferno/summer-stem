<template>
  <div class="handle">
    <span class="label">The Market Calls</span>
    <span class="close">✖</span>
  </div>
</template>

<style lang="scss">
.handle {
    background-color: $red;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    .label {
      font-size: 1.5rem;
    }
    .close {
      float: right;
      font-size: 2rem;
      transform: translateY(-13%);
    }
  }
</style>