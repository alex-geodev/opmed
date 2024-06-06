<template>
  <chat-bot></chat-bot>
  <div class="row full-width q-pa-md">
    <q-card flat class="col-12">
      <q-card-section>
        <file-select />
      </q-card-section>
      <q-card-section>
        <text-input />
      </q-card-section>
      <q-card-actions class="q-pa-md" align="around">
        <q-btn color="primary">Calculate</q-btn>
        <q-btn color="primary">Clear</q-btn>
      </q-card-actions>
    </q-card>
  </div>
  <div class="row full-width q-pb-md q-pl-md q-pr-md" style="min-height: 30vh">
    <q-card flat class="col-12">
      <q-card-section>
        <div class="text-bold text-center">Summary of asdfaasdf</div>
      </q-card-section>
      <q-separator />
      <q-card-section>
        <div class="row text-center">
          <div class="col-3">a</div>
          <div class="col-3">b</div>
          <div class="col-3">c</div>
          <div class="col-3">d</div>
        </div>
        <div class="row text-center">
          <div class="col-3">a</div>
          <div class="col-3">b</div>
          <div class="col-3">c</div>
          <div class="col-3">d</div>
        </div>
      </q-card-section>
    </q-card>
  </div>
  <div
    class="row full-width text-center justify-center"
    style="min-height: 30vh; max-height: 30vh"
  >
    <q-card v-ripple class="col-4 q-mr-md" style="max-width: 32%">
      <q-card-section class="text-bold"> COA 1 </q-card-section>
      <q-card-section>
        Here is an example of where we would put some of this high level
        information
      </q-card-section>
    </q-card>
    <q-card v-ripple class="col-4 q-mr-md" style="max-width: 32%">
      <q-card-section class="text-bold"> COA 2 </q-card-section>
    </q-card>
    <q-card v-ripple class="col-4" style="max-width: 32%">
      <q-card-section class="text-bold"> COA 3 </q-card-section>
    </q-card>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FileSelect from 'src/components/FileSelect.vue';
import TextInput from 'src/components/TextInput.vue';
import ChatBot from 'src/components/ChatBot.vue';
import { useState } from 'src/store/main';

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const {
      loading,
      allNineLines,
      activeNineLine,
      prompt,
      coas,
      chatResponse,
    } = useState();

    return {
      loading,
      allNineLines,
      activeNineLine,
      prompt,
      coas,
      chatResponse,
    };
  },
  components: {
    FileSelect,
    TextInput,
    ChatBot,
  },
});
</script>
