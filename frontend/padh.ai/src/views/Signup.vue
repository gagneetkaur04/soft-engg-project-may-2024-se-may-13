<template>
  <div class="board">
    <div class="board_body d-flex justify-content-between">
      <div class="brand_space">
        <div class="logo"></div>
        <div>
          <h2>Padh.AI</h2>
        </div>
      </div>
      <form method="POST" @submit.prevent="handleFormSubmit">
        <div class="form-floating mb-3">
          <input type="text" :class="{ 'form-control': true, 'is-invalid': v$.firstname.$error }" v-model="firstname"
            name="firstname" id="floatingInput1" placeholder="firstname" autocomplete="off" />
          <label for="floatingInput1">firstname</label>
          <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.firstname.$error">
            <span>{{ v$.firstname.$errors[0].$message }}</span>
          </div>
        </div>
        <div class="form-floating mb-3">
          <input type="text" :class="{ 'form-control': true, 'is-invalid': v$.lastname.$error }" v-model="lastname"
            name="lastname" id="floatingInput2" placeholder="lastname" autocomplete="off" />
          <label for="floatingInput1">lastname</label>
          <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.lastname.$error">
            <span>{{ v$.lastname.$errors[0].$message }}</span>
          </div>
        </div>
        <div class="form-floating mb-3">
          <input type="email" :class="{ 'form-control': true, 'is-invalid': v$.email.$error }" v-model="email"
            name="email" id="floatingInput3" placeholder="email" autocomplete="off" />
          <label for="floatingInput2">email</label>
          <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.email.$error">
            <span>{{ v$.email.$errors[0].$message }}</span>
          </div>
        </div>
        <div class="form-floating mb-3">
          <input type="password" :class="{ 'form-control': true, 'is-invalid': v$.password.$error }" v-model="password"
            name="password" id="floatingPassword1" placeholder="Password" autocomplete="off" />
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
        <button class="w-100 btn btn-lg" type="submit">
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
export default {
  setup() {
    return {
      v$: useVuelidate(),
    };
  },
  name: "SignUp",
  data: function () {
    return {
      firstname: "",
      lastname: "",
      email: " ",
      password: "",
      repeatPassword: "",
      errormsg: "",
      errStatus: false,
    };
  },
  validations() {
    return {
      firstname: {
        required: helpers.withMessage(
          "The firstname field is required",
          required
        ),
        alphaNum: helpers.withMessage(
          "The firstname must contain only letters and numbers",
          alphaNum
        ),
      },
      lastname: {
        required: helpers.withMessage(
          "The lastname field is required",
          required
        ),
        alphaNum: helpers.withMessage(
          "The lastname must contain only letters and numbers",
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
      handleFormSubmit() {
        console.log("test")
        this.v$.$touch();
    }
  }
};
</script>
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--light-green);
}

.board {
  background-color: var(--ivory);
  border-radius: 2em;
  box-shadow: 5px 5px 15px 2px var(--dark-green);
}

.board_body {
  padding: 1em;
}
</style>
