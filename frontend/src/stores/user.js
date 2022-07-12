import { defineStore } from "pinia";
import axios from "axios";

const url = "http://127.0.0.1:8000";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: null,
    authIsReady: false,
  }),
  actions: {
    async login(username, password) {
      await axios
        .post(`${url}/api/v1/token/login`, {
          password: password,
          username: username,
        })
        .then(() => {
          this.user = username;
        })
        .catch((error) => {
          throw new Error(error);
        });
    },
    async signup(email, username, password) {
      await axios
        .post(`${url}/api/v1/users/`, {
          email: email,
          username: username,
          password: password,
        })
        .then(() => {
          this.login(username, password);
        });
    },
    async logout() {
      alert("Non Functional")
    },
  },
});
