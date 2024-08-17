<template>
  <header class="navbar navbar-dark sticky-top topnav flex-md-nowrap p-0 shadow">
    <router-link to="/dashboard" class="navbar-brand col-md-3 col-lg-2 me-0 px-4 fs-4 d-flex">
      <img src="../assets/padhai_logo.png" alt="padhai" width="50" height="50"> 
      <span style="align-self: flex-end;">PADH.AI</span>
    </router-link>
    <div class="navbar-nav topnav_user">
      <div class="nav-item text-nowrap">
        <div class="dropdown px-3 float-end">
          <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
            id="dropdownUser" data-bs-toggle="dropdown" aria-expanded="false">
            <strong>{{ email }}</strong>
          </a>
          <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser"
            data-popper-placement="bottom-end"
            style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(15px, 34px, 0px);">
            <router-link to="/logout" class="dropdown-item">logout</router-link>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
export default {
  name: 'NavBar',
  data: function () {
    return {
      email: localStorage.getItem("email"),
      Auth_Token: localStorage.getItem("Auth-Token"),
    }
  },
}
</script>
<style>
.topnav{
  background-color: var(--dark-green);
}
.navbar {
  z-index: 25;
}

.navbar-brand {
  padding-top: .75rem;
  padding-bottom: .75rem;
  font-family: 'Roboto', sans-serif;
}

.navbar-brand a:hover{
  text-decoration: none;
  background-color: none;
}

.navbar .navbar-toggler {
  top: .25rem;
  right: 1rem;
}

@media (max-width:768px) {
  .topnav_user {
    width: 100% !important
  }
}
</style>