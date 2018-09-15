<template>
  <v-container fluid>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <v-card>
            <apexcharts width="100%" type="area" :options="options" :series="series" height="400px"></apexcharts>
          </v-card>
        </v-flex>
        <v-flex xs6>
          <v-card dark color="secondary">
            <div id="container">
              <video autoplay="true" id="videoElement" style="width:100%; height: 100%" />
            </div>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 3" :key="`4${i}`" xs4>
          <v-card dark color="primary">
            <v-card-text class="px-0">
              <apexcharts width="100%" type="radialBar" :options="emotionBreakdown" :series="emotionBreakdown.series" height="400px"></apexcharts>
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 4" :key="`3${i}`" xs3>
          <v-card dark color="secondary">
            <v-card-text class="px-0">3</v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 6" :key="`2${i}`" xs2>
          <v-card dark color="primary">
            <v-card-text class="px-0">2</v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 12" :key="`1${i}`" xs1>
          <v-card dark color="secondary">
            <v-card-text class="px-0">1</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-layout align-center justify-space-around row fill-height>
      <apexcharts width="1000px" type="line" :options="options" :series="series" height="400px"></apexcharts>
      <apexcharts width="600px" type="line" :options="options" :series="series" height="400px"></apexcharts>
    </v-layout>
    <v-layout align-center justify-space-around row fill-height>
      <v-btn @click="addData">add data</v-btn>
      <apexcharts width="300px" type="radialBar" :options="options" :series="series" height="400px"></apexcharts>
    </v-layout>

    <v-slide-y-transition mode="out-in">

    </v-slide-y-transition>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import VueApexCharts from 'vue-apexcharts';

export default {
    components: {
        apexcharts: VueApexCharts,
    },
    data() {
        return {
            emotionBreakdown: {
                chart: {
                    height: 380,
                    type: 'radialBar',
                    animations: {
                        enabled: true,
                        easing: 'easeinout',
                        speed: 800,
                        animateGradually: {
                            enabled: true,
                            delay: 300,
                        },
                        dynamicAnimation: {
                            enabled: false,
                            speed: 500,
                        },
                    },
                },
                plotOptions: {
                    circle: {
                        dataLabels: {
                            showOn: 'hover',
                        },
                    },
                },
                series: [44, 55, 67, 83],
                labels: ['Apples', 'Oranges', 'Bananas', 'Berries'],
            },
            options: {
                chart: {
                    id: 'vuechart-example',
                },
                xaxis: {
                    categories: [
                        1991,
                        1992,
                        1993,
                        1994,
                        1995,
                        1996,
                        1997,
                        1998,
                        423,
                        543,
                        653,
                        6543,
                        645,
                        234,
                    ],
                },
            },
            series: [
                {
                    name: 'series-1',
                    data: [30, 40, 45, 50, 49, 60, 70, 91, 34, 53, 54, 77, 33, 11, 88, 66],
                },
            ],
        };
    },
    mounted() {
        var video = document.querySelector('#videoElement');

        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices
                .getUserMedia({ video: true })
                .then(function(stream) {
                    video.srcObject = stream;
                })
                .catch(function(err0r) {
                    console.log('Something went wrong!');
                });
        }
        //window.setInterval(this.addData(), 1000);
    },
    methods: {
        addData() {
            this.options.xaxis.categories.push(Math.floor(Math.random() * 100));
            this.series[0].data.push(Math.floor(Math.random() * 100));

            this.series[0].data.shift();
            this.options.xaxis.categories.shift();
        },
        updateEmotionBreakdown() {
            let n = [];
            for (let i = 0; i < 4; i++) {
                n.push(Math.floor(Math.random() * 100));
            }
            this.emotionBreakdown.series = n;
        },
    },
};
</script>

<style scoped>
h1,
h2 {
    font-weight: normal;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
