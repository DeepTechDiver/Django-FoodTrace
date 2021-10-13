<template>
  <el-container class="container">
    <el-aside width="200px" class="aside">
      <el-menu default-active="1" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
        <el-menu-item index="1"  @click="index = 1">
          <span slot="title">首页</span>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <span>用户操作</span>
          </template>
          <el-menu-item index="2-1" style="padding-left:80px" @click="user_info_axios" :disabled="!(post_role==6)">用户信息</el-menu-item>
<!--          <el-menu-item index="2-2" style="padding-left:80px" @click="user_role_axios" :disabled="!(post_role=='root')">用户权限</el-menu-item>-->
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <span>页面跳转</span>
          </template>
          <el-menu-item index="3-1" style="padding-left:80px" @click="producers" :disabled="!(post_role==1 || post_role==6)">生产页面</el-menu-item>
          <el-menu-item index="3-2" style="padding-left:80px" @click="bidders" :disabled="!(post_role==2 || post_role==6)">收购页面</el-menu-item>
          <el-menu-item index="3-3" style="padding-left:80px" @click="shippers" :disabled="!(post_role==3 || post_role==6)">运输页面</el-menu-item>
          <el-menu-item index="3-4" style="padding-left:80px" @click="sellers" :disabled="!(post_role==4 || post_role==6)">销售页面</el-menu-item>
          <el-menu-item index="3-5" style="padding-left:80px" @click="consumers" :disabled="!(post_role==5 || post_role==6)">消费者页面</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header>
        <span style="font-size: 20px;line-height: 60px">食品生鲜溯源系统</span>
        <div style="float: right;line-height: 60px">
          <span style="margin-right: 10px">欢迎用户: {{username}}</span>
          <el-button type="text" @click="login_out">登出</el-button>
        </div>
      </el-header>
      <div style="border-top: 1px solid #2c3e50;padding: 0"></div>
      <el-main v-show="index == 1">
        <h2>欢迎您</h2>
        <el-row style="margin-top: 10px">
          <el-col  style="height:100%;margin-left: 20px;"  >
            <echart1/>
          </el-col>
        </el-row>
        <el-row style="margin-top: 300px" >
          <el-col style="height: 100%;margin-left: 20px;"  >
            <echart2/>
          </el-col>
        </el-row>
        <el-row style="margin-top: 200px" >
          <el-col :span="11" style="height: 100%;margin-left: 20px;"  >
            <echart3/>
          </el-col>
          <el-col :span="11" style="margin-left: 20px;float: right"  >
            <echart4/>
          </el-col>
        </el-row>
      </el-main>
      <el-main v-show="index == 21">
        <el-table :data="user_info" border style="width: 100%">
          <el-table-column prop="username" label="用户名" width="180"></el-table-column>
          <el-table-column prop="password" label="密码" width="180"></el-table-column>
          <el-table-column prop="address" label="地址" width="400"></el-table-column>
          <el-table-column prop="role" label="预期角色" width="180"></el-table-column>
          <el-table-column prop="real_role" label="真实角色">
            <template slot-scope="scope">
              <el-select v-model="user_info[scope.$index].real_role" @change="role_change(scope.$index)">
                <el-option v-for="item in real_role" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Echart1 from "@/echarts/echarts1";
import Echart2 from "@/echarts/echarts2";
import Echart3 from "@/echarts/echarts3";
import Echart4 from "@/echarts/echarts4";
export default {
  // name: "main",
  components: {Echart4, Echart3, Echart2, Echart1},
  data(){
    return{
      index:1,
      post_role:'',
      username:'',
      user_info:[

      ],
      real_role : [
        {
          value: 1,
          label:'生产者'
        },
        {
          value: 2,
          label:'收购者'
        },
        {
          value: 3,
          label:'运输者'
        },
        {
          value: 4,
          label:'销售者'
        },
        {
          value: 5,
          label:'消费者'
        },
        {
          value: 0,
          label:'游客'
        },
        {
          value: 6,
          label:'root'
        },
      ]
    }
  },
  mounted() {
    this.token_username()
    this.get_user_role()
  },
  methods:{
    login_out(){
      this.$cookies.remove('token')
      this.$router.push('/Login')
    },
    token_username(){
      this.axios.post('/token_username')
      .then((res)=>{
        this.username = res.data.data
      })
      .catch((res)=>{
        console.log(res);
      })
    },
    get_user_role(){
      let data = {
        token : this.$cookies.get('token')
      }
      this.axios.post('/get_user_role',data)
      .then((res)=>{
        this.post_role=res.data.data
      })
      .catch((res)=>{
        console.log(res);
      })
    },
    role_change(role_id){
      let data =  this.user_info[role_id]
      this.axios.post('/main/role_change',data)
        .then((res)=>{
          console.log(res);
        })
        .catch((res)=>{
          console.log(res);
        })
    },
    producers(){
      let routerUrl = this.$router.resolve({
        path:'/production'
      })
      window.open(routerUrl.href,'_black')
    },
    bidders(){
      let routerUrl = this.$router.resolve({
        path:'/bidders'
      })
      window.open(routerUrl.href,'_black')
    },
    shippers(){
      let routerUrl = this.$router.resolve({
        path:'/shippers'
      })
      window.open(routerUrl.href,'_black')
    },
    sellers(){
      let routerUrl = this.$router.resolve({
        path:'/sellers'
      })
      window.open(routerUrl.href,'_black')
    },
    consumers(){
      let routerUrl = this.$router.resolve({
        path:'/consumers'
      })
      window.open(routerUrl.href,'_black')
    },
    user_info_axios(){
      this.index = 21
      this.user_info = []
      this.axios.post('/main/user_info')
      .then((res)=>{
        this.user_info = res.data.data
      })
      .catch((res)=>{
        console.log(res);
      })
    },
    user_role_axios(){
      this.index = 22
      this.user_role = []
      let data = {
        page : 1,
        content : ''
      }
      this.axios.post('main_user_role_info',data)
      .then((res)=>{
        this.user_role = res.data.data

      })
      .catch((res)=>{
        console.log(res);
      })
    },
  }
}
</script>

<style scoped>
.container{
  height: 100%;
  width: 100%;
  position: fixed;
}
.aside{
  background-color: #545c64;
}
.main{
  background-color: #fff;
}
.form{
  width: 400px;
  margin: 0 auto;
}
</style>