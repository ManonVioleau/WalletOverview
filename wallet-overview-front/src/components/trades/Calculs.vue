<template>
  <div>
    <h2>Mean Buy and Sell</h2>
    <div id="trades-datas">
      <p>Coin</p>
      <p>Mean Buy</p>
      <p>Mean Sell</p>
      <p>Buy - Sell</p>
    </div>
    <div
      v-for="mean_trade in means_trades"
      :key="mean_trade.id"
      :mean_trade="mean_trade"
    >
      <div id="trades-datas" v-if="mean_trade.mean_buy > mean_trade.mean_sell">
        <p style="color: red">{{ mean_trade.coin }}</p>
        <p style="color: red">{{ mean_trade.mean_buy }}</p>
        <p style="color: red">{{ mean_trade.mean_sell }}</p>
        <p>{{ mean_trade.buy_minus_sell }}</p>
      </div>
      <div id="trades-datas" v-if="mean_trade.mean_buy < mean_trade.mean_sell">
        <p style="color: green">{{ mean_trade.coin }}</p>
        <p style="color: green">{{ mean_trade.mean_buy }}</p>
        <p style="color: green">{{ mean_trade.mean_sell }}</p>
        <p>{{ mean_trade.buy_minus_sell }}</p>
      </div>
    </div>
    <!-- <p class='last_update'>Last update : {{getLastUpdate(balances[0].updated_at)}}</p> -->
  </div>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment";

export default {
  name: "Calculs",
  components: {},
  props: {},
  data() {
    return {
    };
  },
  computed: {
    ...mapState("means_trades", {
      means_trades: (state) => state.means_trades,
    }),
  },
  methods: {
    getLastUpdate(update) {
      return moment(String(update)).calendar();
    },
  },
  async mounted() {},
};
</script>

<style lang="scss">
</style>
