import os
import re

admin_files = ['admin/queries.html', 'admin/courses.html', 'admin/services.html', 'admin/gallery.html', 'admin/vlogs.html', 'admin/settings.html']

firebase_imports = """
    <script type="module" src="js/firebase-init.js"></script>
"""

# The goal is to replace the old <script> tags with a new module script that imports from firebase-init.js
# However, each file has completely different logic.
# It would take too long to write regex for each.
