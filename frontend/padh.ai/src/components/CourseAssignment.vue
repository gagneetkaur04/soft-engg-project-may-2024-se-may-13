<template>
    <NavBar></NavBar>
    <div class="container-fluid">
        <div class="row">
            <SideNavBar :coursePage=true ref="sideNav"></SideNavBar>
            <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4 d-flex">
                <h1 class="mx-auto"> Assigment - {{ weekNumber }}</h1>
            </div>
            <div v-if="submittedFlag">
                <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
                    <h3>Assignment Score: {{ assignmentGrade }}</h3>
                </div>
            </div>
            <form @submit.prevent="submitQuiz" class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
                <div class="mt-4" v-for="(question, index) in assignmentQuestions" :key="index">
                    <h5>{{ index + 1 }}. {{ question.question_text }}</h5>
                    <div v-for="(option, i) in ['option_a', 'option_b', 'option_c', 'option_d']" :key="i">
                        <label>
                            <input type="radio" :name="'question' + index" :value="option.slice(-1)"
                                v-model="submittedAnswers[question.question_id]" required />
                            {{ question[option] }}
                        </label>
                    </div>
                </div>
                <button class="btn btn-primary mt-4" type="submit" v-bind:disabled="submittedFlag">Submit
                    Assignment</button>
            </form>
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
    name: 'CourseAssignment',
    components: {
        NavBar,
        SideNavBar,
        ChatWindow,
    },
    data() {
        return {
            assignmentQuestions: null,
            assignmentGrade: null,
            weekNumber: this.$route.query.weekNumber,
            assignmentId: this.$route.query.assignmentId,
            courseId: this.uppercase(this.$route.params.courseId),
            submittedAnswers: {},
            submittedFlag: false,
        }
    },
    async beforeMount() {
        let request = {
            url: __API_URL__ + "assignments/course" + `/${this.courseId}` + "/week" + `/${this.weekNumber}`,
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
        };
        let response = await axios(request).catch((error) => {
            if (error.response.status === 401) {
                if (error.response.data.msg === "Token has expired") {
                    localStorage.removeItem('Auth-Token');
                    this.$router.push('/login');
                }
            };
            if (error.response.status === 404) {
                alert("No assignments found for this week, Redirecting back to course page.");
                this.$router.push(`/course/${this.courseId}`);
            }
        });
        if (response.status == 200) {
            this.assignmentQuestions = response.data[0].questions;
            if (response.data[0].assignment_id != this.assignmentId) {
                alert("Assignment not found, Redirecting back to course page.");
                this.$router.push(`/course/${this.courseId}`);
            }
        }

        let request_2 = {
            url: __API_URL__ + "assignments/grade" + `/${this.assignmentId}`,
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
        }

        let response_2 = await axios(request_2).catch((error) => {
            if (error.response.status === 401) {
                console.log(error.response.data.msg);
                if (error.response.data.msg === "Token has expired") {
                    localStorage.removeItem('Auth-Token');
                    this.$router.push('/login');
                }
            };
        });
        if (response_2.status == 200) {
            this.assignmentGrade = response_2.data.score;
        }

        let request_3 = {
            url: __API_URL__ + "assignments/submission" + `/${this.assignmentId}`,
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                "Access-Control-Allow-Origin": "*",
            },
        }

        let response_3 = await axios(request_3).catch((error) => {
            if (error.response.status === 401) {
                console.log(error.response.data.msg);
                if (error.response.data.msg === "Token has expired") {
                    localStorage.removeItem('Auth-Token');
                    this.$router.push('/login');
                }
            }
        });
        if (response_3.status == 200) {
            for (let i = 0; i < response_3.data.length; i++) {
                this.submittedAnswers[response_3.data[i].question_id] = response_3.data[i].chosen_answer;
            }
            this.submittedFlag = true;
        }
    },
    methods: {
        uppercase: function (str) {
            return str.toUpperCase();
        },
        submitQuiz() {
            let payload = {
                "assignment_id": this.assignmentId,
                "answers": this.submittedAnswers,
            }
            let request = {
                url: __API_URL__ + "assignments/submit",
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                    "Access-Control-Allow-Origin": "*",
                },
                data: JSON.stringify(payload),
            };
            axios(request).then((response) => {
                alert("Assignment submitted successfully");
                location.reload();
            }).catch((error) => {
                if (error.response.status === 401) {
                    console.log(error.response.data.msg);
                    if (error.response.data.msg === "Token has expired") {
                        localStorage.removeItem('Auth-Token');
                        this.$router.push('/login');
                    }
                };
            });
        }
    },
}
</script>
<style></style>