<template>
  <div>
    <div class="section" v-if="connected && had_wallet && synchro">
      <div class="title">
        <h1>Wallets</h1>
        <button v-on:click="add_wallet = true">Add a Wallet</button>
      </div>
      <div class="wallet-content">
        <div class="square">
          <div v-for="wallet in wallets" :key="wallet.id" :wallet="wallet">
            <h2>{{ platforms.platform_name }}</h2>
            <h3>{{ wallet.name }}</h3>
            <p class="last_update">
              Updated {{ getLastUpdate(balances[0].updated_at) }}
            </p>
          </div>
        </div>
        <div class="square">
          <h2>
            Total :
            <span>${{ Math.round(parseFloat(total) * 100) / 100 }}</span>
          </h2>
          <br />
          <LastTradesClosed :trades_closed_ordered="trades_closed_ordered" :limit="limit"/>
        </div>
      </div>
    </div>
    <div v-else-if="connected && had_wallet">
      <PleaseSynchro />
    </div>
    <div v-else-if="connected">
      <PleaseAddWallet />
    </div>
    <div v-else>
      <PleaseConnect />
    </div>
  </div>
</template>

<script>
import moment from "moment";
import { mapState } from "vuex";
import PleaseAddWallet from "@/components/PleaseAddWallet.vue";
import PleaseConnect from "@/components/PleaseConnect.vue";
import LastTradesClosed from "@/components/trades/LastTradesClosed.vue";
import PleaseSynchro from "@/components/PleaseSynchro.vue";

export default {
  name: "Wallets",
  data() {
    return {
      limit: 5,
    };
  },
  components: {
    PleaseConnect,
    PleaseAddWallet,
    PleaseSynchro,
    LastTradesClosed,
  },
  computed: {
    ...mapState("balances", {
      total: (state) => state.total,
      balances: (state) => state.balances,
    }),
    ...mapState("synchronyse", {
      synchro: (state) => state.synchro,
    }),
    ...mapState("auth", {
      user: (state) => state.user,
      connected: (state) => state.connected,
    }),
    ...mapState("wallets", {
      had_wallet: (state) => state.had_wallet,
      wallets: (state) => state.wallets,
    }),
    ...mapState("platform", {
      platforms: (state) => state.platforms,
    }),
    ...mapState("trades_closed", {
      trades_closed_ordered: (state) => state.trades_closed_ordered,
    }),
  },
  methods: {
    getLastUpdate(update) {
      return moment(String(update)).calendar();
    },
  },
  async mounted() {
  },
};
</script>

<style lang="scss">
</style>
