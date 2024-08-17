<template>
    <NavBar></NavBar>
    <div class="container-fluid">
        <div class="row">
            <SideNavBar :coursePage=true ref="sideNav"></SideNavBar>
            <div v-if="courseInfoFlag">
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4" v-if="courseInfo">
    <div class="card my-4 shadow-sm" style="width: 40%;">
        <div class="card-header bg-onix text-white">
            <h5 class="mb-0">Course Information</h5>
        </div>
        <div class="card-body">
            <h5 class="card-title text-secondary">Course Title</h5>
            <p class="card-text">{{ courseInfo.title }}</p>
            <h6 class="card-title text-secondary">Course ID:</h6>
            <p class="card-text">{{ courseInfo.course_id }}</p>

            <h6 class="card-title text-secondary">Instructor:</h6>
            <p class="card-text mb-1">
                {{ courseInfo.instructor.first_name }} 
                {{ courseInfo.instructor.last_name }}
            </p>
            <p class="card-text">
                <a href="mailto:{{ courseInfo.instructor.email }}" class="text-decoration-none">
                    {{ courseInfo.instructor.email }}
                </a>
            </p>
        </div>
    </div>
</div>
            </div>
            <div v-else>
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <div class="containter pt-5" v-if="weekContents">
                        <h2> {{ weekContents.lecture_title }} </h2>
                        <iframe width="100%" height="530" :src=videoUrl title="YouTube video player" frameborder="0"
                            class="mt-2"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
                            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <ChatWindow></ChatWindow>
</template>
<script>
import axios from 'axios';
import NavBar from '@/components/NavBar.vue';
import SideNavBar from '@/components/SideNavBar.vue';
import ChatWindow from '@/components/ChatWindow.vue';
export default {
    name: 'CourseMain',
    components: {
        NavBar,
        SideNavBar,
        ChatWindow,
    },
    data() {
        return {
            courseInfo: null,
            courseInfoFlag: true,
            courseId: this.uppercase(this.$route.params.courseId),
            contentId: null,
            weekContents: null,
            videoUrl: "https://www.youtube.com/embed/8ndsDXohLMQ",
            subtitleUrl: "https://backend.seek.onlinedegree.iitm.ac.in/21t2_cs1002/assets/img/Lec1W1.vtt"
        }
    },
    async beforeMount() {
        let request = {
            url: __API_URL__ + "courses" + `/${this.courseId}`,
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
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
        if (response.status == 200) {
            this.courseInfo = response.data;
        } else {
            console.log("Error");
        }
        if (this.$route.query.contentId) {
            this.courseInfoFlag = false;
            this.contentId = this.$route.query.contentId;
            let request = {
                url: __API_URL__ + "courses" + `/${this.courseId}` + "/contents" + `/${this.contentId}`,
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                    "Access-Control-Allow-Origin": "*",
                },
            };
            let response = await axios(request).catch((error) => {
                if (error.response.status === 401) {
                    console.log(error.response.data.msg);
                    if (error.response.data.msg === "Token has expired") {
                        localStorage.removeItem('Auth-Token');
                        this.$router.push('/login');
                    }
                };
                if (error.response.status === 404) {
                    console.log(error.response.data.message);
                    if (error.response.data.message === "Content ID : " + `${this.contentId} ` + "not found in course CS1002") {
                        alert(error.response.data.message + " Redirecting to course page");
                        this.courseInfoFlag = true;
                        this.$router.push('/course/' + `${this.courseId}`);
                    }
                    if (error.response.data.message === "Course" + `${this.courseId}` + "doesn't exist") {
                        alert(error.response.data.message + " Redirecting to dashboard");
                        this.courseInfoFlag = true;
                        this.$router.push('/dashboard');
                    }
                }
            });
            if (response.status == 200) {
                this.weekContents = response.data;
                this.videoUrl = this.getembedURL(this.weekContents.lecture_url);
                this.subtitleUrl = this.weekContents.transcript_url;
            }
        }
    },
    methods: {
        uppercase: function (str) {
            return str.toUpperCase();
        },
        getembedURL: function (url) {
            url = url.replace("watch?v=", "embed/");
            return url;
        },
    },
}
</script>
<style>
.bg-onix{
    background-color: #202B22;
}
</style>