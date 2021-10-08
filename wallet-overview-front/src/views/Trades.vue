<template>
  <div class="section">
    <div class="title">
      <h1>Trades</h1>
    </div>
    <div class="">
      <div class="square">

          <LastTradesClosed :trades_closed_ordered="trades_closed_ordered" :limit="limit"/>
      </div>
      <div class="square">
        <Calculs />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Calculs from "@/components/trades/Calculs.vue";
import LastTradesClosed from "@/components/trades/LastTradesClosed.vue";

export default {
  name: "Dashboard",
  data() {
    return {
      limit: 10,
    };
  },
  components: {
    Calculs,
    LastTradesClosed,
  },
  computed: {
    ...mapState("trades_closed", {
      trades_closed_ordered: (state) => state.trades_closed_ordered,
    }),
  },
  methods: {},
  async mounted() {},
};
</script>

<style lang="scss">
</style>
