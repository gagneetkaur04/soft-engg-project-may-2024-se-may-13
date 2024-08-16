<template>
  <div class="chat_icon" data-bs-toggle="modal" data-bs-target="#chatBox">
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-chat-right-fill"
      viewBox="0 0 16 16">
      <path
        d="M14 0a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2z" />
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
            <div class="container-fluid">
              <div class="row chat_background">
                <div class="col-3 col-sm-1">
                  <img src="@/assets/padhai_logo.png" class="rounded-circle" alt="logo" width="20" height="20">
                </div>
                <div class="col-4 col-sm-8">
                  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                  industry's standard dummy text ever since the 1500s.
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veritatis delectus nemo temporibus atque
                  libero omnis velit neque tempore, itaque quia quos numquam aperiam, inventore repellat aut, corporis
                  error vitae odit?
                </div>
              </div>
              <div class="row chat_background">
                <div class="col-3 col-sm-1">
                  <img src="@/assets/padhai_logo.png" class="rounded-circle" alt="logo" width="20" height="20">
                </div>
                <div class="col-4 col-sm-8">
                  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                  industry's standard dummy text ever since the 1500s.
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veritatis delectus nemo temporibus atque
                  libero omnis velit neque tempore, itaque quia quos numquam aperiam, inventore repellat aut, corporis
                  error vitae odit?
                </div>
              </div>
              <div class="row chat_user_background">
                <div class="col-md-8 ms-auto">
                  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                  industry's standard dummy text ever since the 1500s.
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veritatis delectus nemo temporibus atque
                  libero omnis velit neque tempore, itaque quia quos numquam aperiam, inventore repellat aut, corporis
                  error vitae odit?
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <form @submit.prevent="handleForm">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="Type your message here"
                  aria-label="Type your message here" aria-describedby="button-addon2" v-model="chatMsg">
                <button class="btn send_btn" type="button" id="button-addon2"
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
export default {
  name: 'ChatWindow',
  data: function () {
    return {
      toggleStatus: false,
      chatContent: null,
      chatMsg: "",
    }
  },
  methods: {
    async handleForm() {
      this.toggleStatus = !this.toggleStatus;
      let request = {
        url: __API_URL__ + "chat/start",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
          "Access-Control-Allow-Origin": "*",
        },
      };
    }
  }
}
</script>
<style>
.chat_icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  z-index: 30;
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