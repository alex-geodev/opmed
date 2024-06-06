<template>
  <chat-bot></chat-bot>
  <div class="row full-width q-pa-md">
    <q-card flat class="col-12">
      <q-card-section>
        <file-select />
      </q-card-section>
      <q-card-section>
        <div class="row q-gutter-md justify-center">
          <chat-input class="col-5"/>
          <radio-input class="col-5"/>
        </div>
      </q-card-section>
      <q-card-actions class="q-pa-md" align="around">
        <q-btn color="primary" :loading="loadingStatus" :disable="activeNineLine === undefined" @click="getCOAS(activeNineLine.id, chatText, radioText)">Calculate</q-btn>
        <q-btn color="primary" @click="activeNineLine=undefined; chatText=''; radioText=''; coas=[]">Clear</q-btn>
      </q-card-actions>
    </q-card>
  </div>
  <div class="row full-width q-pb-md q-pl-md q-pr-md" style="min-height: 30vh">
    <q-card flat class="col-12" v-if="activeNineLine !== undefined">
      <q-separator />
      <q-card-section>
        <div class="text-bold text-h5 text-center">Summary of {{ activeNineLine.id }}</div>
      </q-card-section>
      <q-separator />
      <q-card-section class="row text-center q-ma-xs">
        <div class="text-h6"> {{ activeNineLine.audio_transcription }}</div>
      </q-card-section>
      <q-card-section class="row text-center q-ma-xs">
        <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="priority_high" size="md" color="primary"></q-icon>
              Priority
            </div>
            <div class="text-h5 text-bold">
              {{ activeNineLine.priority }}
            </div>
        </div>
        <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="public" size="md" color="primary"></q-icon>
              MGRS
            </div>
            <div class="text-h6">
              {{ activeNineLine.mgrs }}
            </div>
        </div>
        <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="summarize" size="md" color="primary"></q-icon>
              Site Security Report
            </div>
            <div class="text-h6">
              {{ activeNineLine.site_security }}
            </div>
        </div>
      </q-card-section>
      <q-card-section>
        <div class="row text-center">
          <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="public" size="md" color="primary"></q-icon>
              Equipment Needed
            </div>
            <div class="text-h6">
              {{ activeNineLine.equipment }}
            </div>
          </div>
          <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="coronavirus" size="md" color="primary"></q-icon>
              Contamination
            </div>
            <div class="text-h6">
              {{ activeNineLine.cbrn }}
            </div>
          </div>
          <div class="col-4">
            <div class="text-h6 text-bold q-ma-sm">
              <q-icon name="crop_square" size="md" color="primary"></q-icon>
              Landing Signal
            </div>
            <div class="text-h6">
              {{ activeNineLine.pickup_mark }}
            </div>
        </div>
        </div>
      </q-card-section>
    </q-card>
  </div>
  <div
    class="row full-width text-center justify-center"
    style="min-height: 30vh; max-height: 30vh" v-if="coas.length > 0"
  >
    <q-card v-ripple class="q-ma-sm" style="max-width: 32% ; min-width: 32%" v-for="c in coas" :key="c.km" @click="getCOATable(c)">
      <q-card-section :key="c.km" class="text-bold text-h5">Distance: {{ c.km }}</q-card-section>
      <q-card-section class="text-bold text-h5">Score: {{ c.score }}</q-card-section>
    </q-card>
  </div>
  <coa-dialog />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FileSelect from 'src/components/FileSelect.vue';
import ChatInput from 'src/components/ChatInput.vue';
import RadioInput from 'src/components/RadioInput.vue';
import CoaDialog from 'src/components/COADialog.vue';
import ChatBot from 'src/components/ChatBot.vue';
import { getCOATable, useState } from 'src/store/main';

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const {
      loadingStatus,
      chatText,
      radioText,
      allNineLines,
      activeNineLine,
      activeCOA,
      coaDialog,
      coas,
      getCOAS,
      getCOATable
    } = useState();

    return {
      loadingStatus,
      chatText,
      radioText,
      allNineLines,
      activeNineLine,
      activeCOA,
      coaDialog,
      coas,
      getCOAS,
      getCOATable
    };
  },
  components: {
    FileSelect,
    ChatInput,
    RadioInput,
    ChatBot,
    CoaDialog
  },
});
</script>
