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
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat :color='sessionColor' @click="toggleSession">{{action}} Session {{$store.state.timeElapsed}}</v-btn>
        <v-btn flat>Logout</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
      <router-view />
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
            return this.weekdays[d.getDay()];
        },
        toggleSession() {
            if (!this.inSession) {
                this.$store.state.inSession = true;
                this.sessionColor = 'error';
                this.timer();
                this.action = 'Stop';
                this.inSession = true;
            } else {
                clearTimeout(this.t);
                clearInterval(this.$store.state.autoTimerId);
                this.inSession = false;
                this.$store.state.inSession = false;
                this.seconds = 0;
                this.minutes = 0;
                this.hours = 0;
                this.sessionColor = 'success';
                this.$store.state.timeElapsed = '';
                this.action = 'Start';
            }
        },
        add() {
            this.seconds++;
            if (this.seconds >= 60) {
                this.seconds = 0;
                this.minutes++;
                if (this.minutes >= 60) {
                    this.minutes = 0;
                    this.hours++;
                }
            }
            this.$store.state.timeElapsed =
                (this.hours ? (this.hours > 9 ? this.hours : '0' + this.hours) : '00') +
                ':' +
                (this.minutes ? (this.minutes > 9 ? this.minutes : '0' + this.minutes) : '00') +
                ':' +
                (this.seconds > 9 ? this.seconds : '0' + this.seconds);

            this.timer();
        },
        timer() {
            this.t = setTimeout(this.add, 1000);
        },
    },
    data() {
        return {
            t: null,
            action: 'Start',
            seconds: 0,
            minutes: 0,
            hours: 0,
            sessionColor: 'success',
            inSession: false,
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
