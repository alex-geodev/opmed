<template>
<q-layout class="flex">
	<div class="row full-width">
    <q-card class="col-12">
      <q-card-section>
        <file-select />
      </q-card-section>
      <q-card-section>
        <text-input />
      </q-card-section>
      <q-card-actions align="around">
        <q-btn color="primary">Calculate</q-btn>
        <q-btn color="primary">Clear</q-btn>
      </q-card-actions>
    </q-card>
	</div>
  <div class="row full-width">
    <q-card class="col-12">
      <q-card-section>
        <div class="text-bold text-center">
          Summary of asdfaasdf
        </div>
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
  <div class="row full-width text-center">
    <q-card v-ripple class="col-4">
      <q-card-section class="text-bold">
        Course of Action 1
      </q-card-section>
    </q-card>
    <q-card v-ripple class="col-4">
      <q-card-section class="text-bold">
        Course of Action 2
      </q-card-section>
    </q-card>
    <q-card v-ripple class="col-4">
      <q-card-section class="text-bold">
        Course of Action 3
      </q-card-section>
    </q-card>
  </div>
</q-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FileSelect from 'src/components/FileSelect.vue';
import TextInput from 'src/components/TextInput.vue';

export default defineComponent({
  name: 'IndexPage',
  components: {
    FileSelect,
    TextInput
  }
});
</script>
