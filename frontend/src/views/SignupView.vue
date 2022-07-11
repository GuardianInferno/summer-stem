<template>
<div class="page-wrapper">
  <div class="form-wrapper">
    <h3>Signup</h3>
    <form @submit.prevent="handleSubmit" class="block-container">
      <div class="block-body">
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="username">Username: </label>
            </div>
          </dt>
          <dd>
            <input class="input" type="username" name="username" v-model="username" required />
          </dd>
        </dl>
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="email">Email:</label>
            </div>
          </dt>
          <dd>
            <input class="input" type="email" name="email" v-model="email" />
          </dd>
        </dl>
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="password">Password: </label>
            </div>
          </dt>
          <dd>
            <input class="input" type="password" name="password" v-model="password" required />
          </dd>
        </dl>
      </div>
      <dl class="form-row form-submit-row">
        <dd>
          <div class="form-submit-row-main">
            <div class="form-submit-row-controls">
            <button class="button"><span class="button-text">LOG IN</span></button>
            <div v-if="error">{{ error }}</div>
          </div>
          </div>
        </dd>
      </dl>
    </form>
  </div>
</div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user";
export default {
  setup() {
    const username = ref("")
    const password = ref("")
    const email = ref("")
    const error = ref(null)
    const router = useRouter()
    const store = useUserStore()
    const handleSubmit = async () => {
      try {
        await store.login(username.value, password.value)
        router.push("/")
      } catch (err) {
        error.value = err.message
      }
    }
    return {
      handleSubmit, username, password, email, error
    }
  }
}
</script>

<style scoped lang="scss">
.page-wrapper {
  display: flex;
  height: 100vh;
}
.form-wrapper {
  margin: auto;
  width: 80%;
  h3 {
    font-size: 2rem;
  }
}
.block-container {
  border: 1px solid;
  border-color: $foreground;
  padding: 1rem;
  padding-bottom: 0;
}
.form-row {
  display: table;
  table-layout: fixed;
  width: 100%;
  margin: 0;
  position: relative;
  dt {
    padding-top: 2.4rem;
    border-right: 1px solid;
    border-color: $foreground;
    text-align: right;
    width: 33%;
    padding: 15px 10px 15px 10px;
  }
  dd {
    width: 67%;
    padding: 15px 10px 15px 10px;
  }
  dd, dt {
    display: table-cell;
    vertical-align: top;
  }
}
.label-wrapper {
  transform: translateY(7px);
  label {
    font-size: 1.5rem;
  }
}
.input {
  color: white;
  background: $background;
  border: 1px solid;
  border-color: $foreground;
  padding: 0.8rem;
  display: block;
  width: 100%;
  line-height: 1.3;
  text-align: left;
  word-wrap: break-word;
  font-family: monospace;
  font-size: 1.5rem;
}
.form-submit-row {
  position: relative;
  dd {
    border-top: 1px solid;
    border-color: $foreground;
  }
}
.form-submit-row-main {
  position: relative;
}
.form-submit-row-controls {
  position: relative;
  padding-left: 33%;
  padding-top: 8px;
  padding-bottom: 8px;
  margin-left: 10px;
  margin-right: 10px; 
}
.button {
  border: 1px solid;
  border-color: $foreground;
  color: $foreground;
  background-color: transparent;
  cursor: pointer;
  text-decoration: none;
  justify-content: center;
  align-items: center;
  display: inline-flex;
  padding-top: 8px;
  padding-right: 10px;
  padding-bottom: 8px;
  padding-left: 10px;
  text-align: center;
  &:hover {
    background-color: $foreground;
    color: white;
  }
}
.button-text {
  font-size: 1.3rem;
}
</style>