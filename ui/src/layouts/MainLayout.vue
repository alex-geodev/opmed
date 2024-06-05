<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>

        <q-toolbar-title>
          <q-avatar class="q-ma-sm">
            <img src="../assets/mc.svg">
          </q-avatar>
          <span class="text-bold">Stitched Up</span>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>


    <q-page-container>
      <q-page class="q-pa-md">
        <router-view />
      </q-page>
    </q-page-container>


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
