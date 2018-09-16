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
          <v-card id="aud" >
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
                      <v-card-text class="px-0">
              <apexcharts width="100%" type="line" :options="futureChart" :series="futureChart.series" height="390px" />
            </v-card-text>
        </v-flex>
        <v-flex xs4>
          <v-card>
            <v-card-text class="px-0">
              <apexcharts width="100%" type="pie" :options="emotionNew" :series="emotionNew.series" height="390px" />
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
import FormData from 'form-data';
import axios from 'axios';
import db from '../private';

export default {
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
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
          categories: [0],
        },
      },
      series: [
        {
          name: 'series-1',
          data: [0],
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
    this.$store.watch(
      state => state.inSession,
      () => {
        console.log('STATE CHANGED', this.$store.state.inSession);
        if (this.$store.state.inSession) {
          this.$store.state.autoTimerId = setInterval(() => {
            this.callBackend();
          }, 1000); // milliseconds
        }
      },
    );

    this.visiualizeAudio();
    this.newFirebaseSession();
    const video = document.querySelector('#videoElement');

    // if (navigator.mediaDevices.getUserMedia) {
    //     navigator.mediaDevices
    //         .getUserMedia({ video: true })
    //         .then(stream => {
    //             video.srcObject = stream;
    //         })
    //         .catch(err0r => {
    //             console.log('Something went wrong!');
    //         });
    // }

    // const canvas = document.createElement('canvas');
    // const screenshotButton = document.querySelector('#screenshotButton');

    screenshotButton.onclick = video.onclick = function () {
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      // Other browsers will fall back to image/png
      const img = canvas.toDataURL('image/png');
      console.log(`Image taken!${img}`);
    };

    const recordButton = document.querySelector('#recordButton');
    const stopButton = document.querySelector('#stopButton');
    let rec;
    let gumStream;
    recordButton.addEventListener('click', startRecording);
    stopButton.addEventListener('click', stopRecording);

    function startRecording() {
      console.log('recordButton clicked');
      const constraints = { audio: true, video: false };
      navigator.mediaDevices
        .getUserMedia(constraints)
        .then((stream) => {
          console.log('getUserMedia() success, stream created, initializing Recorder.js ...');
          // update the format
          /*  assign to gumStream for later use  */
          gumStream = stream;
          console.log(gumStream);
          /* use the stream */
          /*
                Create the Recorder object and configure to record mono sound (1 channel)
                Recording 2 channels  will double the file size
            */
          rec = new Recorder(input, { numChannels: 1 });
          console.log('Recorder Made');
          // start the recording process
          rec.record();
          console.log('Recording started');
        })
        .catch((err) => {});
    }

    function stopRecording() {
      console.log('stopButton clicked');
      // tell the recorder to stop the recording
      rec.stop();
      // stop microphone access
      gumStream.getAudioTracks()[0].stop();
      // create the wav blob and pass it on to createDownloadLink
      rec.exportWAV(createDownloadLink);
    }

    function createDownloadLink(blob) {
      const url = URL.createObjectURL(blob);
      const au = document.createElement('audio');
      const li = document.createElement('li');
      const link = document.createElement('a');

      // name of .wav file to use during upload and download (without extendion)
      const filename = new Date().toISOString();

      // add controls to the <audio> element
      au.controls = true;
      au.src = url;

      // save to disk link
      link.href = url;
      link.download = `${filename}.wav`; // download forces the browser to donwload the file using the  filename
      link.innerHTML = 'Save to disk';

      // add the new audio element to li
      li.appendChild(au);

      // add the filename to the li
      li.appendChild(document.createTextNode(`${filename}.wav `));

      // add the save to disk link to li
      li.appendChild(link);

      // upload link
      const upload = document.createElement('a');
      upload.href = '#';
      upload.innerHTML = 'Upload';
      upload.addEventListener('click', (event) => {
        const xhr = new XMLHttpRequest();
        xhr.onload = function (e) {
          if (this.readyState === 4) {
            console.log('Server returned: ', e.target.responseText);
          }
        };
        const fd = new FormData();
        fd.append('audio_data', blob, filename);
        xhr.open('POST', 'upload.php', true);
        xhr.send(fd);
      });
      li.appendChild(document.createTextNode(' ')); // add a space in between
      li.appendChild(upload); // add the upload link to li

      // add the li element to the ol
      recordingsList.appendChild(li);
    }

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
    updateAzureData() {
      console.log('foewuhfuiwe');
      console.log('EMOO', this.azureResponse.neutral);
      this.series[0].data.push(this.azureResponse.total_ppl);
      this.emotionNew.series = [
        this.azureResponse.anger,
        this.azureResponse.contempt,
        this.azureResponse.disgust,
        this.azureResponse.fear,
        this.azureResponse.neutral,
      ];

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
      if (dataURI.split(',')[0].indexOf('base64') >= 0) { byteString = atob(dataURI.split(',')[1]); } else byteString = unescape(dataURI.split(',')[1]);

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
    visiualizeAudio() {
      const paths = document.getElementById('aud').getElementsByTagName('path');
      const visualizer = document.getElementById('visualizer');
      const mask = visualizer.getElementById('mymask');
      const h = document.getElementsByTagName('h1')[0];
      let path;
      const report = 0;
      console.log('suhhhhhhhhh', paths);
      const soundAllowed = function (stream) {
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
        var doDraw = function () {
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

      const soundNotAllowed = function (error) {
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
