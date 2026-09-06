import os
import re

firebase_scripts = '''
    <script type="module" src="js/firebase-init.js"></script>
    <script src="https://upload-widget.cloudinary.com/global/all.js" type="text/javascript"></script>
    <script src="js/cloudinary-init.js"></script>
'''

login_script = '''<script type="module">
        import { auth, signInWithEmailAndPassword } from './js/firebase-init.js';
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = e.target.querySelector('button');
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            btn.disabled = true;

            const email = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            try {
                await signInWithEmailAndPassword(auth, email, password);
                window.location.href = 'dashboard.html';
            } catch (err) {
                document.getElementById('errorMsg').style.display = 'block';
                document.getElementById('errorMsg').innerText = err.message;
                btn.innerHTML = 'Sign In';
                btn.disabled = false;
            }
        });
    </script>'''

# Modify admin/login.html
with open('admin/login.html', 'r', encoding='utf-8') as f:
    content = f.read()
if 'firebase-init.js' not in content:
    content = content.replace('</head>', firebase_scripts + '\n</head>')
    content = re.sub(r'<script>.*?</script>', login_script, content, flags=re.DOTALL)
with open('admin/login.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated login.html")
