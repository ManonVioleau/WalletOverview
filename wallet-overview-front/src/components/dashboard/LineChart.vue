<script>
import { Line } from "vue-chartjs";
import moment from "moment";

export default {
  extends: Line,
  data() {
    return {
      chartData: {},
      datasets: [],
      labels: [],
      options: {
        scales: {
          yAxes: [
            {
              title: "USDT value",
              ticks: {
                beginAtZero: true,
              },
              gridLines: {
                display: true,
              },
            },
          ],
          xAxes: [
            {
              title: "Date",
              gridLines: {
                display: true,
              },
            },
          ],
        },
        legend: {
          display: true,
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  props: {
    walletevolutions: Array,
    transferts_ordered: Array,
  },
  methods: {
    formatDate: (value) => {
      if (value) {
        return moment(String(value)).format("DD-MM-YY");
      }
    },
    getData() {
      // const labels1 = this.walletevolutions.map((elem) =>
      //   this.formatDate(elem.date)
      // );
      // const labels2 = this.transferts.map((elem) => this.formatDate(elem.date));
      // const data1 = this.walletevolutions.map((elem) => elem.wallet_value_USDT);
      // const data2 = this.transferts.map((elem) => elem.dep_with_value);
      // console.log(data1, data2, labels1, labels2);
      // this.chartData = {
      //   labels: labels1,
      //   labels2: labels2,
      //   datasets: [
      //     {
      //       label: "WalletEvolution",
      //       data: data1,
      //       fill: false,
      //       borderColor: "#2554FF",
      //       backgroundColor: "#2554FF",
      //       borderWidth: 1,
      //     },
      //   ],
      //   datasets2: [
      //     {
      //       label: "Transferts",
      //       data: data2,
      //       fill: false,
      //       borderColor: "#f87979",
      //       backgroundColor: "#f87979",
      //       borderWidth: 1,
      //     },
      //   ],
      // };
      // const labels1 = this.walletevolutions.map((elem) =>
      //   this.formatDate(elem.date)
      // );
      const data1 = this.walletevolutions.map((elem) => elem.wallet_value_USDT);
      const data2 = this.transferts_ordered.map((elem) => elem.value);
      const labels1 = this.transferts_ordered.map((elem) =>
        this.formatDate(elem.date)
      );
      console.log(data1)
      console.log(data2)
      this.chartData = {
        labels: labels1,
        datasets: [
          {
            label: "WalletEvolution",
            data: data1,
            fill: false,
            borderColor: "#2554FF",
            backgroundColor: "#2554FF",
            borderWidth: 1,
          },
          {
            label: "Transferts",
            data: data2,
            fill: false,
            borderColor: "#f87979",
            backgroundColor: "#f87979",
            borderWidth: 1,
          },
        ],
      };
    },
  },
  async mounted() {
    await this.getData();
    await this.renderChart(this.chartData, this.options);
  },
};
</script>