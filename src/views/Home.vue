<template>
  <v-container fluid>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs8>
          <v-card>
            <apexcharts width="100%" type="area" :options="options" :series="series" height="400px"></apexcharts>
          </v-card>
        </v-flex>
        <v-flex xs4>
          <v-card id="aud">
            <svg preserveAspectRatio="none" id="visualizer" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
              <defs>
                <mask id="mymask">
                  <g id="maskGroup">
                  </g>
                </mask>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" style="stop-color:#ff0a0a;stop-opacity:1" />
                  <stop offset="20%" style="stop-color:#f1ff0a;stop-opacity:1" />
                  <stop offset="90%" style="stop-color:#d923b9;stop-opacity:1" />
                  <stop offset="100%" style="stop-color:#050d61;stop-opacity:1" />
                </linearGradient>
              </defs>
              <rect x="0" y="0" width="100%" height="100%" fill="url(#gradient)" mask="url(#mymask)"></rect>
            </svg>
            <h1>In</h1>
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
import axios from 'axios';
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
        const res = await db
            .collection('sessions')
            .doc('1')
            .get();
        console.log(res.data());
        this.emotionBreakdown.series = res.data().chartData.emotionBreakdown.series;
        this.emotionBreakdown.labels = res.data().chartData.emotionBreakdown.labels;
    },
    mounted() {
        this.visiualizeAudio();
        this.newFirebaseSession();
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
            console.log('Image taken!' + img);
        };

        // window.setInterval(this.addData(), 1000);
    },
    methods: {
        async newFirebaseSession() {
            try {
                const response = await db
                    .collection('sessions')
                    .doc((new Date() * 1000).toString())
                    .set({ suhbruh: 'ssss' });
                console.log('fb success');
            } catch (err) {
                console.log('Error updating firebase: ', err);
            }
        },
        async callBackend() {
            const response = await axios.post('http://127.0.0.1:5000/messages');
        },
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
        visiualizeAudio() {
            var paths = document.getElementById('aud').getElementsByTagName('path');
            var visualizer = document.getElementById('visualizer');
            var mask = visualizer.getElementById('mymask');
            var h = document.getElementsByTagName('h1')[0];
            var path;
            var report = 0;
            console.log('suhhhhhhhhh', paths);
            var soundAllowed = function(stream) {
                //Audio stops listening in FF without // window.persistAudioStream = stream;
                //https://bugzilla.mozilla.org/show_bug.cgi?id=965483
                //https://support.mozilla.org/en-US/questions/984179
                window.persistAudioStream = stream;
                h.innerHTML = 'Thanks';
                h.setAttribute('style', 'opacity: 0;');
                var audioContent = new AudioContext();
                var audioStream = audioContent.createMediaStreamSource(stream);
                var analyser = audioContent.createAnalyser();
                audioStream.connect(analyser);
                analyser.fftSize = 1024;

                var frequencyArray = new Uint8Array(analyser.frequencyBinCount);
                visualizer.setAttribute('viewBox', '0 0 255 255');

                //Through the frequencyArray has a length longer than 255, there seems to be no
                //significant data after this point. Not worth visualizing.
                for (var i = 0; i < 255; i++) {
                    path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                    path.setAttribute('stroke-dasharray', '4,1');
                    mask.appendChild(path);
                }
                var doDraw = function() {
                    requestAnimationFrame(doDraw);
                    analyser.getByteFrequencyData(frequencyArray);
                    var adjustedLength;
                    for (var i = 0; i < 255; i++) {
                        adjustedLength =
                            Math.floor(frequencyArray[i]) - Math.floor(frequencyArray[i]) % 5;
                        paths[i].setAttribute('d', 'M ' + i + ',255 l 0,-' + adjustedLength);
                    }
                };
                doDraw();
            };

            var soundNotAllowed = function(error) {
                h.innerHTML = 'You must allow your microphone.';
                console.log(error);
            };

            /*window.navigator = window.navigator || {};
    /*navigator.getUserMedia =  navigator.getUserMedia       ||
                              navigator.webkitGetUserMedia ||
                              navigator.mozGetUserMedia    ||
                              null;*/
            //navigator.getUserMedia({ audio: true }, soundAllowed, soundNotAllowed);
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

#aud {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    background-color: white;
    font-size: 0;
}

svg {
    display: block;
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    position: absolute;
}

h1 {
    width: 100%;
    font-family: sans-serif;
    position: absolute;
    text-align: center;
    color: white;
    font-size: 18px;
    top: 40%;
    opacity: 1;
    transition: opacity 1s ease-in-out;
    -moz-transition: opacity 1s ease-in-out;
    -webkit-transition: opacity 1s ease-in-out;
}

h1 a {
    color: #48b1f4;
    text-decoration: none;
}

#aud path {
    stroke-linecap: square;
    stroke: white;
    stroke-width: 0.5px;
}
</style>
