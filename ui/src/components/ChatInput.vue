<template>
    <q-input
      v-model="chatText"
      filled
      stack-label
      label="Message Chatter"
      >

    </q-input>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue';
import { useState } from 'src/store/main';

export default defineComponent({
  name: 'chatInput',
  setup() {
    const {
        chatText
      } = useState();

    return {
      chatText
    }
  }
});
</script>

<style scoped>

</style>