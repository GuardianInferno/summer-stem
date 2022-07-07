<template>
  <div class="form-wrapper">
    <h3>Sign Up</h3>
    <form @submit.prevent="handleSubmit" class="block-container">
      <div class="block-body">
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="email">Email: </label>
            </div>
          </dt>
          <dd>
            <input
              class="input"
              type="email"
              name="email"
              v-model="email"
              required
            />
          </dd>
        </dl>
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="username">Username: </label>
            </div>
          </dt>
          <dd>
            <input
              class="input"
              type="username"
              name="username"
              v-model="username"
              required
            />
          </dd>
        </dl>
        <dl class="form-row">
          <dt>
            <div class="label-wrapper">
              <label for="password">Password: </label>
            </div>
          </dt>
          <dd>
            <input
              class="input"
              type="password"
              name="password"
              v-model="password"
              required
            />
          </dd>
        </dl>
      </div>
      <dl class="form-row form-submit-row">
        <dd>
          <div class="form-submit-row-main">
            <div class="form-submit-row-controls">
              <button class="button">
                <span class="button-text">SIGN UP</span>
              </button>
              <div v-if="error">{{ error }}</div>
            </div>
          </div>
        </dd>
      </dl>
    </form>
  </div>
</template>


<script>
import { ref } from "vue";
import { useFirebaseStore } from "@/stores/firebase-store";
import { useRouter } from "vue-router";
export default {
  setup() {
    const store = useFirebaseStore();
    const email = ref("");
    const password = ref("");
    const username = ref("");
    const error = ref(null);
    const router = useRouter();
    const handleSubmit = async () => {
      try {
        await store.signup(email, password, username);
        router.push("/");
      } catch (err) {
        error.value = err.message;
      }
    };
    return {
      handleSubmit,
      email,
      password,
      error,
      username,
    };
  },
};
</script>