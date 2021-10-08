<script>
import { Pie } from "vue-chartjs";
import "chartjs-plugin-labels";

export default {
  extends: Pie,
  data() {
    return {
      options: {
        tooltips: {
          // enabled: false,
        },
        legend: {
          display: true,
        },
        responsive: true,
        maintainAspectRatio: false,
        // pieceLabel: {
        //   mode: "percentage",
        //   precision: 1,
        // },
        plugins: {
          // datalabels: {
          //   formatter: (value, ctx) => {
          //     let sum = 0;
          //     let dataArr = ctx.chart.data.datasets[0].data;
          //     dataArr.map(data => {
          //       sum += data;
          //     })
          //     let percentage = (value*100 / sum).toFixed(2)+"%";
          //     return percentage
          //   },
          //   color: 'rgba(0, 0, 0, 1)'
          // }
          // labels: [
          //   {
          //     render: "percentage",
          //     fontColor: 'rgba(0, 0, 0, 1)',
          //     precision: 2,
          //   },
          // ],
        },
      },
      chartData: {},
    };
  },
  props: {
    datas: Array,
  },
  methods: {
    get_datas() {
      let labels = this.datas.map((elem) => elem.label);
      let data = this.datas.map((elem) => elem.data);

      let colors_back = [];
      let colors_border = [];
      let color = "";
      for (let index = 0; index < this.datas.length; index++) {
        if (index == 0) {
          color = "242, 157, 82";
        } else if (index == 1) {
          color = "4, 135, 217";
        } else if (index == 2) {
          color = "242, 107, 143";
        } else if (index == 3) {
          color = "5, 242, 242";
        } else if (index == 4) {
          color = "191, 104, 73";
        } else if (index % 2 != 0) {
          color = "73, 191, 104";
        } else {
          color = "5, 242, 242";
        }
        const color_back = `rgba(${color}, 0.2)`;
        const color_border = `rgba(${color}, 0.5)`;
        colors_back.push(color_back);
        colors_border.push(color_border);
      }
      this.chartData = {
        labels: labels,
        datasets: [
          {
            label: "Pie Chart",
            data: data,
            fill: true,
            borderColor: colors_border,
            backgroundColor: colors_back,
            borderWidth: 1,
          },
        ],
      };
    },
  },
  async mounted() {
    await this.get_datas();
    await this.renderChart(this.chartData, this.options);
    // let ctx = document.getElementById("pie-chart").getContext('2d');
    // let myChart = new Pie(ctx, {
    //   type: 'pie',
    //   data: {
    //     datasets: this.chartData
    //   },
    //   options: this.options,
    // })
  },
};
</script>
