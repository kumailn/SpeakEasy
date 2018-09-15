import firebase from 'firebase';

// Initialize Firebase
const config = {
  apiKey: 'AIzaSyBv_asVDo6QMLMM4GWcxOQFEamvK6yYfPY',
  authDomain: 'htn2018-cf008.firebaseapp.com',
  databaseURL: 'https://htn2018-cf008.firebaseio.com',
  projectId: 'htn2018-cf008',
  storageBucket: 'htn2018-cf008.appspot.com',
  messagingSenderId: '823759780493',
};

const firebaseApp = firebase.initializeApp(config);
firebaseApp.firestore().settings({ timestampsInSnapshots: true });
export default firebaseApp.firestore();
