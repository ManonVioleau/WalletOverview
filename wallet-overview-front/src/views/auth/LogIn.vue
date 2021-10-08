<template>
  <div>
    <div v-if="!connected">
      <div class="errors" v-if="errors.message && errors.message != null">
        <p>{{ errors.message }}</p>
        <img
          src="@/assets/icons/close_black_24dp.svg"
          alt=""
          v-on:click="errors.message = null"
        />
      </div>
      <div class="auth square">
        <h1>Log In</h1>
        <form @submit.prevent="connectUser()">
          <input type="text" v-model="name" placeholder="Username" required />
          <input
            type="password"
            v-model="password"
            placeholder="Password"
            required
          />
          <div><input type="checkbox" v-model="remember" /><p> Remember Me</p> </div>
          <button type="submit">Let's go !</button>
        </form>
      </div>
    </div>
    <div v-else>
      <!-- <div class="messages" v-if="errors.message && errors.message != null">
        <p>{{ errors.message }}</p>
        <img
          src="@/assets/icons/close_black_24dp.svg"
          alt=""
          v-on:click="errors.message = null"
        />
      </div> -->
      <div class="auth square">
        <h1>Welcome Back {{ user.name }} !</h1>

        <!-- <router-link class="go_dash" to="/Dashboard"> -->
        <form @submit.prevent="go_dash()">
          <button type="submit">My Dashboard</button>
          <!-- </router-link> -->
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "SignUp",
  components: {},
  data() {
    return {
      name: "",
      email: "",
      password: "",
      password_confirm: "",
      remember: false,
    };
  },
  computed: {
    ...mapState("auth", {
      user: (state) => state.user,
      connected: (state) => state.connected,
    }),
    ...mapState("errors", {
      errors: (state) => state.errors,
    }),
  },
  methods: {
    ...mapActions({
      login: "auth/LOGIN",
    }),
    connectUser() {
      const body = {
        name: this.name,
        password: this.password,
        remember: this.remember,
      };
      this.login(body);
    },
    go_dash() {
      this.$router.push("/Dashboard");
    },
  },
  mounted() {},
};
</script>
