# -*- coding: utf-8 -*-
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

typewriter_js = """
// Typewriter Effect
const tw = document.getElementById('typewriter');
if (tw) {
    const words = ["Excellence", "Elegance", "Perfection", "Artistry"];
    let wI = 0;
    let cI = 0;
    let isDeleting = false;

    function typeEffect() {
        const currentWord = words[wI];
        
        if (isDeleting) {
            tw.textContent = currentWord.substring(0, cI - 1);
            cI--;
        } else {
            tw.textContent = currentWord.substring(0, cI + 1);
            cI++;
        }

        let typeSpeed = isDeleting ? 50 : 100;

        if (!isDeleting && cI === currentWord.length) {
            typeSpeed = 2000; // Pause at the end of word
            isDeleting = true;
        } else if (isDeleting && cI === 0) {
            isDeleting = false;
            wI = (wI + 1) % words.length;
            typeSpeed = 500; // Pause before typing new word
        }

        setTimeout(typeEffect, typeSpeed);
    }
    
    // Start typing
    setTimeout(typeEffect, 1000);
}
"""

if 'const tw = document.getElementById(\'typewriter\');' not in js:
    js += '\n' + typewriter_js
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Typewriter JS added")
else:
    print("Already exists")
