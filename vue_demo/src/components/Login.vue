<template>
  <div class="Login">
    <h2>欢迎登录</h2>
    <el-form class="form" label-width="80px">
      <el-form-item label="用户名" label-width="80px">
        <el-input v-model="loginform.username" clearable></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginform.password" show-password clearable></el-input>
      </el-form-item>
      <el-alert v-show = "code == 201" title="用户不存在" type="error" center show-icon></el-alert>
      <el-alert v-show = 'code == 202' title="密码错误" type="error" center show-icon></el-alert>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
        <el-button @click="onRegister">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data(){
    return{
      loginform:{
        username:'',
        password:''
      },
      code:'0',
    }
  },
  methods:{
    onSubmit(){
      this.axios.post('/user/login',this.loginform)
      .then((res)=>{
        console.log(res);
        let code = res.data.code
        this.code = code
        if(code == 200){
          let token = res.data.data.token
          this.$cookies.set('token',token)
          this.$router.push('/main')
        }
      })
      .catch((res)=>{
        console.log(res);
      })
    },
    onRegister(){
      //新建页面跳转
      let routerUrl = this.$router.resolve({
        path:'/Register'
      })
      window.open(routerUrl.href,'_black')
    }
  }
}
</script>

<style scoped>
.Login{
  /*height: 100%;*/
  /*width: 100%;*/
  /*position: fixed;*/
  /*background-color: #42b983;*/
  border: 1px solid aqua;
  border-radius: 10px;
  width: 400px;
  margin: 150px auto;
}
.form{
  width: 350px;
  margin: 0 auto;
}
.el-button{
  margin-right: 30px;
}
</style>