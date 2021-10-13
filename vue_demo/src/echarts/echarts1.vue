<template>
  <div>
    <div id="main" :style="{width: '100%', height: '500px'}"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import {
  ToolboxComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
} from 'echarts/components';
import {
  BarChart
} from 'echarts/charts';
import {
  CanvasRenderer
} from 'echarts/renderers';

echarts.use(
    [ToolboxComponent, TooltipComponent, GridComponent, LegendComponent, BarChart, CanvasRenderer]
);

export default {
  name: "echart1",
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    }
  },
  mounted() {
    this.drawLine()
  },
  methods: {
    drawLine() {
      this.axios.post('/echarts12')
          .then((res)=>{
            let datelist = res.data.data.date
            let shengchan = res.data.data.production
            let shougou = res.data.data.bidders
            let yunshu = res.data.data.transport
            let xiaoshou = res.data.data.sale
            let xiaofei = res.data.data.consume

            //绘制图表部分
            var app = {};
            var chartDom = document.getElementById('main');
            var myChart = echarts.init(chartDom);
            var option;
            window.addEventListener("resize", function() {
              myChart.resize();
            });
            var posList = [
              'left', 'right', 'top', 'bottom',
              'inside',
              'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
              'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
            ];
            app.configParameters = {
              rotate: {
                min: -90,
                max: 90
              },
              align: {
                options: {
                  left: 'left',
                  center: 'center',
                  right: 'right'
                }
              },
              verticalAlign: {
                options: {
                  top: 'top',
                  middle: 'middle',
                  bottom: 'bottom'
                }
              },
              position: {
                options: posList.reduce(function (map, pos) {
                  map[pos] = pos;
                  return map;
                }, {})
              },
              distance: {
                min: 0,
                max: 100
              }
            };
            app.config = {
              rotate: 90,
              align: 'left',
              verticalAlign: 'middle',
              position: 'insideBottom',
              distance: 15,
              onChange: function () {
                var labelOption = {
                  normal: {
                    rotate: app.config.rotate,
                    align: app.config.align,
                    verticalAlign: app.config.verticalAlign,
                    position: app.config.position,
                    distance: app.config.distance
                  }
                };
                myChart.setOption({
                  series: [{
                    label: labelOption
                  }, {
                    label: labelOption
                  }, {
                    label: labelOption
                  }, {
                    label: labelOption
                  }]
                });
              }
            };
            var labelOption = {
              show: true,
              position: app.config.position,
              distance: app.config.distance,
              align: app.config.align,
              verticalAlign: app.config.verticalAlign,
              rotate: app.config.rotate,
              formatter: '{c}  {name|{a}}',
              fontSize: 16,
              rich: {
                name: {
                }
              }
            };
            option = {
              tooltip: {
                trigger: 'axis',
                axisPointer: {
                  type: 'shadow'
                }
              },
              legend: {
                data: ['生产', '收购', '运输', '销售','消费']
              },
              toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                  mark: {show: true},
                  dataView: {show: true, readOnly: false},
                  magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                  restore: {show: true},
                  saveAsImage: {show: true}
                }
              },
              xAxis: [
                {
                  type: 'category',
                  axisTick: {show: false},
                  data: datelist
                }
              ],
              yAxis: [
                {
                  type: 'value'
                }
              ],
              series: [
                {
                  name: '生产',
                  type: 'bar',
                  barGap: 0,
                  label: labelOption,
                  emphasis: {
                    focus: 'series'
                  },
                  data: shengchan
                },
                {
                  name: '收购',
                  type: 'bar',
                  label: labelOption,
                  emphasis: {
                    focus: 'series'
                  },
                  data: shougou
                },
                {
                  name: '运输',
                  type: 'bar',
                  label: labelOption,
                  emphasis: {
                    focus: 'series'
                  },
                  data: yunshu
                },
                {
                  name: '销售',
                  type: 'bar',
                  label: labelOption,
                  emphasis: {
                    focus: 'series'
                  },
                  data: xiaoshou
                },
                {
                  name: '消费',
                  type: 'bar',
                  label: labelOption,
                  emphasis: {
                    focus: 'series'
                  },
                  data: xiaofei
                }
              ]
            };
            option && myChart.setOption(option);
          })
          .catch((res)=>{
            console.log(res);
          })
    }
  }
}
</script>

<style scoped>


</style>