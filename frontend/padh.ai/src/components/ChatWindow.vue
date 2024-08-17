<template>
  <div class="chat_icon" data-bs-toggle="modal" data-bs-target="#chatBox">
    <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chat-right-fill"
      viewBox="0 0 16 16">
      <path
        d="M14 0a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2z" />
      <title>AI Assistant</title>
    </svg>
  </div>
  <div>
    <div class="modal fade" id="chatBox" tabindex="-1" aria-labelledby="chatBoxLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="chatBoxLabel">AI Assistant</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="container-fluid" v-for="value in chatContents">
              <div class="row chat_background" v-if=!checkSender(Object.keys(value)[0])>
                <div class="col-3 col-sm-1">
                  <img src="@/assets/padhai_logo.png" class="rounded-circle" alt="logo" width="20" height="20">
                </div>
                <div class="col-4 col-sm-8" v-html="renderMarkdown(renderKatex(value.ai_message))">
                </div>
              </div>
              <div class="row chat_user_background" v-if=checkSender(Object.keys(value)[0])>
                <div class="col-md-8 ms-auto">
                  {{ value.user }}
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <form @submit.prevent="handleForm">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="Type your message here"
                  aria-label="Type your message here" aria-describedby="button-addon2" v-model="chatMsg"
                  v-bind:disabled="toggleStatus" id="chatInput">
                <button class="btn send_btn" type="submit" id="button-addon2"
                  v-bind:disabled="toggleStatus">Send</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { marked } from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';
export default {
  name: 'ChatWindow',
  data: function () {
    return {
      toggleStatus: false,
      chatContents: null,
      chatMsg: "",
      conversationId: null,
    }
  },
  methods: {
    async handleForm() {
      this.toggleStatus = !this.toggleStatus;
      if (this.conversationId == null) {
        let request = {
          url: __API_URL__ + "chat/start",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
            "Access-Control-Allow-Origin": "*",
          },
          data: JSON.stringify({ "message": this.chatMsg }),
        };
        this.chatContents = [{ "user": this.chatMsg }];
        this.chatMsg = "";
        await axios(request).then((response) => {
          this.conversationId = response.data.conversation.conversation_id;
          this.chatContents.push({ "ai_message": response.data.ai_message.message_text });
          this.toggleStatus = !this.toggleStatus;
        }).catch((error) => {
          console.log(error);
        });
      }
      else {
        let request = {
          url: __API_URL__ + "chat/continue/" + `${this.conversationId}`,
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
            "Access-Control-Allow-Origin": "*",
          },
          data: JSON.stringify({ "message": this.chatMsg }),
        };
        this.chatContents.push({ "user": this.chatMsg });
        this.chatMsg = "";
        await axios(request).then((response) => {
          this.chatContents.push({ "ai_message": response.data.ai_message.message_text });
          this.toggleStatus = !this.toggleStatus;
        }).catch((error) => {
          console.log(error);
        });
      }
    },
    checkSender(key) {
      if (key === 'user') {
        return true;
      }
      else {
        return false;
      }
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
<style>
.chat_icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  z-index: 30;
  color: var(--dark-green);
}

#chatBox modal {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  z-index: 32;
}

.chat_background {
  background-color: var(--light-green);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: left;
}

.chat_user_background {
  background-color: var(--candice);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: right;
}

.form-control:focus {
  border-color: var(--light-green) !important;
  box-shadow: 0 0 0 0.25rem var(--light-green) !important;
}

.send_btn {
  background-color: var(--light-green);
  color: white;
  border-radius: 10px;
  border: none;
  padding: 10px;
  margin-left: 10px;
  color: black;
}

.send_btn:hover {
  background-color: var(--dark-green);
  color: white;
}
</style>