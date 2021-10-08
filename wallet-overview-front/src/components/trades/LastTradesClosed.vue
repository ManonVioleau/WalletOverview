<template>
  <div>
    <h2>Last Trades :</h2>
    <div class="trades-tab">
      <p style="font-weight: 600">Date</p>
      <p style="font-weight: 600">Symbol</p>
      <p style="font-weight: 600">Type</p>
      <p style="font-weight: 600">Trade value ($)</p>
      <p style="font-weight: 600">Fee value ($)</p>
    </div>
    <div
      class="trades-tab"
      v-for="trade_closed in trades_closed_ordered.slice(0, limit)"
      :key="trade_closed.id"
      :trade_closed="trade_closed"
    >
      <p>{{ trade_closed.date }}</p>
      <p>{{ trade_closed.symbol }}</p>
      <p>{{ trade_closed.type }}</p>
      <p>{{ trade_closed.trade_value }}</p>
      <p>{{ trade_closed.fee_value }}</p>
    </div>
  </div>
</template>

<script>
// import { mapState } from "vuex";
// import moment from "moment";

export default {
  name: "Calculs",
  components: {},
  props: {
      trades_closed_ordered: Array,
      limit: Number,
  },
  data() {
    return {
    };
  },
  async mounted() {},
};
</script>

<style lang="scss">
</style>