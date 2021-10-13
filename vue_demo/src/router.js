import Login from "@/components/Login";
import production from "@/components/producers";
import Register from "@/components/Register";
import bidders from "@/components/bidders";
import shippers from "@/components/shippers";
import sellers from "@/components/sellers";
import consumers from "@/components/consumers";
import main from "@/components/main";
import echarts1 from "@/echarts/echarts1";
import echarts2 from "@/echarts/echarts2";
import echarts3 from "@/echarts/echarts3";
import echarts4 from "@/echarts/echarts4";

export default [
  {path:'/',redirect:'/Login'},
  //  用户登录
  {path: '/Login',component:Login},
  //  用户注册
  {path: '/Register',component: Register},
  //  生产商
  {path: '/production',component: production},
//  收购商
  {path: '/bidders',component: bidders},
//    运输商
  {path: '/shippers',component: shippers},
//  销售商
  {path: '/sellers',component: sellers},
//  消费者
  {path: '/consumers',component: consumers},
//  admin用户
  {path: '/main',component: main},
  {path: '/echarts1',component: echarts1},
  {path: '/echarts2',component: echarts2},
  {path: '/echarts3',component: echarts3},
  {path: '/echarts4',component: echarts4}
]