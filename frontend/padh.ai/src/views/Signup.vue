<template>
  <div class="box">
    <div class="board">
      <div class="container board_body">
        <div class="col">
          <div class="brand_space">
            <div class="logo">
              <img src="@/assets/padhai.png" alt="logo">
            </div>
            <div class="brand_text">
              <div>
                <h2>Create Account</h2>
                <span>to access padhai</span>
              </div>
            </div>
          </div>
        </div>
        <div class="col">
          <form method="POST" @submit.prevent="handleFormSubmit" class="float-right">
            <div class="form-floating mb-3">
              <input type="text" :class="{ 'form-control': true, 'is-invalid': v$.first_name.$error }"
                v-model="first_name" name="first_name" id="floatingInput1" placeholder="first_name"
                autocomplete="off" />
              <label for="floatingInput1">first_name</label>
              <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.first_name.$error">
                <span>{{ v$.first_name.$errors[0].$message }}</span>
              </div>
            </div>
            <div class="form-floating mb-3">
              <input type="text" :class="{ 'form-control': true, 'is-invalid': v$.last_name.$error }"
                v-model="last_name" name="last_name" id="floatingInput2" placeholder="last_name" autocomplete="off" />
              <label for="floatingInput2">last_name</label>
              <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.last_name.$error">
                <span>{{ v$.last_name.$errors[0].$message }}</span>
              </div>
            </div>
            <div class="form-floating mb-3">
              <input type="email" :class="{ 'form-control': true, 'is-invalid': v$.email.$error }" v-model="email"
                name="email" id="floatingInput3" placeholder="email" autocomplete="off" />
              <label for="floatingInput3">email</label>
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
            <div class="form-floating mb-3">
              <input type="password" :class="{
                'form-control': true,
                'is-invalid': v$.repeatPassword.$error,
              }" v-model="repeatPassword" name="repeat_password" id="floatingPassword2"
                placeholder="repeat the same password as above" autocomplete="off" />
              <label for="floatingPassword2">Repeat Password</label>
              <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.repeatPassword.$error">
                <span>{{ v$.repeatPassword.$errors[0].$message }}</span>
              </div>
            </div>
            <button class="w-100 btn btn-lg btn-submit" type="submit">
              Sign Up
            </button>
            <hr class="my-4" />
            <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="errStatus">
              <strong>{{ errormsg }}</strong>.
              <button type="button" class="btn-close" aria-label="Close" @click="errStatus = false"></button>
            </div>
            <small>Have an account? <router-link to="/login">Login now</router-link>
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
  sameAs,
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
      first_name: "",
      last_name: "",
      email: " ",
      password: "",
      repeatPassword: "",
      errormsg: "",
      errStatus: false,
    };
  },
  validations() {
    return {
      first_name: {
        required: helpers.withMessage(
          "The first_name field is required",
          required
        ),
        alphaNum: helpers.withMessage(
          "The first_name must contain only letters and numbers",
          alphaNum
        ),
      },
      last_name: {
        required: helpers.withMessage(
          "The last_name field is required",
          required
        ),
        alphaNum: helpers.withMessage(
          "The last_name must contain only letters and numbers",
          alphaNum
        ),
      },
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
      repeatPassword: {
        required: helpers.withMessage(
          "The confirm password field is required",
          required
        ),
        sameAsPassword: helpers.withMessage(
          "The passwords should match",
          sameAs(this.password)
        ),
      },
    };
  },
  methods: {

    async handleFormSubmit() {
      this.v$.$touch();
      if (this.first_name) {
        let payload = {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
        }
        let request = {
          url: __API_URL__ + "auth/register",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
          data: JSON.stringify(payload),
        };
        // let response = await axios(request)
        // console.log(response)
        // alert(response.data)
        await axios(request).then((response) => {
          console.log(response);
          alert("User registered successfully, redirecting to login page");
          this.$router.push("/login");
        })
          .catch((error) => {
            console.log(error.response.data.errStatus);
            this.errormsg = error.response.data.message;
            this.errStatus = true;
          });
      }
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

.board {
  background-color: var(--ivory);
  border-radius: 2em;
  box-shadow: 5px 5px 15px 2px var(--dark-green);
  width: 100%;
  padding: 1em;
  text-align: center;
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
