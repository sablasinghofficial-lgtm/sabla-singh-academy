import re

with open('admin/login.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add mapping logic to login.html
new_script = """
    <script type="module">
        import { auth, signInWithEmailAndPassword } from './js/firebase-init.js';
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = e.target.querySelector('button');
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            btn.disabled = true;

            let email = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value;

            // Map custom username to actual Firebase email
            if (email === 'Sablasingh@0404' || email.toLowerCase() === 'admin') {
                email = 'sablasinghofficial@gmail.com';
            }

            try {
                await signInWithEmailAndPassword(auth, email, password);
                window.location.href = 'dashboard.html';
            } catch (err) {
                document.getElementById('errorMsg').style.display = 'block';
                document.getElementById('errorMsg').innerText = "Error: Invalid credentials or user not found.";
                console.error(err);
                btn.innerHTML = 'Sign In';
                btn.disabled = false;
            }
        });
    </script>
"""

content = re.sub(r'<script type="module">.*?</script>', new_script, content, flags=re.DOTALL)
# Also fix logo in admin login just in case
content = content.replace('src="../logo.png"', 'src="../logo_transparent.png"')

with open('admin/login.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("login.html updated")
