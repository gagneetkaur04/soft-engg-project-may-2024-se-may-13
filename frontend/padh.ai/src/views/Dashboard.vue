<template>
  <div>
    <NavBar></NavBar>  
    <div class="d-flex justify-content-center align-items-center pt-5 px-4">
      <div class="row">
        <h1>Dashboard</h1>
        <h3 class="mx-1">Current Courses</h3>
        
      <div class="container mt-4 ">
        <div class="row">
          <div v-for="course in courses" :key="course.course_id" class="col-md-4 mb-4">
            <div class="card custom-card">
              <div class="card-body justify-content-center">
                <h5 class="card-title">{{ course.title }}</h5>
              </div>
              <div class="card-footer footer-radius">
                <router-link :to="'/course/' + course.course_id" class="btn">View Course</router-link>
              </div>
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  <ChatWindow></ChatWindow>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from '@/components/NavBar.vue';
import ChatWindow from '@/components/ChatWindow.vue';
import SideNavBar from '@/components/SideNavBar.vue';

export default {
  name: 'Dashboard',
  components: {
    NavBar,
    ChatWindow,
    SideNavBar,
  },
  data() {
    return {
      courses: [],
    };
  },
  async beforeMount() {
    let request = {
      url: __API_URL__ + 'courses/',
      method: "GET",
      headers: { 'content-type': 'application/json', "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}` },

    };

    let response = await axios(request).catch((error) => {
      if (error.response.status === 401) {
        console.log(error.response.data.msg);
        if (error.response.data.msg === "Token has expired") {
          localStorage.removeItem('Auth-Token');
          this.$router.push('/login');
        }
      }
    });

    if (response && response.status == 200) {
      this.courses = response.data;
    } else {
      console.log("Error fetching courses");
    }
  }
};
</script>

<style scoped>

.container{
  padding-top: 5%;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.card-img-top {
  height: 200px;
  object-fit: cover;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.card-text {
  color: #6c757d;
}

.card-footer {
  background-color: #f8f9fa;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}

.custom-card {
  height: 250px;
  width: auto;
  border-radius: 15px;
}
.footer-radius{
  border-radius: 15px;
  
}

</style>
