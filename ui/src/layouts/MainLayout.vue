<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>

        <q-toolbar-title>
          <span>OP Med Tool</span>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>


    <q-page-container>
      <q-page class="column justify-start">
        <router-view />
      </q-page>
    </q-page-container>

    <q-footer bordered class="bg-primary text-white">
      <div class="row no-wrap shadow-1">
      <q-toolbar class="col-11">
        <q-btn flat round dense icon="copyright" />
          <div>2022 License Here</div>
      </q-toolbar>
      </div>
    </q-footer>

  </q-layout>
</template>

<script>

export default {
  setup () {
    console.log("fill");
  },
  components: {
  }
}
</script>

<style>
</style>
