<template>
  <div>
    <h2>Wallet Value : <span>${{ Math.round(parseFloat(total) * 100) / 100 }}</span></h2>
    <div id="pie-chart">
      <PieChart :datas="datas" />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import PieChart from "@/components/dashboard/PieChart.vue";
// import moment from "moment";

export default {
  name: "Balances",
  components: {
    PieChart,
  },
  props: {},
  data() {
    return {
    };
  },
  computed: {
    ...mapState("balances", {
      total: (state) => state.total,
      datas: (state) => state.datas,
      balances: (state) => state.balances,
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
