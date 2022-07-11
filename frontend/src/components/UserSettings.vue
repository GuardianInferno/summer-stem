<script setup>
import { useUserStore } from '../stores/user';
</script>

<template>
  <div class="settings">
    <RouterLink to="/login">Login</RouterLink>
    <RouterLink to="/signup">Signup</RouterLink>
  </div>
</template>

<style lang="scss" scoped>
.settings {
  @include border;
  a {
    color: $foreground;
    text-decoration: none;
  }
}
</style>