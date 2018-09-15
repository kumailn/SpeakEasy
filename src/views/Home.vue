<template>
  <v-container fluid>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <v-card>
            <apexcharts width="100%" type="area" :options="options" :series="series" height="400px"></apexcharts>
          </v-card>
        </v-flex>
        <v-flex xs4>
          <v-card dark color="secondary">
            <div id="container">
              <video autoplay="true" id="videoElement" style="width: 100%; height: 100%;" />
            </div>
            <button id="screenshotButton"> Take a Screenshot </button>
            </br>
            <button id="recordButton"> Record </button>
          </v-card>
        </v-flex>
        <v-flex xs4>
          <v-card>
            <v-card-text class="px-0">
              <apexcharts width="100%" type="radialBar" :options="emotionBreakdown" :series="emotionBreakdown.series" height="390px" />
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex xs4>
          <v-card>
            <v-card-text class="px-0">
              <apexcharts width="100%" type="line" :options="futureChart" :series="futureChart.series" height="390px" />
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 4 " :key="`3${i}` " xs3>
          <v-card dark color="secondary ">
            <v-card-text class="px-0 ">3</v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 6 " :key="`2${i}` " xs2>
          <v-card dark color="primary ">
            <v-card-text class="px-0 ">2</v-card-text>
          </v-card>
        </v-flex>
        <v-flex v-for="i in 12 " :key="`1${i}` " xs1>
          <v-card dark color="secondary ">
            <v-card-text class="px-0 ">1</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <v-slide-y-transition mode="out-in ">

    </v-slide-y-transition>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import VueApexCharts from 'vue-apexcharts';
import db from '../private';
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
                series: [],
                labels: [],
            },
            futureChart: {
                chart: {
                    height: 380,
                    type: 'line',
                },
                series: [
                    {
                        name: 'Website Blog',
                        type: 'column',
                        data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160],
                    },
                    {
                        name: 'Social Media',
                        type: 'line',
                        data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16],
                    },
                ],
                stroke: {
                    width: [0, 4],
                },
                title: {
                    text: 'Traffic Sources',
                },
                // labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                labels: [
                    '01 Jan 2001',
                    '02 Jan 2001',
                    '03 Jan 2001',
                    '04 Jan 2001',
                    '05 Jan 2001',
                    '06 Jan 2001',
                    '07 Jan 2001',
                    '08 Jan 2001',
                    '09 Jan 2001',
                    '10 Jan 2001',
                    '11 Jan 2001',
                    '12 Jan 2001',
                ],
                xaxis: {
                    type: 'datetime',
                },
                yaxis: [
                    {
                        title: {
                            text: 'Website Blog',
                        },
                    },
                    {
                        opposite: true,
                        title: {
                            text: 'Social Media',
                        },
                    },
                ],
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
    async beforeMount() {
        let res = await db
            .collection('sessions')
            .doc('1')
            .get();
        console.log(res.data());
        this.emotionBreakdown.series = res.data().chartData.emotionBreakdown.series;
        this.emotionBreakdown.labels = res.data().chartData.emotionBreakdown.labels;
    },
    mounted() {
        const video = document.querySelector('#videoElement');
        
        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices
                .getUserMedia({ video: true })
                .then(stream => {
                    video.srcObject = stream;
                })
                .catch(err0r => {
                    console.log('Something went wrong!');
                });
        }


        const canvas = document.createElement('canvas');
        const screenshotButton = document.querySelector('#screenshotButton');

        screenshotButton.onclick = video.onclick = function() {
        canvas.width = video.videoWidth;
         canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        // Other browsers will fall back to image/png
        var img = canvas.toDataURL('image/png');
        console.log("Image taken!" + img)
        };

        // window.setInterval(this.addData(), 1000);
    },
    methods: {
        addData() {
            this.options.xaxis.categories.push(Math.floor(Math.random() * 100));
            this.series[0].data.push(Math.floor(Math.random() * 100));

            this.series[0].data.shift();
            this.options.xaxis.categories.shift();
        },
        updateEmotionBreakdown() {
            const n = [];
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
