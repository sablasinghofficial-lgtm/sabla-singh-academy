import os
import re

html_content = """
    <script type="module">
        import { auth, db, collection, getDocs, onAuthStateChanged, signOut } from './js/firebase-init.js';
        
        onAuthStateChanged(auth, async (user) => {
            if (!user) {
                window.location.href = 'login.html';
                return;
            }
            document.getElementById('adminName').innerText = user.email.split('@')[0];
            await loadDashboard();
        });

        async function loadDashboard() {
            try {
                // Queries
                const qSnap = await getDocs(collection(db, 'queries'));
                const queries = [];
                let newQueries = 0;
                qSnap.forEach(doc => {
                    const data = doc.data();
                    queries.push({ id: doc.id, ...data });
                    if(data.status === 'New') newQueries++;
                });
                
                // Sort by date desc (assuming created_at exists)
                queries.sort((a,b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

                document.getElementById('statQueries').innerText = queries.length;

                if (newQueries > 0) {
                    const badge = document.getElementById('newQCount');
                    badge.style.display = 'inline-block';
                    badge.innerText = newQueries;
                }

                // Recent queries
                const tbody = document.getElementById('recentQueries');
                tbody.innerHTML = '';
                
                if (queries.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:#888;">No enquiries yet.</td></tr>';
                } else {
                    queries.slice(0, 5).forEach(q => {
                        const date = q.created_at ? new Date(q.created_at).toLocaleDateString() : '-';
                        const badgeClass = (q.status || 'New').toLowerCase();
                        tbody.innerHTML += `
                            <tr>
                                <td>${date}</td>
                                <td><strong>${q.name}</strong></td>
                                <td>${q.phone}</td>
                                <td>${q.interested_in || '-'}</td>
                                <td><span class="badge ${badgeClass}">${q.status || 'New'}</span></td>
                            </tr>
                        `;
                    });
                }

                // Mock other stats since we might not have collections yet
                const sSnap = await getDocs(collection(db, 'services'));
                document.getElementById('statServices').innerText = sSnap.size;
                
                const cSnap = await getDocs(collection(db, 'courses'));
                document.getElementById('statCourses').innerText = cSnap.size;
                
                const gSnap = await getDocs(collection(db, 'gallery'));
                document.getElementById('statGallery').innerText = gSnap.size;

            } catch (err) {
                console.error("Dashboard error:", err);
            }
        }

        window.logout = async function() {
            await signOut(auth);
            window.location.href = 'login.html';
        }
    </script>
"""

with open('admin/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old script with new module script
content = re.sub(r'<script>\s*async function loadDashboard.*?</script>', html_content, content, flags=re.DOTALL)
# Add module to firebase init in head if missing
if '<script type="module" src="js/firebase-init.js"></script>' not in content:
    content = content.replace('</head>', '    <script type="module" src="js/firebase-init.js"></script>\n</head>')
# Replace logo
content = content.replace('src="../logo.png"', 'src="../logo_transparent.png"')

with open('admin/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.html updated")
