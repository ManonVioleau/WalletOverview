<template>
  <div>
    <h2>Portfolio Evolution</h2>
    <!-- {{transferts_ordered}} -->
    <div id="line-chart">
        <LineChart :walletevolutions="walletevolutions" :transferts_ordered="transferts_ordered"/>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import LineChart from "@/components/dashboard/LineChart.vue";

export default {
  name: "WalletEvolution",
  components: {
    LineChart,
  },
  props: {},
  data() {
    return {
    };
  },
  computed: {
    ...mapState("walletevolutions", {
      walletevolutions: (state) => state.walletevolutions,
    }),
    ...mapState("transferts_ordered", {
      transferts_ordered: (state) => state.transferts_ordered,
    }),
  },
  methods: {
  },
  async mounted() {
  },
};
</script>

<style lang="scss">
</style>
