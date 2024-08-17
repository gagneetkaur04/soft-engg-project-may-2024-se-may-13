<template>
    <NavBar></NavBar>
    <div class="container-fluid">
        <div class="row">
            <SideNavBar :coursePage=true ref="sideNav"></SideNavBar>
            <div v-if="courseInfoFlag">
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4" v-if="courseInfo">
                    <h2 class="align-center"> {{ courseInfo.title }}</h2>
                    <div v-html="renderMarkdown(renderKatex(courseInfo.description))">
                    </div>
                </div>
            </div>
            <CodeEditor></CodeEditor>
        </div>
    </div>
    <ChatWindow></ChatWindow>
</template>
<script>
import axios from 'axios';
import NavBar from '@/components/NavBar.vue';
import SideNavBar from '@/components/SideNavBar.vue';
import ChatWindow from '@/components/ChatWindow.vue';
import CodeEditor from './CodeEditor.vue';
import { marked } from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';
export default {
    name: 'CourseMain',
    components: {
        NavBar,
        SideNavBar,
        ChatWindow,
        CodeEditor,
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
    beforeMount() {
        let request = {
            url: __API_URL__ + "programming_assignments" + `/${this.$route.query.progAssignmentId}`,
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
            data: null,
        };
        axios(request)
            .then((response) => {
                this.courseInfo = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
    methods: {
        uppercase: function (str) {
            return str.toUpperCase();
        },
        renderKatex(text) {
            return text.replace(/\$\$([\s\S]*?)\$\$/g, (match, p1) => {
                return `<span class="katex">${katex.renderToString(p1, { throwOnError: false })}</span>`;
            }).replace(/\$([\s\S]*?)\$/g, (match, p1) => {
                return `<span class="katex">${katex.renderToString(p1, { throwOnError: false })}</span>`;
            });
            // }).replace(/<code>([\s\S]*?)<\/code>/g, (match, latex) => {
            //   return `<span class="katex">${katex.renderToString(latex, { displayMode: false })}</span>`;
            // });
        },
        renderMarkdown(text) {
            return marked(text);
        },
    },
}
</script>
<style></style>