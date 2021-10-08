<template>
  <div class="section">
    <div class="title">
      <h1>Dashboard</h1>
    </div>
    <div class="content">
      <div class="square" id="balance">
        <Balance />
      </div>
      <div class="square" id="walletevolution">
        <WalletEvolution />
      </div>
      <div class="square" id="lasttrades">
        <LastTradesClosed :trades_closed_ordered="trades_closed_ordered" :limit="limit"/>
      </div>
      <div class="square" id="lasttradesopen">
        <LastTradesOpen :trades_open_ordered="trades_open_ordered" :limit="limit"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Balance from "@/components/dashboard/Balance.vue";
import WalletEvolution from "@/components/dashboard/WalletEvolution.vue";
import LastTradesClosed from "@/components/trades/LastTradesClosed.vue";
import LastTradesOpen from "@/components/trades/LastTradesOpen.vue";

export default {
  name: "Dashboard",
  data() {
    return {
      limit: 10,
    };
  },
  components: {
    Balance,
    WalletEvolution,
    LastTradesClosed,
    LastTradesOpen,
  },
  computed: {
    ...mapState("trades_closed", {
      trades_closed_ordered: (state) => state.trades_closed_ordered,
    }),
    ...mapState("trades_open", {
      trades_open_ordered: (state) => state.trades_open_ordered,
    }),},
  methods: {},
  async mounted() {},
};
</script>

<style lang="scss">
</style>
