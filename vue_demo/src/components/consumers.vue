<template>
  <el-container class="container">
    <el-aside width="200px" class="aside">
      <el-menu default-active="2" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
<!--        <el-menu-item index="1"  @click="index = 1">-->
<!--          <span slot="title">首页</span>-->
<!--        </el-menu-item>-->
        <el-menu-item index="2" @click="index = 2">
          <span slot="title">信息管理</span>
        </el-menu-item>
        <el-menu-item index="3" @click="menu3">
          <span slot="title">个人信息</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header>
        <span style="font-size: 20px;line-height: 60px">食品生鲜溯源系统-消费者</span>
        <div style="float: right;line-height: 60px">
          <span style="margin-right: 10px">欢迎用户:{{username}}</span>
          <el-button type="text" @click="login_out">登出</el-button>
        </div>
      </el-header>
      <div style="border-top: 1px solid #2c3e50;padding: 0"></div>
      <el-main v-show="index == 2">
        <el-input placeholder="请输入需要查询的商品ID" suffix-icon="el-icon-search" v-model="search" style="width: 300px;margin-right: 20px"></el-input>
        <el-button type="primary" round @click="get_table">搜索</el-button>
        <el-alert title="未找到该订单" type="error" center show-icon v-show="show_alert == true" class="alert"></el-alert>
        <el-row style="margin-top: 20px">
          <el-col :span="12">
            <el-form :model="producers" label-width="90px" class="demo-table-expand" v-show="show_table == true">
              <span>生产商</span>
              <el-form-item label="食物名称" style="margin-top: 20px">
                <span>{{producers.feedname}}</span>
              </el-form-item>
              <el-form-item label="公司单位">
                <span>{{producers.company}}</span>
              </el-form-item>
              <el-form-item label="负责人">
                <span>{{producers.people}}</span>
              </el-form-item>
              <el-form-item label="联系方式">
                <span>{{producers.phone}}</span>
              </el-form-item>
              <el-form-item label="订单时间">
                <span>{{producers.date}}</span>
              </el-form-item>
              <el-form-item label="部署地址">
                <span>{{producers.address}}</span>
              </el-form-item>
            </el-form>
          </el-col>
          <el-col :span="12">
            <el-form :model="bidders" label-width="90px" class="demo-table-expand" v-show="show_table == true">
              <span>收购商</span>
              <el-form-item label="公司单位" style="margin-top: 20px">
                <span>{{bidders.customer}}</span>
              </el-form-item>
              <el-form-item label="负责人">
                <span>{{bidders.people}}</span>
              </el-form-item>
              <el-form-item label="联系方式">
                <span>{{bidders.phone}}</span>
              </el-form-item>
              <el-form-item label="订单时间">
                <span>{{bidders.date}}</span>
              </el-form-item>
              <el-form-item label="部署地址">
                <span>{{bidders.address}}</span>
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form :model="shippers" label-width="90px" class="demo-table-expand" v-show="show_table == true">
              <span style="margin-bottom: 10px">运输商</span>
              <el-form-item label="车牌号" style="margin-top: 20px">
                <span>{{shippers.car_num}}</span>
              </el-form-item>
              <el-form-item label="初始地">
                <span>{{shippers.form_place}}</span>
              </el-form-item>
              <el-form-item label="目的地">
                <span>{{shippers.to_place}}</span>
              </el-form-item>
              <el-form-item label="负责人">
                <span>{{shippers.people}}</span>
              </el-form-item>
              <el-form-item label="联系方式">
                <span>{{shippers.phone}}</span>
              </el-form-item>
              <el-form-item label="订单时间">
                <span>{{shippers.date}}</span>
              </el-form-item>
              <el-form-item label="部署地址">
                <span>{{shippers.address}}</span>
              </el-form-item>
            </el-form>
          </el-col>
          <el-col :span="12">
            <el-form :model="sellers" label-width="90px" class="demo-table-expand" v-show="show_table == true">
              <span>销售商</span>
              <el-form-item label="食品重量" style="margin-top: 20px">
                <span>{{sellers.weight}}</span>
              </el-form-item>
              <el-form-item label="食品价格">
                <span>{{sellers.price}}</span>
              </el-form-item>
              <el-form-item label="保质期">
                <span>{{sellers.day}}</span>
              </el-form-item>
              <el-form-item label="商品信息">
                <span>{{sellers.place}}</span>
              </el-form-item>
              <el-form-item label="负责人">
                <span>{{sellers.people}}</span>
              </el-form-item>
              <el-form-item label="联系方式">
                <span>{{sellers.phone}}</span>
              </el-form-item>
              <el-form-item label="订单时间">
                <span>{{sellers.date}}</span>
              </el-form-item>
              <el-form-item label="部署地址">
                <span>{{sellers.address}}</span>
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
      </el-main>
      <el-main v-show="index == 3">
        <el-form class="form" label-width="80px">
          <el-form-item label="用户名">
            <span style="float: left">{{form.username}}</span>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="form.password" show-password clearable @input="password_change = true"></el-input>
          </el-form-item>
          <el-form-item label="地址">
            <el-input v-model="form.address" clearable @change="address_change = true"></el-input>
          </el-form-item>
          <el-form-item label="角色">
            <el-select v-model="form.role" style="float: left;width: 318px" @change="role_change = true">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onRegister">修改</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "production",
  data(){
    return{
      index:2,
      username:'',
      show_table : false,
      show_alert: false,
      password_change:false,
      address_change: false,
      role_change:false,
      form:{
        nickname:'',
        username:'',
        password:'',
        sex:'',
        phone:'',
        address:'',
        company:''
      },
      search:'',
      producers:{
        feedname:'',
        company:'',
        people:'',
        phone:'',
        date:'',
        address:''
      },
      bidders:{
        customer:'',
        people:'',
        phone:'',
        date:'',
        address:''
      },
      shippers:{
        car_num:'',
        form_place:'',
        to_place:'',
        people:'',
        phone:'',
        date:'',
        address:''
      },
      sellers:{
        weight:'',
        price:'',
        day:'',
        place:'',
        people:'',
        phone:'',
        date:'',
        address:''
      },
    }
  },
  mounted() {
    this.token_username()
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
    onRegister(){
      if (this.password_change == false && this.role_change == false && this.address_change == false){
        alert("您似乎并没有修改什么")
      }else{
        let data = {
          username : this.username,
          password_change:this.password_change,
          address_change:this.address_change,
          role_change:this.role_change,
          password:this.form.password,
          address:this.form.address,
          role:this.form.role
        }
        this.axios.post('/user_info_change',data)
            .then((res)=>{
              if(res.data.code == 200){
                alert("修改成功")
                this.password_change = false
                this.address_change = false
                this.role_change = false
              }else {
                alert("修改失败")
              }
            })
            .catch((res)=>{
              console.log(res);
            })
      }
    },
    get_table(){
      let data = {
        search:this.search,
        username :this.username
      }

      this.axios.post('id_get_all',data)
      .then((res)=>{
        console.log(res);
        let code = res.data.code
        if (code == 200){
          this.show_alert = false
          this.producers = res.data.data[0]
          this.bidders = res.data.data[1]
          this.shippers = res.data.data[2]
          this.sellers = res.data.data[3]
          this.show_table = true

        }else {
          this.show_alert = true
          this.show_table = false
        }
      })
      .catch((res)=>{
        console.log(res);
      })
    },
    menu3(){
      this.index = 3
      let data = {
        username:this.username
      }
      this.axios.post('/personal_info',data)
          .then((res)=>{
            this.form = res.data.data
          })
          .catch((res)=>{
            console.log(res);
          })
    },
    orderSubmit(){

    }
  }
}
</script>

<style>
.container{
  height: 100%;
  width: 100%;
  position: fixed;
}
.alert{
  margin: 20px auto;
  width: 396px;
}
.aside{
  background-color: #545c64;
}
.main{
  background-color: #fff;
}
.demo-table-expand{
  margin-top: 20px;
}
.demo-table-expand label {
  color: #99a9bf;
}
.el-form-item span{
  float: left;
  margin-left: 10px;
}
.form{
  width: 400px;
  margin: 0 auto;
}
</style>