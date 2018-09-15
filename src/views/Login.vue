<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 class="text-xs-center" mt-5>
        <h1>Welcome to HTN2018</h1>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 mt-3>
        <blockquote class="blockquote text-xs-center">
          An online feedback platform designed <br>
           to perfect your presentation skills
        </blockquote>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 class="text-xs-center" mt-5>
        <v-btn color="primary" to="/"> Live Feedback</v-btn>
        <v-btn to="/history"> History </v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {}
</script>