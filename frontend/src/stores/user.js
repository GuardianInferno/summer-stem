import { defineStore } from "pinia";

const url = "http://127.0.0.1:8000";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: null,
    authIsReady: false,
  }),
  actions: {
    async login() {},
  },
});
