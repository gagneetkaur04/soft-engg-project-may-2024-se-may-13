<template>
  <NavBar></NavBar>
  <div class="container-fluid">
    <div class="row">
      <SideNavBar></SideNavBar>
    </div>
  </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue';
import SideNavBar from '@/components/SideNavBar.vue';
export default {
  name: 'Dashboard',
  components: {
    NavBar,
    SideNavBar
  }
}
</script>
<style></style>