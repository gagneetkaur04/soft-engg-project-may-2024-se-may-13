<template>
    <div class="key_points" @click="sendData">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-stars"
            viewBox="0 0 16 16">
            <path
                d="M7.657 6.247c.11-.33.576-.33.686 0l.645 1.937a2.89 2.89 0 0 0 1.829 1.828l1.936.645c.33.11.33.576 0 .686l-1.937.645a2.89 2.89 0 0 0-1.828 1.829l-.645 1.936a.361.361 0 0 1-.686 0l-.645-1.937a2.89 2.89 0 0 0-1.828-1.828l-1.937-.645a.361.361 0 0 1 0-.686l1.937-.645a2.89 2.89 0 0 0 1.828-1.828zM3.794 1.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387A1.73 1.73 0 0 0 4.593 5.69l-.387 1.162a.217.217 0 0 1-.412 0L3.407 5.69A1.73 1.73 0 0 0 2.31 4.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387A1.73 1.73 0 0 0 3.407 2.31zM10.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.16 1.16 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.16 1.16 0 0 0-.732-.732L9.1 2.137a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732z" />
            <title>lecture keypoints</title>
        </svg>
    </div>
</template>
<script>
import axios from 'axios';
import { marked } from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';
export default {
    name: 'keyPoints',
    data: function () {
        return {
            keyPoints: "",
        }
    },
    methods: {
        renderKatex(text) {
            return text.replace(/\$\$([\s\S]*?)\$\$/g, (match, p1) => {
                return `<span class="katex">${katex.renderToString(p1, { throwOnError: false })}</span>`;
            }).replace(/\$([\s\S]*?)\$/g, (match, p1) => {
                return `<span class="katex">${katex.renderToString(p1, { throwOnError: false })}</span>`;
            });
        },
        renderMarkdown(text) {
            return marked(text);
        },
        async sendData() {
            let request = {
                url: __API_URL__ + "summary" + `/${this.$route.query.contentId}`,
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                    "Access-Control-Allow-Origin": "*",
                },
            };
            await axios(request).then((response) => {
                this.keyPoints = this.renderMarkdown(this.renderKatex(response.data.summary));
            }).catch((error) => {
                console.log(error);
            });
            this.$emit('child-data', this.keyPoints);
        },
    },
}
</script>
<style>
.key_points {
    position: fixed;
    bottom: 140px;
    right: 30px;
    cursor: pointer;
    z-index: 30;
    color: var(--dark-green);
}
</style>