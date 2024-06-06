<template>
  <button v-if="!isVisible" class="open-chatbot" @click="toggleChatbot">Chat with us!</button>

  <div class="chatbot-container" v-if="isVisible">
    <div class="chatbot-header">
      <span>ChatBot</span>
      <button @click="toggleChatbot">X</button>
    </div>
    <div class="chatbot-messages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <div class="user" v-if="message.user">{{ message.text }}</div>
        <div class="bot" v-else>{{ message.text }}</div>
      </div>
    </div>
    <div class="chatbot-input">
      <input
        type="text"
        v-model="userMessage"
        @keyup.enter="sendMessage"
        placeholder="Type a message..."
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isVisible: false,
      userMessage: '',
      messages: [{ user: false, text: 'Hello! How can I help you?' }],
    };
  },
  methods: {
    toggleChatbot() {
      this.isVisible = !this.isVisible;
    },
    sendMessage() {
      if (this.userMessage.trim() !== '') {
        this.messages.push({ user: true, text: this.userMessage });
        this.userMessage = '';
        // Simulate bot response
        setTimeout(() => {
          this.messages.push({ user: false, text: 'I am here to help!' });
        }, 1000);
      }
    },
  },
};
</script>

<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  height: 400px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 999;
}
.chatbot-header {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
.chatbot-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}
.message {
  margin: 5px 0;
}
.user {
  text-align: right;
  color: blue;
}
.bot {
  text-align: left;
  color: green;
}
.chatbot-input {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
}
.chatbot-input input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.chatbot-input button {
  margin-left: 10px;
  padding: 5px 10px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.open-chatbot {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  z-index: 999;
}
</style>
