<template>
  <div>
    <div class="addwallet" v-if="connected">
      <div class="messages" v-if="errors.message && success == true">
        {{ errors.message }}
      </div>
      <h1>Add a Wallet</h1>
      <div>
        <div class="section-add-wallet">
          <form @submit.prevent="add_wallet()" class="square">
            <div class="errors" v-if="errors.message && success == false">
              {{ errors.message }}
            </div>
            <h2>Choose a platform</h2>
            <select v-model="platform" required>
              <option value="Binance">Binance</option>
            </select>
            <h2 style="margin-top: 1rem">Give a name to your Wallet</h2>
            <input type="text" v-model="name" required />
            <h2 style="margin-top: 1rem">API Sync</h2>
            <p>
              We are only requesting view permissions. This does not give us
              access to your private keys nor the ability move your funds.
            </p>
            <h3>API Key</h3>
            <input type="text" v-model="api_key" required />
            <h3>API Secret</h3>
            <input type="password" v-model="api_secret" /> <br />
            <button type="submit">Add Wallet</button>
          </form>
          <div class="square">
            <h2>How to add your Binance account:</h2>
            <p class="infos-add-wallet">
              Open the Binance API page <br />
              Create a new API key by entering a label, such as
              'WalletOverview', and clicking the Create New Key button <br />
              If applicable, enter your two-factor authentication code <br />
              Copy the API Key and Secret <br />
              <span>RECOMMENDED : </span>Disable trading access for this API
              key:
              <br />
              Click the Edit button <br />
              Disable the Enable Trading permission <br />
              Click Save <br />
              If applicable, enter your two-factor authentication code
            </p>
            <p></p>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <PleaseConnect />
    </div>
  </div>
</template>

<script>
// import moment from "moment";
import { mapState, mapActions } from "vuex";
import PleaseConnect from "@/components/PleaseConnect.vue";

export default {
  name: "AddWallet",
  data() {
    return {
      platform: "",
      api_key: "",
      api_secret: "",
      name: "",
    };
  },
  components: { PleaseConnect },
  computed: {
    ...mapState("auth", {
      user: (state) => state.user,
      connected: (state) => state.connected,
    }),
    ...mapState("errors", {
      errors: (state) => state.errors,
    }),
    ...mapState("wallets", {
      success: (state) => state.success,
    }),
  },
  methods: {
    ...mapActions({
      connect_wallet: "wallets/ADD_WALLET",
    }),
    add_wallet() {
      const body = {
        platform_name: this.platform,
        user_id: this.user.id,
        name: this.name,
        api_key: this.api_key,
        api_secret: this.api_secret,
      };
      this.connect_wallet(body);
    },
  },
  async mounted() {},
};
</script>

<style lang="scss">
</style>
