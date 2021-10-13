<template>
  <div class="register">
    <h2>用户注册</h2>
    <el-main class="main">
      <el-form class="form" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" clearable></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" show-password clearable></el-input>
        </el-form-item>
        <el-form-item label="address">
          <el-input v-model="form.address" clearable></el-input>
        </el-form-item>
        <el-form-item label="角色">
          <el-select v-model="form.role" placeholder="请选择">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onRegister" style="margin-right: 60px">注册</el-button>
        </el-form-item>
      </el-form>
    </el-main>
  </div>
</template>

<script>
export default {
  name: "Register",
  data(){
    return{
      form:{
        username:'',
        password:'',
        address:'',
        role:''
      },
      options:[{
        value:'生产商',
        label:'生产商'
      },{
        value:'收购商',
        label:'收购商'
      },{
        value:'运输商',
        label:'运输商'
      },{
        value:'销售商',
        label:'销售商'
      },{
        value:'消费者',
        label:'消费者'
      },{
        value:'游客',
        label:'游客'
      }]
    }
  },
  methods:{
    onRegister(){
      this.axios.post('/user/create',this.form)
      .then((res)=>{
        let code = res.data.code
        if (code == 200){
          alert("注册成功")
          this.$router.push('/Login')
        }
      })
      .catch((res)=>{
        console.log(res);
      })
    }
  }
}
</script>

<style scoped>
.register{
  width:400px;
  border: 1px solid darkgrey;
  margin: 100px auto;
  /*border-radius: 10px;*/
}
.form{
  width: 300px;
  /*border: 1px solid darkgrey;*/
}
</style>