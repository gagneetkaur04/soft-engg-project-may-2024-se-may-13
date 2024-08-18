<template>
    <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4" style="height: 80vh;">
        <div class="d-flex">
            <select v-model="states.lang" disabled>
                <option v-for="lang of langs" :value="lang">{{ lang }}</option>
            </select>
            <select v-model="states.theme">
                <option v-for="theme of themes" :value="theme">{{ theme }}</option>
            </select>
            <div>
                <span class="badge" v-bind:class="{ 'bg-primary': !flag, 'bg-secondary': flag }" type="submit"
                    @click="submitCode" v-bind:disabled="flag">Submit
                    Code</span>
            </div>
        </div>
        <div class="alert alert-danger alert-dismissible fade show mt-2" role="alert" v-if="errorStatus">
            <strong>{{ errorMsg }}</strong>.
            <button type="button" class="btn-close" aria-label="Close" @click="errorStatus = false"></button>
        </div>
        <div style="height: 80vh;" class="codeEditor">
            <VAceEditor ref="aceRef" v-model:value="states.content" class="vue-ace-editor" :placeholder=placeholder
                :lang="states.lang" :theme="states.theme" :options="{
                    useWorker: true,
                    enableBasicAutocompletion: true,
                    enableSnippets: true,
                    enableLiveAutocompletion: true,
                    readOnly: flag,
                }" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { VAceEditor } from 'vue3-ace-editor';
import ace from 'ace-builds';
import 'ace-builds/src-noconflict/ext-language_tools';
import 'ace-builds/src-noconflict/mode-python';
ace.require("ace/ext/language_tools");
import themeMonokaiUrl from 'ace-builds/src-noconflict/theme-monokai';
ace.config.setModuleUrl('ace/theme/monokai', themeMonokaiUrl);
import themeGithubUrl from 'ace-builds/src-noconflict/theme-github';
ace.config.setModuleUrl('ace/theme/github', themeGithubUrl);
import themeChromeUrl from 'ace-builds/src-noconflict/theme-chrome';
import { readonly } from 'vue';
ace.config.setModuleUrl('ace/theme/chrome', themeChromeUrl);

export default {
    name: 'CodeEditor',
    components: {
        VAceEditor,
    },
    data: function () {
        return {
            states: {
                lang: 'python',
                theme: 'monokai',
                content: '',
            },
            langs: ['python'],
            themes: ['github', 'chrome', 'monokai'],
            errorMsg: null,
            errorStatus: null
        }
    },
    props: {
        flag: Boolean, // by default false
        placeholder: String, // by default 'Enter your code here',
    },
    created() {
        this.states.content = this.placeholder;
    },
    methods: {
        async submitCode() {
            let request = {
                url: __API_URL__ + "programming_assignments" + `/${this.$route.query.progAssignmentId}` + "/submit",
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                    "Access-Control-Allow-Origin": "*",
                },
                data: {
                    code: this.states.content,
                },
            };
            await axios(request).then((response) => {
                location.reload();
            }).catch((error) => {
                const replacedMessage = error.response.data.message.replace(
                    /File.*main.py", /,
                    ''
                );
                this.errorMsg = replacedMessage;
                this.errorStatus = true;
            });
        }
    }
};


</script>

<style lang="scss" scoped>
header {
    display: flex;
}

select {
    margin-right: 15px;
    position: relative;
}

.codeEditor {
    flex: 1;
    margin-top: 15px;
    display: flex;
    position: relative;
}

.vue-ace-editor {
    font-size: 16px;
    border: 1px solid;
    flex: 1;
}
</style>