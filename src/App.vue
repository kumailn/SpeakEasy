<template>
  <v-app>
    <v-navigation-drawer persistent :mini-variant="miniVariant" :clipped="clipped" v-model="drawer" enable-resize-watcher fixed app>
      <v-list>
        <v-list-tile @click="console.log('suh')">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="console.log('suh')">
          <v-list-tile-action>
            <v-icon>history</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>History</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-group prepend-icon="replay" value="true">
          <v-list-tile slot="activator">
            <v-list-tile-title>Recent Sessions</v-list-tile-title>
          </v-list-tile>

          <v-list-group sub-group no-action v-for="(day, dkey) in days" :key="dkey">
            <v-list-tile slot="activator">
              <v-list-tile-title>{{getPrevDay(day)}}</v-list-tile-title>
            </v-list-tile>
            <v-list-tile v-for="(crud, i) in previousSessions" :key="i" @click="">
              <v-list-tile-title v-text="crud"></v-list-tile-title>
              <v-list-tile-action>
                <v-icon></v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list-group>
        </v-list-group>

      </v-list>
    </v-navigation-drawer>
    <v-toolbar app :clipped-left="clipped">
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <!-- <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
      </v-btn> -->
      <!-- <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>web</v-icon>
      </v-btn> -->
      <!-- <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>remove</v-icon>
      </v-btn> -->
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>menu</v-icon>
      </v-btn> -->
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <v-navigation-drawer temporary :right="right" v-model="rightDrawer" fixed app>
      <v-list>
        <v-list-tile @click="right = !right">
          <v-list-tile-action>
            <v-icon>compare_arrows</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Switch drawer (click me)</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  methods: {
    getPrevDay(num) {
      if (num === 0) return 'Yesterday';
      const d = new Date();
      d.setDate(d.getDate() - num);
      console.log(num, d.getDay());
      return this.weekdays[d.getDay()];
    },
  },
  data() {
    return {
      weekdays: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
      ],
      days: [0, 1, 2, 3, 4, 5],
      previousSessions: ['1:20pm', '2:30pm', '7:15pm'],
      cruds: [
        ['Create', 'add'],
        ['Read', 'insert_drive_file'],
        ['Update', 'update'],
        ['Delete', 'delete'],
      ],
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'bubble_chart',
          title: 'Inspire',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'HTN 2018',
    };
  },
};
</script>
