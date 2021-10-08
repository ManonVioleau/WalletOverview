<template>
  <div class="auth square">
    <h1>You Successfully Logged Out !</h1>
    <form @submit.prevent="go_dash()">
      <p>See you soon !</p>
      <button type="submit">Go Back Home</button>
    </form>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SignUp",
  components: {},
  computed: {
    ...mapState("auth", {
      user: (state) => state.user,
      connected: (state) => state.connected,
    }),
  },
  methods: {
    go_dash() {
      this.$router.push("/Home");
    },
  },
  created() {
    this.$store.state.auth.user = {};
    this.$store.state.auth.connected = false;
    this.$store.state.errors.errors.message = "";
    let hasCookie = document.cookie.split(";").some((c) => {
      return c.trim().startsWith("profil" + "=");
    });
    if (hasCookie) {
      document.cookie =
        "profil" +
        "=" +
        ";path=/;secure" +
        ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
    }
  },
};
</script>
