<template>
  <div>
    <h2>Last Open Trades :</h2>
    <div class="trades-tab">
      <p style="font-weight: 600">Date</p>
      <p style="font-weight: 600">Symbol</p>
      <p style="font-weight: 600">Type</p>
      <p style="font-weight: 600">Quantity</p>
      <p style="font-weight: 600">Price</p>
    </div>
    <div
      class="trades-tab"
      v-for="trade_closed in trades_open_ordered.slice(0, limit)"
      :key="trade_closed.id"
      :trade_closed="trade_closed"
    >
      <p>{{ trade_closed.date }}</p>
      <p>{{ trade_closed.symbol }}</p>
      <p>{{ trade_closed.type }}</p>
      <p>{{ trade_closed.quantity }}</p>
      <p>{{ trade_closed.price }}</p>
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
      trades_open_ordered: Array,
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