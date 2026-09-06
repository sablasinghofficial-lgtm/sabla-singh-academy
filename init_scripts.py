import os

firebase_js = '''
// Firebase SDKs
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getFirestore, collection, getDocs, doc, setDoc, deleteDoc, updateDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

const firebaseConfig = {
  projectId: "sabla-singh-academy-f9547",
  appId: "1:119769884219:web:c956052ddce7a1eabf9e1e",
  storageBucket: "sabla-singh-academy-f9547.firebasestorage.app",
  apiKey: "AIzaSyCNlUjfBzF8eFLxTQgB0rk0FK3OOQqjtqg",
  authDomain: "sabla-singh-academy-f9547.firebaseapp.com",
  messagingSenderId: "119769884219",
  measurementId: "G-KP3WY78M9F"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

window.db = db;
window.auth = auth;
window.collection = collection;
window.getDocs = getDocs;
window.doc = doc;
window.setDoc = setDoc;
window.deleteDoc = deleteDoc;
window.updateDoc = updateDoc;
window.signInWithEmailAndPassword = signInWithEmailAndPassword;
window.onAuthStateChanged = onAuthStateChanged;
window.signOut = signOut;
'''

cloudinary_js = '''
const CLOUD_NAME = "iqlwz76c";
const UPLOAD_PRESET = "ml_default";

window.openCloudinaryWidget = function(callback) {
    cloudinary.createUploadWidget({
        cloudName: CLOUD_NAME,
        uploadPreset: UPLOAD_PRESET,
        sources: ['local', 'url', 'camera'],
        multiple: false
    }, (error, result) => {
        if (!error && result && result.event === "success") {
            callback(result.info.secure_url);
        }
    }).open();
};
'''

if not os.path.exists('admin/js'):
    os.makedirs('admin/js')

with open('admin/js/firebase-init.js', 'w') as f:
    f.write(firebase_js)

with open('admin/js/cloudinary-init.js', 'w') as f:
    f.write(cloudinary_js)

print("Created firebase-init.js and cloudinary-init.js")
