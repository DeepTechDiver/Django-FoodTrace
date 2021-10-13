<template>
  <div id="main1" :style="{width: '100%', height: '500px'}"></div>

</template>

<script>
import * as echarts from 'echarts/core';
import {
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
} from 'echarts/components';
import {
  LineChart
} from 'echarts/charts';
import {
  CanvasRenderer
} from 'echarts/renderers';

echarts.use(
    [TitleComponent, ToolboxComponent, TooltipComponent, GridComponent, LegendComponent, LineChart, CanvasRenderer]
);

export default {
  name: "echart2",
  data(){
    return{
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine(){
      this.axios.post('echarts12')
          .then((res)=>{
            let datelist = res.data.data.date
            let shengchan = res.data.data.production
            let shougou = res.data.data.bidders
            let yunshu = res.data.data.transport
            let xiaoshou = res.data.data.sale
            let xiaofei = res.data.data.consume

            // 绘制图表
            var chartDom = document.getElementById('main1');
            var myChart = echarts.init(chartDom);
            var option;
            window.addEventListener("resize", function() {
              myChart.resize();
            });

            option = {
              title: {
                text: '折线图堆叠'
              },
              tooltip: {
                trigger: 'axis'
              },
              legend: {
                data: ['生产', '收购', '运输', '销售', '消费']
              },
              grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
              },
              toolbox: {
                feature: {
                  saveAsImage: {}
                }
              },
              xAxis: {
                type: 'category',
                boundaryGap: false,
                data: datelist
              },
              yAxis: {
                type: 'value'
              },
              series: [
                {
                  name: '生产',
                  type: 'line',
                  stack: '总量',
                  data: shengchan
                },
                {
                  name: '收购',
                  type: 'line',
                  stack: '总量',
                  data: shougou
                },
                {
                  name: '运输',
                  type: 'line',
                  stack: '总量',
                  data: yunshu
                },
                {
                  name: '销售',
                  type: 'line',
                  stack: '总量',
                  data: xiaoshou
                },
                {
                  name: '消费',
                  type: 'line',
                  stack: '总量',
                  data: xiaofei
                }
              ]
            };

            option && myChart.setOption(option);

          })



    }
  }
}
</script>

<style scoped>

</style>