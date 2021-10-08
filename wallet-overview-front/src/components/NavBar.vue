<template>
  <div id="nav">
    <router-link to="/"
      ><h1>Wallet<span>Overview</span></h1></router-link
    >
    <div class="middle" id="first">
      <router-link class="underline" to="/Dashboard">Dashboard</router-link>
      <router-link class="underline" to="/Wallets">Wallets</router-link>
      <router-link class="underline" to="/Trades">Trades</router-link>
      <!-- <router-link class="underline" to="/Portfolio">Portfolio</router-link> -->
    </div>
    <div class="middle" v-if="!connected">
      <router-link class="underline" to="/LogIn">Log in</router-link>
      <router-link class="underline" to="/SignUp">Sign up</router-link>
    </div>
    <div class="middle" v-else>
      <a id="sync-navbar" v-if="had_wallet">
        <div style="display: flex" v-if="loading">
          <div class="loader"></div>
          <p class="last_update" style="margin-left: 1rem">
            This operation can take between 10 and 20min
          </p>
        </div>
        <div style="display: flex" v-else>
          <img
            src="@/assets/icons/sync_orange_24dp.svg"
            alt=""
            v-on:click="get_synchro()"
          />
          <p class="last_update" v-if="synchro">
            {{ getLastUpdate(balances[0].updated_at) }}
          </p>
          <p class="last_update" v-else>Please synchronyse your wallets</p>
        </div>
      </a>
      <router-link class="underline" to="/AddWallet" v-else
        >Add wallet</router-link
      >
      <router-link class="underline" to="/LogOut">Log out</router-link>
    </div>
    <div class="menu_icon" v-if="close">
      <img
        src="../assets/icons/menu_black_24dp.svg"
        alt=""
        v-on:click="open_menu()"
      />
    </div>
    <div class="menu_icon" v-else>
      <img
        src="../assets/icons/close_black_24dp.svg"
        alt=""
        v-on:click="close_menu()"
      />
    </div>
  </div>
</template>

<script>
import moment from "moment";
import { mapState, mapActions } from "vuex";

export default {
  name: "NavBar",
  components: {},
  data() {
    return {
      close: true,
      loading: false,
    };
  },
  computed: {
    ...mapState("balances", {
      total: (state) => state.total,
      datas: (state) => state.datas,
      balances: (state) => state.balances,
    }),
    ...mapState("synchronyse", {
      synchro: (state) => state.synchro,
    }),
    ...mapState("platform", {
      platforms: (state) => state.platforms,
    }),
    ...mapState("auth", {
      user: (state) => state.user,
      connected: (state) => state.connected,
    }),
    ...mapState("wallets", {
      had_wallet: (state) => state.had_wallet,
      wallets: (state) => state.wallets,
    }),
  },
  methods: {
    open_menu() {
      this.close = false;
      // document.getElementsByTagName("h1")[0].style.top = '0'
      document.getElementsByClassName("middle").forEach((element) => {
        element.style.height = "auto";
        element.style.transform = "translateY(0)";
      });
    },
    close_menu() {
      this.close = true;
      document.getElementsByClassName("middle").forEach((element) => {
        element.style.height = "0";
        element.style.transform = "translateY(-20rem)";
      });
    },
    getLastUpdate(update) {
      return moment(String(update)).calendar();
    },
    ...mapActions({
      fetch_balances: "balances/FETCH_BALANCES",
      fetch_wallets: "wallets/FETCH_WALLETS",
      synchronyse: "synchronyse/SYNCHRONYSE",
      fetch_means_trades: "means_trades/FETCH_MEANS_TRADES",
      fetch_walletevolutions: 'walletevolutions/FETCH_WALLETEVOLUTIONS',
      fetch_platforms: 'platform/FETCH_PLATFORMS',
      fetch_trades_closed: 'trades_closed/FETCH_TRADES_CLOSED',
      fetch_trades_open: 'trades_open/FETCH_TRADES_OPEN',
      fetch_transferts: 'transferts/FETCH_TRANSFERTS',
      fetch_transferts_ordered: 'transferts_ordered/FETCH_TRANSFERTS_ORDERED',
      
    }),
    async get_synchro() {
      this.loading = true;
      try {
        await this.synchronyse({
          user_id: this.user.id,
          platform_id: this.platforms.id,
        });
        // await this.synchronyse({
        //   user_id: this.user.id,
        //   platform_id: this.platform_id,
        // });
        this.loading = false;
      } catch (error) {
        console.log(error);
        this.loading = false;
      }
    },
  },
  async mounted() {
    var user = "";
    let cookies = document.cookie.split(";");
    cookies.forEach((cookie) => {
      let goodOne = cookie.trim().startsWith("profil" + "=");
      if (goodOne) {
        user = cookie.trim().split("profil=")[1];
        this.$store.commit("auth/SET_USER", JSON.parse(user));
        this.$store.state.auth.connected = true;
      }
    });
    if (this.connected) {
      await this.fetch_wallets({
        user_id: this.user.id,
      });
    }
    if (this.connected && this.had_wallet) {
      this.wallets.forEach(async (wallet) => {
        await this.fetch_balances({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_means_trades({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_walletevolutions({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_platforms({
          platform_id: wallet.platform_id,
        });
        await this.fetch_trades_closed({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_trades_open({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_transferts({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
        await this.fetch_transferts_ordered({
          user_id: this.user.id,
          platform_id: wallet.platform_id,
        });
      });
    }
  },
};
</script>

<style lang="scss">
.loader {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #ffae42;
  border-right: 5px solid #ffae42;
  border-left: 5px solid #ffae42;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
