<template>
    <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-2" style="height: 80vh;">
        <select v-model="states.lang" disabled>
            <option v-for="lang of langs" :value="lang">{{ lang }}</option>
        </select>
        <select v-model="states.theme">
            <option v-for="theme of themes" :value="theme">{{ theme }}</option>
        </select>
        <div>
            <span class="badge bg-primary" type="submit" @click="submitCode">Send</span>
        </div>
        <div style="height: 60vh;" class="codeEditor">
            <VAceEditor ref="aceRef" v-model:value="states.content" class="vue-ace-editor"
                :placeholder="`Enter your ${states.lang} code here`" :lang="states.lang" :theme="states.theme" :options="{
                    useWorker: true,
                    enableBasicAutocompletion: true,
                    enableSnippets: true,
                    enableLiveAutocompletion: true,
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
        }
    },
    methods: {
        async submitCode() {
            console.log("hello")
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
                console.log(response);
            }).catch((error) => {
                console.log(error);
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