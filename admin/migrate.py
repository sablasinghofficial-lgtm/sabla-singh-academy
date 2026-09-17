import os
import re

base_dir = r"c:\Users\mathu\Desktop\1%\S makeup\admin"

def process_file(filename):
    path = os.path.join(base_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Logo replacement
    content = content.replace('src="../logo.png"', 'src="../logo_transparent.png"')

    # Extract script content
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if not script_match:
        return
    
    script_content = script_match.group(1)
    
    # Common replacements
    script_content = script_content.replace(
        "const res = await fetch('/api/admin/courses');",
        "const querySnapshot = await getDocs(collection(db, 'courses'));"
    ).replace(
        "const res = await fetch('/api/admin/gallery');",
        "const querySnapshot = await getDocs(collection(db, 'gallery'));"
    ).replace(
        "const res = await fetch('/api/admin/services');",
        "const querySnapshot = await getDocs(collection(db, 'services'));"
    ).replace(
        "const res = await fetch('/api/admin/vlogs');",
        "const querySnapshot = await getDocs(collection(db, 'vlogs'));"
    )

    # Replace `.json()` mapping
    script_content = re.sub(
        r'all([A-Za-z]+) = await res\.json\(\);',
        r'all\1 = querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));',
        script_content
    )
    script_content = re.sub(
        r'const ([a-z]+) = await res\.json\(\);',
        r'const \1 = querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));',
        script_content
    )

    # Delete mapping
    script_content = re.sub(
        r"await fetch\(`/api/admin/([a-z]+)/\$\{id\}`,\s*\{\s*method:\s*'DELETE'\s*\}\);",
        r"await deleteDoc(doc(db, '\1', id));",
        script_content
    )

    # POST / PUT for vlogs mapping
    script_content = re.sub(
        r"const url = id \? `/api/admin/([a-z]+)/\$\{id\}` : `/api/admin/\1`;\s*"
        r"const method = id \? 'PUT' : 'POST';\s*"
        r"await fetch\(url, \{\s*method: method,\s*headers: \{ 'Content-Type': 'application/json' \},\s*body: JSON\.stringify\((.*?)\)\s*\}\);",
        r"if (id) { await updateDoc(doc(db, '\1', id), \2); } else { await addDoc(collection(db, '\1'), \2); }",
        script_content
    )

    # Logout
    script_content = re.sub(
        r"await fetch\('/api/auth/logout',\s*\{\s*method:\s*'POST'\s*\}\);",
        r"await signOut(auth);",
        script_content
    )

    # Functions to window. (like function openModal, function deleteCourse)
    # Be careful with async function and normal function
    script_content = re.sub(
        r"async function ([a-zA-Z0-9_]+)\((.*?)\)",
        r"window.\1 = async function(\2)",
        script_content
    )
    script_content = re.sub(
        r"function ([a-zA-Z0-9_]+)\((.*?)\)",
        r"window.\1 = function(\2)",
        script_content
    )

    # If res.status === 401 is there, we remove it, since we handle auth state at the top.
    script_content = re.sub(
        r"if \(res\.status === 401\).*?;",
        "",
        script_content
    )

    # Add module imports and auth wrapper
    init = """
        import { auth, db, collection, getDocs, addDoc, deleteDoc, doc, updateDoc, onAuthStateChanged, signOut } from './js/firebase-init.js';

        onAuthStateChanged(auth, async (user) => {
            if (!user) {
                window.location.href = 'login.html';
                return;
            }
            if (typeof window.loadcourses === 'function') await window.loadcourses();
            if (typeof window.loadServices === 'function') await window.loadServices();
            if (typeof window.loadgallery === 'function') await window.loadgallery();
            if (typeof window.loadVlogs === 'function') await window.loadVlogs();
        });
"""

    script_content = init + script_content

    # Now make the script type="module"
    new_script = f'<script type="module">{script_content}</script>'
    content = content.replace(script_match.group(0), new_script)
    
    # Change onclicks to string id where applicable: deleteCourse(${s.id}) -> deleteCourse('${s.id}')
    # Similarly for editCourse
    content = re.sub(r"deleteCourse\((\$\{.+?\})\)", r"deleteCourse('\1')", content)
    content = re.sub(r"editCourse\((\$\{.+?\})\)", r"editCourse('\1')", content)
    content = re.sub(r"deletePhoto\((\$\{.+?\})\)", r"deletePhoto('\1')", content)
    content = re.sub(r"editService\((\$\{.+?\})\)", r"editService('\1')", content)
    content = re.sub(r"deleteService\((\$\{.+?\})\)", r"deleteService('\1')", content)
    content = re.sub(r"editVlog\((\$\{.+?\})\)", r"editVlog('\1')", content)
    content = re.sub(r"deleteVlog\((\$\{.+?\})\)", r"deleteVlog('\1')", content)

    # The load function inside script was made window.loadcourses, wait.
    # The original file had loadcourses() at the bottom.
    content = re.sub(r"^\s*(loadcourses|loadServices|loadgallery|loadVlogs)\(\);\s*$", "", content, flags=re.MULTILINE)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


for f in ['courses.html', 'gallery.html', 'services.html', 'vlogs.html', 'settings.html']:
    process_file(f)
