import re

html_script = """
    <script type="module">
        import { auth, db, collection, getDocs, doc, deleteDoc, updateDoc, onAuthStateChanged, signOut } from './js/firebase-init.js';

        let allQueries = [];

        onAuthStateChanged(auth, async (user) => {
            if (!user) {
                window.location.href = 'login.html';
                return;
            }
            await loadQueries();
        });

        async function loadQueries() {
            try {
                const qSnap = await getDocs(collection(db, 'queries'));
                allQueries = [];
                qSnap.forEach(d => {
                    allQueries.push({ id: d.id, ...d.data() });
                });
                // Sort by date desc
                allQueries.sort((a,b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
                renderQueries(allQueries);
            } catch (err) {
                console.error(err);
            }
        }

        window.renderQueries = function(queries) {
            const tbody = document.getElementById('queriesTable');
            tbody.innerHTML = '';
            
            if (queries.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" style="text-align:center;color:#888;">No enquiries found.</td></tr>';
                return;
            }

            queries.forEach(q => {
                const date = q.created_at ? new Date(q.created_at).toLocaleString() : '-';
                const status = q.status || 'New';
                tbody.innerHTML += `
                    <tr>
                        <td style="white-space:nowrap;font-size:0.85rem;color:#888;">${date}</td>
                        <td><strong>${q.name}</strong></td>
                        <td>${q.phone}<br><span style="font-size:0.8rem;color:#888;">${q.email||'-'}</span></td>
                        <td>${q.interested_in || '-'}</td>
                        <td class="msg-cell" onclick='viewQuery(${JSON.stringify(q).replace(/'/g, "&#39;")})'>${q.message || '<em style="color:#aaa;">No message</em>'}</td>
                        <td>
                            <select class="status-select" onchange="updateStatus('${q.id}', this.value)">
                                <option value="New" ${status === 'New' ? 'selected' : ''}>New</option>
                                <option value="Contacted" ${status === 'Contacted' ? 'selected' : ''}>Contacted</option>
                                <option value="Resolved" ${status === 'Resolved' ? 'selected' : ''}>Resolved</option>
                            </select>
                        </td>
                        <td class="action-btns">
                            <button title="View Details" onclick='viewQuery(${JSON.stringify(q).replace(/'/g, "&#39;")})'><i class="fas fa-eye"></i></button>
                            <button title="Delete" onclick="deleteQuery('${q.id}')" style="color:#dc3545;"><i class="fas fa-trash"></i></button>
                        </td>
                    </tr>
                `;
            });
        }

        window.filterQueries = function() {
            const search = document.getElementById('searchInput').value.toLowerCase();
            const status = document.getElementById('statusFilter').value;
            
            const filtered = allQueries.filter(q => {
                const nameMatch = q.name ? q.name.toLowerCase().includes(search) : false;
                const phoneMatch = q.phone ? q.phone.includes(search) : false;
                const matchesSearch = nameMatch || phoneMatch;
                const qStatus = q.status || 'New';
                const matchesStatus = status === 'All' || qStatus === status;
                return matchesSearch && matchesStatus;
            });
            renderQueries(filtered);
        }

        window.updateStatus = async function(id, status) {
            try {
                await updateDoc(doc(db, 'queries', id), { status });
                const q = allQueries.find(x => x.id === id);
                if(q) q.status = status;
            } catch (err) {
                console.error(err);
                alert('Error updating status');
            }
        }

        window.deleteQuery = async function(id) {
            if(confirm('Are you sure you want to delete this enquiry?')) {
                try {
                    await deleteDoc(doc(db, 'queries', id));
                    await loadQueries();
                } catch (err) {
                    console.error(err);
                    alert('Error deleting');
                }
            }
        }

        window.viewQuery = function(q) {
            const date = q.created_at ? new Date(q.created_at).toLocaleString() : '-';
            const status = q.status || 'New';
            let html = `
                <p><strong>Date:</strong> ${date}</p>
                <p><strong>Name:</strong> ${q.name}</p>
                <p><strong>Phone:</strong> <a href="tel:${q.phone}">${q.phone}</a></p>
                <p><strong>Email:</strong> ${q.email ? `<a href="mailto:${q.email}">${q.email}</a>` : '-'}</p>
                <p><strong>Interested In:</strong> ${q.interested_in || '-'}</p>
                <p><strong>Status:</strong> <span class="badge ${status.toLowerCase()}">${status}</span></p>
                <div class="modal-msg">${q.message || 'No additional message provided.'}</div>
                <div style="margin-top:20px;text-align:right;">
                    <a href="https://wa.me/91${q.phone}" target="_blank" class="btn-gold" style="text-decoration:none;display:inline-block;padding:10px 20px;width:auto;"><i class="fab fa-whatsapp"></i> WhatsApp Client</a>
                </div>
            `;
            document.getElementById('modalBody').innerHTML = html;
            document.getElementById('viewModal').style.display = 'flex';
        }

        window.closeModal = function() {
            document.getElementById('viewModal').style.display = 'none';
        }

        window.logout = async function() {
            await signOut(auth);
            window.location.href = 'login.html';
        }
    </script>
"""

with open('admin/queries.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<script>\s*let allQueries = \[\];.*?</script>', html_script, content, flags=re.DOTALL)
content = content.replace('src="../logo.png"', 'src="../logo_transparent.png"')

with open('admin/queries.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("queries.html updated")
