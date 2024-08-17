<template>
  <div class="box">
    <div class="board" style="width: 70%">
      <div class="container board_body">
        <div class="col">
          <div class="brand_space">
            <div class="logo">
              <img src="@/assets/padhai.png" alt="logo">
            </div>
            <div class="brand_text">
              <div>
                <h2>Sign in</h2>
                <span>to visit padhai</span>
              </div>
            </div>
          </div>
        </div>
        <div class="col">
          <form method="POST" @submit.prevent="handleFormSubmit" class="float-right">
            <div class="form-floating mb-3">
              <input type="email" :class="{ 'form-control': true, 'is-invalid': v$.email.$error }" v-model="email"
                name="email" id="floatingInput2" placeholder="email" autocomplete="off" />
              <label for="floatingInput2">email</label>
              <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.email.$error">
                <span>{{ v$.email.$errors[0].$message }}</span>
              </div>
            </div>
            <div class="form-floating mb-3">
              <input type="password" :class="{ 'form-control': true, 'is-invalid': v$.password.$error }"
                v-model="password" name="password" id="floatingPassword1" placeholder="Password" autocomplete="off" />
              <label for="floatingPassword1">Password</label>
              <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.password.$error">
                <span>{{ v$.password.$errors[0].$message }}</span>
              </div>
            </div>
            <button class="w-100 btn btn-lg btn-submit" type="submit">
              Login Now
            </button>
            <hr class="my-4" />
            <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="errStatus">
              <strong>{{ errormsg }}</strong>.
              <button type="button" class="btn-close" aria-label="Close" @click="errStatus = false"></button>
            </div>
            <small>Create an account? <router-link to="/signup">Sign Up now</router-link>
            </small>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useVuelidate } from "@vuelidate/core";
import {
  required,
  alphaNum,
  email,
  helpers,
} from "@vuelidate/validators";
import axios from "axios";
export default {
  setup() {
    return {
      v$: useVuelidate(),
    };
  },
  name: "SignUp",
  data: function () {
    return {
      email: " ",
      password: "",
      errormsg: "",
      errStatus: false,
    };
  },
  validations() {
    return {
      email: {
        required: helpers.withMessage("The email field is required", required),
        email: helpers.withMessage("The email must be valid", email),
      },
      password: {
        required: helpers.withMessage(
          "The password field is required",
          required
        ),
      },
    };
  },
  methods: {
    async handleFormSubmit() {
      let payload = {
        email: this.email,
        password: this.password,
      }
      let request = {
        url: __API_URL__ + "auth/login",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        data: JSON.stringify(payload),
      };
      await axios(request).then((response) => {
        localStorage.setItem("email", this.email);
        localStorage.setItem("Auth-Token", response.data.access_token);
        this.$router.push("/dashboard");
      })
        .catch((error) => {
          console.log(error.response.data.errStatus);
          this.errormsg = error.response.data.message;
          this.errStatus = true;
        });
      this.v$.$touch();
    }
  }
};
</script>
<style>
body {
  display: grid;
  place-items: center;
  background-color: var(--light-green);
  height: 100%;
  margin: 0;
}

.box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0 5em 0 5em;
}

.board_body {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center;
  padding: 1em;
}

.brand_space {
  flex: 1;
  padding-right: 2em;
  /* Takes up equal space */
}

.brand_text {
  display: flex;
  padding-top: 2em;
  justify-content: center;
}

form {
  flex: 2;
  /* Takes up twice the space of brand_space */
}

.logo {
  display: flex;
  justify-content: center;
}

img {
  max-width: 300px;
}

h2 {
  margin: 0;
  font-size: 1.5em;
}
</style>
