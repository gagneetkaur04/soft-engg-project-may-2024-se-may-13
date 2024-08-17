<template>
    <div class="notes" data-bs-toggle="modal" data-bs-target="#notesBox">
        <svg xmlns="http://www.w3.org/2000/svg" width="32 " height="32" fill="currentColor" class="bi bi-journal-check"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
                d="M10.854 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 8.793l2.646-2.647a.5.5 0 0 1 .708 0" />
            <path
                d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-1h1v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1H1V2a2 2 0 0 1 2-2" />
            <path
                d="M1 5v-.5a.5.5 0 0 1 1 0V5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1zm0 3v-.5a.5.5 0 0 1 1 0V8h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1zm0 3v-.5a.5.5 0 0 1 1 0v.5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1z" />
            <title>
                Add Notes
            </title>
        </svg>
    </div>
    <div>
        <div class="modal fade" id="notesBox" tabindex="-1" aria-labelledby="notesBoxLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="notesBoxLabel">Add Notes</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-footer">
                        <form @submit.prevent="handleForm">
                            <div class="input-group">
                                <textarea type="text" class="form-control" placeholder="Type your message here"
                                    aria-label="Type your message here" aria-describedby="button-addon2"
                                    v-model="noteContent" v-bind:disabled="toggleStatus" id="chatInput"> </textarea>
                                <button class="btn send_btn" type="submit" id="button-addon2"
                                    v-bind:disabled="toggleStatus"> &#11157; </button>
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
export default {
    name: 'Notes',
    data: function () {
        return {
            toggleStatus: false,
            noteContent: "",
        }
    },
    methods: {
        async handleForm() {
            this.toggleStatus = !this.toggleStatus;
            if (this.conversationId == null) {
                let request = {
                    url: __API_URL__ + "notes/",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${localStorage.getItem('Auth-Token')}`,
                        "Access-Control-Allow-Origin": "*",
                    },
                    data: JSON.stringify({ "note_content": this.noteContent }),
                };
                await axios(request).then(() => {
                    alert("Note added successfully");
                    location.reload();
                }).catch((error) => {
                    console.log(error);
                });
            }
        },
    },
}
</script>
<style>
.notes {
    position: fixed;
    bottom: 80px;
    right: 30px;
    cursor: pointer;
    z-index: 30;
    color: var(--dark-green);
}

#notesBox modal {
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