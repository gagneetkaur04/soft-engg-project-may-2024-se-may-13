<template>
    <NavBar></NavBar>
    <div class="container-fluid">
        <div class="row">
            <SideNavBar :coursePage=true ref="sideNav"></SideNavBar>
            <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4 d-flex">
                <div class="container pt-5">
                
                        <div v-if="highlights" v-html="renderedHighlights"></div>
                        <p v-else> Loading highlights... </p>
                
                </div>
            </div>


        </div>
        </div>
    <ChatWindow></ChatWindow>
</template>
<script>
import axios from 'axios';
import { marked } from 'marked';
import NavBar from '@/components/NavBar.vue';
import SideNavBar from '@/components/SideNavBar.vue';
import ChatWindow from '@/components/ChatWindow.vue';
export default {
    name: 'CourseHighlights',
    components: {
        NavBar,
        SideNavBar,
        ChatWindow,
    },
    data() {
        return {
            courseId: this.uppercase(this.$route.params.courseId),
            highlights: "",
        }
    },
    computed: {
        renderedHighlights() {
            return marked(this.highlights || '');
        }
    },
    async beforeMount() {
        let request = {
            url: __API_URL__ + "courses" + `/${this.courseId}` + "/highlights",
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
            // console.log(response);

            this.highlights = response.data.highlights;

        } else {
            console.log("Error");
        }
    },

    methods: {
        uppercase: function (str) {
            return str.toUpperCase();
        },
    },
}



</script>
<style></style>