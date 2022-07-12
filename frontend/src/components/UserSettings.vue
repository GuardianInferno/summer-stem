<script setup>
import { useUserStore } from '../stores/user';
</script>

<template>
  <div class="settings">
    <RouterLink to="/login">Login</RouterLink>
    <RouterLink to="/signup">Signup</RouterLink>
    <a v-if="useUserStore().user" @click="useUserStore().logout()">Log Out</a>
    <span v-if="useUserStore().user">Logged in as: {{useUserStore.user}}</span>
  </div>
</template>

<style lang="scss" scoped>
.settings {
  @include border;
  a {
    color: $foreground;
    text-decoration: none;
    margin-right: 1rem;
    &:hover {
      color: wheat;
      cursor: pointer;
    }
  }
  span {
    float: right;
  }
}
</style>