<template>
  <div  id="main4" style="width: 100%;height: 500px"></div>
</template>

<script>
import * as echarts from 'echarts';
import 'echarts-gl'
export default {
  name: "echart4",
  mounted() {
    this.drewLine()
  },
  methods:{
    drewLine(){
      this.axios.post('/echarts34')
          .then((res)=>{
            let data = res.data.data.data
            let dataX = res.data.data.date
            let dataY = ['生产','收购','运输','销售','消费']
            var vdata = []
            for (var i=0;i<dataY.length;i++){
              vdata[i] = []
            }
            for(var t=0;t<dataY.length;t++){
              var y = dataY[t];
              for(var k=0;k<data[0].length;k++){
                for(var p=0;p<dataX.length;p++){
                  var x = dataX[p];
                  var z = data[t][p];
                  vdata[t].push([x,y,z]);
                }
                break;
              }
            }
            var chart = echarts.init(document.getElementById('main4'));
            chart.setOption({

              xAxis3D: {
                type: 'category',
                name: '',
                data: dataX,
                axisLabel:{
                  show: true,
                  interval: 0  //使x轴都显示
                }
              },
              yAxis3D: {
                type: 'category',
                name: '',
                data: dataY,
                axisLabel:{
                  show: true,
                  interval: 0   //使y轴都显示
                }
              },
              zAxis3D: {
                type: 'value',
                name: ''
              },
              //图例
              legend: {
                orient: 'vertical',
                right: 0,
                top: 100,
                icon: 'roundRect',
                textStyle:{
                  color: '#2c3e50'
                }
              },
              tooltip:{
                show:true
              },
              grid3D: {
                boxWidth: 300,
                boxHeight:120,
                boxDepth: 200,
                axisLine: {
                  show: true,
                  interval: 0,
                  lineStyle: {
                    color: '#2c3e50'
                  }
                },
                viewControl: {
                  distance: 400,
                }
              },
              series:[
                {
                  type: 'bar3D', //当type为line3D时有label没有作用，官网没有label这个配置项
                  name: '生产',
                  itemStyle: {
                    width: 8,   //线的宽度
                    color: 'rgb(165,  0, 38)'   //线的颜色
                  },
                  label:{
                    show:true,
                    position:'top',
                    distance: 0,
                    textStyle: {
                      color:'#000',
                      fontSize:12,
                      borderWidth:0,
                      borderColor:'#2c3e50',
                      backgroundColor:'transparent'
                    }
                  },
                  data:vdata[0]   //线数据和点数据所需要的格式一样
                },
                {
                  type: 'bar3D',
                  name: '收购',
                  lineStyle: {
                    color: 'rgb(215, 48, 39)',  //线的颜色
                    width: 8     //线的宽度
                  },
                  label:{
                    show:true,
                    position:'top',
                    distance: 0,
                    textStyle: {
                      color: '#000',
                      fontSize: 12,
                      borderWidth: 0,
                      borderColor: '#2c3e50',
                      backgroundColor: 'transparent'
                    }
                  },
                  data:vdata[1]
                },
                {
                  type: 'bar3D',
                  name: '运输',
                  lineStyle: {
                    color: 'rgb(254,224,144)',
                    width: 8
                  },
                  label:{
                    show:true,
                    position:'top',
                    distance: 0,
                    textStyle: {
                      color: '#000',
                      fontSize: 12,
                      borderWidth: 0,
                      borderColor: '#2c3e50',
                      backgroundColor: 'transparent'
                    }
                  },
                  data:vdata[2]
                },
                {
                  type: 'bar3D',
                  name: '销售',
                  lineStyle: {
                    color: 'rgb(255,255,191)',
                    width: 8
                  },
                  label:{
                    show:true,
                    position:'top',
                    distance: 0,
                    textStyle: {
                      color: '#000',
                      fontSize: 12,
                      borderWidth: 0,
                      borderColor: '#2c3e50',
                      backgroundColor: 'transparent'
                    }
                  },
                  data:vdata[3]
                },
                {
                  type: 'bar3D',
                  name: '消费',
                  lineStyle: {
                    color: 'rgb(224,243,248)',
                    width: 8
                  },
                  label:{
                    show:true,
                    position:'top',
                    distance: 0,
                    textStyle: {
                      color: '#000',
                      fontSize: 12,
                      borderWidth: 0,
                      borderColor: '#2c3e50',
                      backgroundColor: 'transparent'
                    }
                  },
                  data:vdata[4]
                },
              ]
            })
            window.addEventListener('resize', function () {
              chart.resize();
            });
          })
          .catch((res)=>{
            console.log(res);
          })
    }
  }
}
</script>

<style scoped>
.div{
  background-color: #2c3e50;
}
</style>