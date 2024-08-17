<template>
    <NavBar></NavBar>
    <div class="container-fluid">
        <div class="row">
            <SideNavBar :coursePage=true ref="sideNav"></SideNavBar>
            <div v-if="assignmentInfoFlag">
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4" v-if="assignmentInfo">
                    <div class="d-flex">
                        <h1 class="mx-auto"> {{ assignmentInfo.title }}</h1>
                    </div>
                    <div v-html="renderMarkdown(renderKatex(assignmentInfo.description))" class="pt-4">
                    </div>
                </div>
            </div>
            <div v-if="assignmentGrade">
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
                    <div class="d-flex">
                        <h5> You've submitted this assignment, your score is {{ assignmentGrade }}</h5>
                    </div>
                </div>
            </div>
            <CodeEditor :flag="flag" :placeholder="placeholder" v-if="loadCodeEditor"></CodeEditor>
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
            assignmentInfo: null,
            assignmentInfoFlag: true,
            courseId: this.uppercase(this.$route.params.courseId),
            assignmentGrade: null,
            placeholder: "Enter your python code here",
            flag: false,
            grade: null,
            loadCodeEditor: false,
        }
    },
    async beforeMount() {
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
        await axios(request)
            .then((response) => {
                this.assignmentInfo = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
        let request_2 = {
            url: __API_URL__ + "programming_assignments" + '/grades',
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
        }
        await axios(request_2)
            .then((response) => {
                this.grade = response.data;
                if (this.grade.length > 0) {
                    for (let i = 0; i < this.grade.length; i++) {
                        if (this.grade[i].prog_assignment_id == this.$route.query.progAssignmentId) {
                            this.assignmentGrade = this.grade[i].score;
                            this.flag = true;
                            this.placeholder = this.grade[i].code;
                        }
                    }
                }
                this.loadCodeEditor = true;
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