<template>
  <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse" style="">
    <div class="position-sticky pt-3">
      <h4 class="d-flex justify-content-between align-items-center mt-4 mb-1" v-if="coursePage">
        <a class="nav-link active" aria-current="page" :href="`/course/${courseId}`">{{ courseTitle
          }}</a>
      </h4>
      <hr style="color: white;">
      <ul class="nav flex-column mb-2">
        <li class="nav-item">
          <div class="card border-dark mb-3">
            <div class="nav-item text-nowrap card-header d-flex justify-content-center" @click="toggleFlag">
              <div>
                <a class="nav-link" aria-current="page" :href="`/course/${courseId}`">
                  <span data-feather="Course Info"></span>
                  Course Info
                </a>
              </div>
            </div>
          </div>
        </li>
        <li class="nav-item" v-for="(value, key) in weeksContents"
          v-if="this.assignments || this.programmingAssignments">
          <SideNavItem :courseId=this.courseId :courseTitle=this.courseTitle :weekNumber=value.week_number
            :weekContents=value.contents :assignment=getAssignment(key) :assignmentType=getAssignmentType()>
          </SideNavItem>
        </li>
        <li class="nav-item">
          <div class="card border-dark mb-3">
            <div class="nav-item text-nowrap card-header d-flex justify-content-center">
              <div>
                <router-link class="nav-link" aria-current="page" :to="{ path: `/course/${courseId}/highlights` }">
                  <span data-feather="Course Highlights"></span>
                  Course Highlights
                </router-link>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>
<script>
import axios from 'axios';
import SideNavItem from './SideNavItem.vue';

export default {
  name: 'SideNavBar',
  data: function () {
    return {
      courseTitle: null,
      courseId: this.uppercase(this.$route.params.courseId),
      weeksContents: null,
      assignments: null,
      programmingAssignments: null,
    }
  },
  components: { SideNavItem },
  props: {
    coursePage: Boolean
  },
  async beforeMount() {
    let request = {
      headers: { 'content-type': 'application/json', "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}` },
      'method': 'GET',
      url: __API_URL__ + `courses/${this.courseId}/contents`,
    };
    await axios(request).then((response) => {
      if (response.status === 200) {
        let data = response.data;
        this.courseTitle = data.course_title;
        this.weeksContents = data.weeks;
      }
      else {
        this.weeksContents = null;
      }
    }).catch((error) => {
      console.log(error);
      if (error.response.status === 401) {
        if (error.response.data.msg === "Token has expired") {
          localStorage.removeItem('Auth-Token');
          this.$router.push('/login');
        }
      };
      if (error.response.status === 404) {
        console.log(error.response.data.message);
        console.log("Course " + `/${this.courseId} ` + "doesn't exist or has no content");
        if (error.response.data.message === "Course " + `${this.courseId} ` + "doesn't exist or has no content") {
          alert("Course not found, redirecting to dashboard");
          this.$router.push('/dashboard');
        }
      }
    });
    if (this.uppercase(this.courseId) != "CS1002") {
      let request_2 = {
        headers: { 'content-type': 'application/json', "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}` },
        'method': 'GET',
        url: __API_URL__ + `assignments/course/${this.courseId}`,
      }
      await axios(request_2).then((response) => {
        if (response.status === 200) {
          let data = response.data;
          this.assignments = data;
        }
        else {
          this.assignments = null;
        }
      }).catch((error) => {
        console.log(error);
        if (error.response.status === 401) {
          if (error.response.data.msg === "Token has expired") {
            localStorage.removeItem('Auth-Token');
            this.$router.push('/login');
          }
        };
        if (error.response.status === 404) {
          if (error.response.data.message === "Course " + `${this.courseId} ` + "doesn't exist or has no content") {
            alert("Course not found, redirecting to dashboard");
            this.$router.push('/dashboard');
          }
        };
      });
    }
    else {
      let request_3 = {
        headers: { 'content-type': 'application/json', "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}` },
        'method': 'GET',
        url: __API_URL__ + 'programming_assignments/',
      }
      await axios(request_3).then((response) => {
        if (response.status === 200) {
          let data = response.data;
          this.programmingAssignments = data;
        }
        else {
          this.programmingAssignments = null;
        }
      }).catch((error) => {
        console.log(error);
        if (error.response.status === 401) {
          if (error.response.data.msg === "Token has expired") {
            alert("Token has expired, redirecting to login page");
            localStorage.removeItem('Auth-Token');
            this.$router.push('/login');
          }
        }
      });
    }
  },
  methods: {
    uppercase: function (str) {
      return str.toUpperCase();
    },
    getAssignmentType() {
      if (this.uppercase(this.courseId) != "CS1002") {
        return "MCQ";
      }
      else {
        return "Programming Assignment";
      }
    },
    getAssignment(key) {
      if (this.uppercase(this.courseId) != "CS1002") {
        let assignmentsData = [];
        for (let i = 0; i < this.assignments.length; i++) {
          if (this.assignments[i].week_number == (key + 1)) {
            assignmentsData.push(this.assignments[i]);
            break;
          }
        }
        return assignmentsData;
      }
      else {
        let assignmentsData = [];
        for (let i = 0; i < this.programmingAssignments.length; i++) {
          if (this.programmingAssignments[i].prog_assignment_id == (key + 1)) {
            assignmentsData.push(this.programmingAssignments[i]);
            break;
          }
        }
        return assignmentsData;
      }
    },
    getWeekContents() {
      console.log(this.weeksContents);
      return this.weeksContents;
    }
  }
}
</script>
<style>
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  padding: 48px 40px 0;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
  overflow-x: hidden;
  overflow-y: auto;
  /* Hide scrollbar for IE, Edge and Firefox */
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.sidebar::-webkit-scrollbar {
  display: none;
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 5rem;
  }
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: hidden;
}

.sidebar .nav-link {
  font-weight: 500;
  color: #fff;
}
</style>