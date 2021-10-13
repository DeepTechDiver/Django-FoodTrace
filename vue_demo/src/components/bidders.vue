<template>
  <el-container class="container">
    <el-aside width="200px" class="aside">
      <el-menu default-active="2" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
<!--        <el-menu-item index="1"  @click="index = 1">-->
<!--          <span slot="title">首页</span>-->
<!--        </el-menu-item>-->
        <el-menu-item index="2" @click="menu2">
          <span slot="title">信息管理</span>
        </el-menu-item>
        <el-menu-item index="3" @click="menu3">
          <span slot="title">个人信息</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header>
        <span style="font-size: 20px;line-height: 60px">食品生鲜溯源系统-收购商</span>
        <div style="float: right;line-height: 60px">
          <span style="margin-right: 10px">欢迎用户:{{usename}}</span>
          <el-button type="text" @click="login_out">登出</el-button>
        </div>
      </el-header>
      <div style="border-top: 1px solid #2c3e50;padding: 0"></div>
      <el-main v-show="index == 2">
        <el-button style="float: left;margin-bottom: 20px" @click="dialogFormVisible_1 = true">
          <i class="el-icon-plus"></i> 添加订单
        </el-button>
        <el-dialog title="创建食品订单" :visible.sync="dialogFormVisible_1" append-to-body>
          <el-form :model="order_id_info" label-width="90px" style="width: 400px;margin: 0 auto">
            <el-form-item label="订单编号">
              <el-input v-model="order_id_info.id"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="id_info">下一步</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
        <el-dialog title="填写生产者信息" :visible.sync="dialogFormVisible_2" append-to-body>
          <el-form :model="bidders" label-width="90px" style="width: 400px;margin: 0 auto">
            <el-form-item label="订单编号">
              <span>{{bidders.id}}</span>
            </el-form-item>
            <el-form-item label="食品名称">
              <span>{{bidders.feedname}}</span>
            </el-form-item>
            <el-form-item label="收购单位">
              <el-input v-model="bidders.customer"></el-input>
            </el-form-item>
            <el-form-item label="负责人">
              <el-input v-model="bidders.people"></el-input>
            </el-form-item>
            <el-form-item label="联系电话">
              <el-input v-model="bidders.phone"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="bidders_order">提交订单</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
        <el-table :data="tableData" border width="100%">
          <el-table-column prop="id" label="ID" width="100"></el-table-column>
          <el-table-column prop="customer" label="收购单位" width="190"></el-table-column>
          <el-table-column prop="address" label="订单用户" width="250"></el-table-column>
          <el-table-column prop="people" label="生产负责人" width="100"></el-table-column>
          <el-table-column prop="phone" label="联系电话" width="190"></el-table-column>
          <el-table-column prop="date" label="生产时间" ></el-table-column>
        </el-table>
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
      dialogFormVisible_1 : false,
      dialogFormVisible_2 : false,
      password_change:false,
      address_change: false,
      role_change:false,
      options:[{
        value: 'root',
        label: 'root'
      },{
        value: '生产商',
        label: '生产商'
      },{
        value: '收购商',
        label: '收购商'
      },{
        value: '运输商',
        label: '运输商'
      },{
        value: '销售商',
        label: '销售商'
      },{
        value: '消费者',
        label: '消费者'
      },{
        value: '游客',
        label: '游客'
      }],
      form:{
        username:'',
        password:'',
        address:'',
        role:''
      },
      order_id_info:{
        id:''
      },
      bidders:{
        id:'',
        feedname:'',
        customer:'',
        people:'',
        phone:''
      },
      tableData:[]
    }
  },
  mounted(){
    this.menu2()
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
    id_info(){
      let data = {
        username :this.username,
        id: this.order_id_info.id
      }
      this.bidders.id = this.order_id_info.id
      this.axios.post('/get_id_info',data)
          .then((res)=>{
            this.bidders.feedname = res.data.data
          })
          .catch((res)=>{
            console.log(res);
          })
      this.dialogFormVisible_1 = false
      this.dialogFormVisible_2 = true
    },
    bidders_order(){
      let data = {
        username :this.username,
        id : this.bidders.id,
        customer: this.bidders.customer,
        people: this.bidders.people,
        phone : this.bidders.phone
      }
      this.axios.post('/bidders_order',data)
          .then((res)=>{
            console.log(res);
            if (res.data.code == 200){
              this.dialogFormVisible_2 = false
              alert("提交成功!")
              this.menu2()
            }else {
              alert("提交失败")
            }
          })
          .catch((res)=>{
            console.log(res);
          })

    },
    menu2(){
      let data = {
        token : this.$cookies.get('token')
      }
      this.index = 2
      this.tableData = []
      this.axios.post('get_bidders_order',data)
          .then((res)=>{
            console.log(res);
            this.tableData = res.data.data
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