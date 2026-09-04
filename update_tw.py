with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Remove old typewriter code and add upgraded one
if "const tw = document.getElementById(" in js:
    start = js.find("// Typewriter Effect")
    if start == -1:
        start = js.find("const tw = document.getElementById(")
    end = js.find("\n}", start) + 2
    js = js[:start] + js[end:]

new_tw = """
// ===== Typewriter Effect =====
(function(){
  const el = document.getElementById("typewriter");
  if (!el) return;
  const words = ["CONFIDENCE", "EXCELLENCE", "ELEGANCE", "ARTISTRY", "YOUR FUTURE"];
  let wI = 0, cI = 0, deleting = false;

  function type() {
    const word = words[wI];
    el.textContent = deleting ? word.substring(0, cI - 1) : word.substring(0, cI + 1);
    deleting ? cI-- : cI++;

    let speed = deleting ? 40 : 90;
    if (!deleting && cI === word.length) { speed = 2200; deleting = true; }
    else if (deleting && cI === 0) { deleting = false; wI = (wI + 1) % words.length; speed = 400; }
    setTimeout(type, speed);
  }
  setTimeout(type, 800);
})();
"""

js = js.rstrip() + "\n" + new_tw

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Typewriter updated!")
