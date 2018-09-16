<template>
  <div style="background-image: linear-gradient(#c6ffdd, #fbd786, #f7797d);">
    <v-container fluid>
      <v-container grid-list-md text-xs-center>
        <v-layout row wrap>
          <v-flex xs8>
            <v-card>
              <apexcharts width="100%" type="area" :options="options" :series="series" height="400px"></apexcharts>
            </v-card>
          </v-flex>
          <v-flex xs4>
            <v-card id="aud" style="height: 100%;">
              <div>
                <h2 style="padding-bottom: 5%; font-weight: bold;">Audience Statistics</h2>
                <h3>Total People:
                </h3>
                <IOdometer class="iOdometer" :value="totalNumPeople" />
                <br/>
                <br/>
                <h3>Total % Smiling:</h3>
                <IOdometer class="iOdometer" :value="smiles" />
                <br/>
                <br/>
                <h3>Average Estimated Age:</h3>
                <IOdometer class="iOdometer" :value="avgAge" />
                <br/>
                <h3>% Male:</h3>
                <IOdometer class="iOdometer" :value="numMales" />
                <br/>
                <h3>% Female:</h3>
                <IOdometer class="iOdometer" :value="numMales" />

              </div>
            </v-card>
          </v-flex>
          <v-flex xs4>
            <v-card dark color="secondary">
              <div id="container">
                <video autoplay="true" id="videoElement" style="width: 100%; height: 100%;" />
              </div>
              <button id="screenshotButton"> Take a Screenshot </button>
              <br>
              <button id="recordButton" @click="startRec1"> Record </button> <br>
              <button id="stopButton" @click="stopR"> Stop </button>
            </v-card>
          </v-flex>
          <v-flex xs4>
            <v-card>
              <v-card-text class="px-0">
                <apexcharts width="100%" type="bar" :options="emoteBar" :series="emoteBar.series" height="400px" />
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs4>
            <v-card>
              <v-card-text class="px-0">
                <apexcharts width="100%" type="line" :options="averageChart" :series="averageChart.series" height="400px" />
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>

      <v-slide-y-transition mode="out-in ">

      </v-slide-y-transition>
    </v-container>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import VueApexCharts from 'vue-apexcharts';
import Recorder from 'recorder-js';
import FormData from 'form-data';
import axios from 'axios';
import db from '../private';
import IOdometer from 'vue-odometer';
import 'odometer/themes/odometer-theme-default.css';

export default {
    components: {
        apexcharts: VueApexCharts,
        IOdometer,
    },
    data() {
        return {
            numFemales: 0,
            numMales: 0,
            avgAge: 0,
            smiles: 0,
            totalNumPeople: 15,
            emoteBar: {
                chart: {
                    height: 380,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                    },
                },
                dataLabels: {
                    enabled: false,
                },
                series: [
                    {
                        data: [400, 430, 448, 470, 540, 580, 690, 1100],
                    },
                ],
                xaxis: {
                    categories: [
                        'Happiness',
                        'Neurrality',
                        'Anger',
                        'Disgust',
                        'Sadness',
                        'Suprise',
                        'Fear',
                        'Contempt',
                    ],
                },
                yaxis: {},
                tooltip: {},
            },
            azureResponse: null,
            emotionNew: {
                chart: {
                    height: 380,
                    width: 400,
                    type: 'radialBar',
                },
                plotOptions: {
                    radialBar: {
                        offsetY: -30,
                        startAngle: 0,
                        endAngle: 270,
                        hollow: {
                            margin: 5,
                            size: '30%',
                            background: 'transparent',
                            image: undefined,
                        },
                        dataLabels: {
                            name: {
                                show: false,
                            },
                            value: {
                                show: false,
                            },
                        },
                    },
                },
                colors: ['#f45942', '#f47141', '#cb74e8', '#e8d874', '#3ae4ff', '#fffbb2'],
                series: [76, 67, 61, 90, 44],
                labels: ['Anger', 'Contempt', 'Disgust', 'Fear', 'Neutral'],
                legend: {
                    show: true,
                    floating: true,
                    fontSize: '16px',
                    position: 'left',
                    verticalAlign: 'top',
                    textAnchor: 'end',
                    labels: {
                        useSeriesColors: true,
                    },
                    markers: {
                        size: 0,
                    },
                    formatter(seriesName, opts) {
                        return `${seriesName}:  ${opts.globals.series[opts.seriesIndex]}`;
                    },
                    itemMargin: {
                        vertical: 8,
                    },
                    containerMargin: {
                        left: 180,
                        top: 8,
                    },
                },
            },
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
                series: ['Anger', 'Contempt', 'Disgust', 'Fear', 'Neutral'],
                labels: [],
            },
            averageChart: {
                chart: {
                    height: 380,
                    type: 'column',
                },
                series: [
                    {
                        name: 'Average Emotion',
                        type: 'column',
                        data: [100, 100, 100, 100, 100, 100, 100, 100],
                    },
                ],
                stroke: {
                    width: [0, 4],
                },
                title: {
                    text: 'Average Emotion',
                },
                // labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                labels: [
                    'Happiness',
                    'Neurrality',
                    'Anger',
                    'Disgust',
                    'Sadness',
                    'Suprise',
                    'Fear',
                    'Contempt',
                ],
                xaxis: {
                    type: 'string',
                },
                yaxis: [
                    {
                        title: {
                            text: 'Response',
                        },
                    },
                ],
            },
            options: {
                chart: {
                    id: 'vuechart-example',
                },
                xaxis: {
                    categories: [0],
                },
            },
            series: [
                {
                    name: 'series-1',
                    data: [0],
                },
            ],
            persistantData: {
                engagementChart: { x: [], y: [] },
                emotionalBreakdown: { labels: [], sets: {} },
            },
            gumStream: null,
            rec: null,
            voice: null,
            input: null,
            AudioContext: null,
            audioContext: null,
            recorder: null,
            isRecording: false,
            blob: null,
            averages: [0, 0, 0, 0, 0, 0, 0, 0],
            colors2: [
                '#008FFB',
                '#00E396',
                '#FEB019',
                '#FF4560',
                '#775DD0',
                '#546E7A',
                '#26a69a',
                '#D10CE8',
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
        this.$store.watch(
            state => state.inSession,
            () => {
                console.log('STATE CHANGED', this.$store.state.inSession);
                if (this.$store.state.inSession) {
                    this.$store.state.autoTimerId = setInterval(() => {
                        this.callBackend();
                    }, 1000); // milliseconds
                } else {
                    this.saveSessionToDB();
                }
            }
        );

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
            const img = canvas.toDataURL('image/png');
            console.log(`Image taken!${img}`);
        };

        // window.setInterval(this.addData(), 1000);
    },
    methods: {
        async startRec1() {
            const sleep = time => new Promise(resolve => setTimeout(resolve, time));
            const recorder = await this.recordAudio();
            recorder.start();
            await sleep(5000);
            const audio = await recorder.stop();
            audio.play();
            console.log('audio yo', audio);
            const fd = new FormData();
            fd.append('fname', 'test.wav');
            fd.append('voice', audio.audioBlob);
            console.log('fd', fd);
            try {
                const response = await axios.post('http://127.0.0.1:5000/audio', fd, {
                    headers: {
                        accept: 'application/json',
                        'Accept-Language': 'en-US,en;q=0.8',
                    },
                });
                this.azureResponse = response.data;
                this.updateAzureData();
                console.log('AUDIO DATAA: ', response.data);
            } catch (err) {
                console.log('Error with axios post file: ', err);
            }
        },
        recordAudio() {
            return new Promise(resolve => {
                navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
                    const mediaRecorder = new MediaRecorder(stream);
                    const audioChunks = [];

                    mediaRecorder.addEventListener('dataavailable', event => {
                        audioChunks.push(event.data);
                    });

                    const start = () => {
                        mediaRecorder.start();
                    };

                    const stop = () =>
                        new Promise(resolve => {
                            mediaRecorder.addEventListener('stop', () => {
                                const audioBlob = new Blob(audioChunks, { type: 'audio/wav;' });
                                const audioUrl = URL.createObjectURL(audioBlob);
                                const audio = new Audio(audioUrl);
                                const play = () => {
                                    audio.play();
                                };
                                resolve({ audioBlob, audioUrl, play });
                            });

                            mediaRecorder.stop();
                        });

                    resolve({ start, stop });
                });
            });
        },
        startR() {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.recorder = new Recorder(this.audioContext, {
                // An array of 255 Numbers
                // You can use this to visualize the audio stream
                // If you use react, check out react-wave-stream
                onAnalysed: data => null,
            });
            navigator.mediaDevices
                .getUserMedia({ audio: true })
                .then(stream => this.recorder.init(stream))
                .catch(err => console.log('Uh oh... unable to get stream...', err));

            this.recorder.start().then(() => (this.isRecording = true));
            console.log('Started reco');
        },
        stopR() {
            this.recorder.stop().then(({ blob, buffer }) => {
                this.blob = blob;
            });
            Recorder.download(this.blob, 'my-audio-file');
        },
        stopRecording() {
            console.log('stopButton clicked');
            // tell the recorder to stop the recording
            this.rec.stop();
            // stop microphone access
            this.gumStream.getAudioTracks()[0].stop();
            // create the wav blob and pass it on to createDownloadLink
            this.voice = this.rec.exportWAV;
        },
        startRecording() {
            this.AudioContext = window.AudioContext || window.webkitAudioContext;
            this.audioContext = new AudioContext(); // new audio context to help us record

            console.log('recordButton clicked');
            const constraints = { audio: true, video: false };
            const parent = this;
            navigator.mediaDevices
                .getUserMedia(constraints)
                .then(stream => {
                    console.log(
                        'getUserMedia() success, stream created, initializing Recorder.js ...'
                    );
                    // update the format
                    /*  assign to gumStream for later use  */
                    try {
                        parent.gumStream = stream;
                        parent.input = parent.audioContext.createMediaStreamSource(stream);
                        console.log(parent.gumStream);
                        parent.rec = new Recorder(parent.input, { numChannels: 1 });
                        console.log('Recorder Made');
                        // start the recording process
                        parent.rec.record();
                        console.log('Recording started');
                    } catch (err) {
                        console.log('Gum error', err);
                    }
                    /* use the stream */
                    /*
                Create the Recorder object and configure to record mono sound (1 channel)
                Recording 2 channels  will double the file size
            */
                })
                .catch(err => {});
        },
        async newFirebaseSession() {
            try {
                const response = await db
                    .collection('sessions')
                    .doc((new Date() * 1000).toString())
                    .set(this.persistantData);
                console.log('fb success');
            } catch (err) {
                console.log('Error updating firebase: ', err);
            }
        },
        async saveSessionToDB() {
            try {
                const response = await db
                    .collection('sessions')
                    .doc((new Date() * 1000).toString())
                    .set(this.persistantData);
                console.log('Saved session to the database!');
            } catch (err) {
                console.log('Error updating firebase: ', err);
            }
        },
        async callBackend() {
            console.log('DAFWEFGWG', this.$store.state.timeElapsed);
            const video = document.querySelector('#videoElement');
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            // Other browsers will fall back to image/png
            const img = canvas.toDataURL('image/png');
            const blob = this.dataURItoBlob(img);
            const fd = new FormData();
            fd.append('audience_image', blob);

            const data = new FormData();
            data.append('audience_image', img, 'myimage1');
            console.log('data', data);
            try {
                const response = await axios.post('http://127.0.0.1:5000/messages', fd, {
                    headers: {
                        accept: 'application/json',
                        'Accept-Language': 'en-US,en;q=0.8',
                    },
                });
                this.azureResponse = response.data;
                this.updateAzureData();
                console.log('AI DATA: ', response.data);
            } catch (err) {
                console.log('Error with axios post file: ', err);
            }
        },
        addData() {
            this.options.xaxis.categories.push(Math.floor(Math.random() * 100));
            this.series[0].data.push(Math.floor(Math.random() * 100));
            this.series[0].data.shift();
            this.options.xaxis.categories.shift();
        },
        computeAverageEmotions() {
            this.averageChart.series[0].data[0] += this.azureResponse.anger;
            this.averageChart.series[0].data[1] += this.azureResponse.neutral;
            this.averageChart.series[0].data[2] += this.azureResponse.anger;
            this.averageChart.series[0].data[3] += this.azureResponse.disgust;
            this.averageChart.series[0].data[4] += this.azureResponse.sadness;
            this.averageChart.series[0].data[5] += this.azureResponse.surprise;
            this.averageChart.series[0].data[6] += this.azureResponse.fear;
            this.averageChart.series[0].data[7] += this.azureResponse.contempt;
        },
        updateAzureData() {
            console.log('EMOO', this.azureResponse.neutral);
            this.persistantData.engagementChart.y.push(this.azureResponse.engagement_pct);
            this.persistantData.engagementChart.x.push(
                this.timeStrToSecs(this.$store.state.timeElapsed)
            );
            this.persistantData.emotionalBreakdown.labels = this.emoteBar.xaxis.categories;
            this.persistantData.emotionalBreakdown.sets[
                Object.keys(this.persistantData.emotionalBreakdown.sets).length
            ] = [
                this.azureResponse.anger,
                this.azureResponse.neutral,
                this.azureResponse.anger,
                this.azureResponse.disgust,
                this.azureResponse.sadness,
                this.azureResponse.surprise,
                this.azureResponse.fear,
                this.azureResponse.contempt,
            ];
            this.options.xaxis.categories.push(this.timeStrToSecs(this.$store.state.timeElapsed));
            this.series[0].data.push(this.azureResponse.engagement_pct);
            if (this.options.xaxis.categories.length > 20) {
                this.options.xaxis.categories.shift();
                this.series[0].data.shift();
            }
            this.emoteBar.series[0].data = [
                this.azureResponse.anger,
                this.azureResponse.neutral,
                this.azureResponse.anger,
                this.azureResponse.disgust,
                this.azureResponse.sadness,
                this.azureResponse.surprise,
                this.azureResponse.fear,
                this.azureResponse.contempt,
            ];
            this.smiles = Math.round(this.azureResponse.smiles_incrowd_pct);
            this.totalNumPeople = Math.round(this.azureResponse.total_ppl);
            this.avgAge = Math.round(this.azureResponse.avg_age_incrowd);
            this.numMales = Math.round(this.azureResponse.males_incrowd_pct);
            this.numFemales = 100 - Math.round(this.azureResponse.males_incrowd_pct);

            this.computeAverageEmotions();
            // this.series[0].data.shift();
            // this.options.xaxis.categories.shift();
        },
        updateEmotionBreakdown() {
            const n = [];
            for (let i = 0; i < 4; i++) {
                n.push(Math.floor(Math.random() * 100));
            }
            this.emotionBreakdown.series = n;
        },
        dataURItoBlob(dataURI) {
            // convert base64/URLEncoded data component to raw binary data held in a string
            let byteString;
            if (dataURI.split(',')[0].indexOf('base64') >= 0) {
                byteString = atob(dataURI.split(',')[1]);
            } else byteString = unescape(dataURI.split(',')[1]);

            // separate out the mime component
            const mimeString = dataURI
                .split(',')[0]
                .split(':')[1]
                .split(';')[0];

            // write the bytes of the string to a typed array
            const ia = new Uint8Array(byteString.length);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }

            return new Blob([ia], { type: mimeString });
        },
        timeStrToSecs(timein) {
            const a = timein.split(':'); // split it at the colons
            // minutes are worth 60 seconds. Hours are worth 60 minutes.
            const seconds = +a[0] * 60 * 60 + +a[1] * 60 + +a[2];
            return seconds;
        },
        visiualizeAudio() {
            const paths = document.getElementById('aud').getElementsByTagName('path');
            const visualizer = document.getElementById('visualizer');
            const mask = visualizer.getElementById('mymask');
            const h = document.getElementsByTagName('h1')[0];
            let path;
            const report = 0;
            console.log('suhhhhhhhhh', paths);
            const soundAllowed = function(stream) {
                // Audio stops listening in FF without // window.persistAudioStream = stream;
                // https://bugzilla.mozilla.org/show_bug.cgi?id=965483
                // https://support.mozilla.org/en-US/questions/984179
                window.persistAudioStream = stream;
                h.innerHTML = 'Thanks';
                h.setAttribute('style', 'opacity: 0;');
                const audioContent = new AudioContext();
                const audioStream = audioContent.createMediaStreamSource(stream);
                const analyser = audioContent.createAnalyser();
                audioStream.connect(analyser);
                analyser.fftSize = 1024;

                const frequencyArray = new Uint8Array(analyser.frequencyBinCount);
                visualizer.setAttribute('viewBox', '0 0 255 255');

                // Through the frequencyArray has a length longer than 255, there seems to be no
                // significant data after this point. Not worth visualizing.
                for (let i = 0; i < 255; i++) {
                    path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                    path.setAttribute('stroke-dasharray', '4,1');
                    mask.appendChild(path);
                }
                var doDraw = function() {
                    requestAnimationFrame(doDraw);
                    analyser.getByteFrequencyData(frequencyArray);
                    let adjustedLength;
                    for (let i = 0; i < 255; i++) {
                        adjustedLength =
                            Math.floor(frequencyArray[i]) - Math.floor(frequencyArray[i]) % 5;
                        paths[i].setAttribute('d', `M ${i},255 l 0,-${adjustedLength}`);
                    }
                };
                doDraw();
            };

            const soundNotAllowed = function(error) {
                h.innerHTML = 'You must allow your microphone.';
                console.log(error);
            };

            /* window.navigator = window.navigator || {};
    /*navigator.getUserMedia =  navigator.getUserMedia       ||
                              navigator.webkitGetUserMedia ||
                              navigator.mozGetUserMedia    ||
                              null; */
            // navigator.getUserMedia({ audio: true }, soundAllowed, soundNotAllowed);
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

#audh {
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

.iOdometer {
    font-size: 2em;
    margin: 0;
}
</style>
