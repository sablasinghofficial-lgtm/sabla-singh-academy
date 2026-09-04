AOS.init({once:true,offset:50,duration:700});

const bt = document.getElementById('backTop');
if (bt) {
    window.addEventListener('scroll',()=>{ bt.classList.toggle('visible', scrollY>500) });
}

const hb = document.getElementById('hamburger'), mm = document.getElementById('mobMenu');
if (hb && mm) {
    hb.onclick = () => {
        hb.classList.toggle('active');
        mm.classList.toggle('active');
        document.body.style.overflow = mm.classList.contains('active') ? 'hidden' : '';
    };
    document.querySelectorAll('.ml').forEach(l => l.onclick = () => {
        hb.classList.remove('active');
        mm.classList.remove('active');
        document.body.style.overflow = '';
    });
}

// Counters
const counters = document.querySelectorAll('.counter');
if (counters.length > 0) {
    const cO = new IntersectionObserver(es => {
        es.forEach(e => {
            if(e.isIntersecting){
                const el = e.target, t = +el.dataset.count, s = t/112;
                let c = 0;
                const ti = setInterval(()=>{
                    c += s;
                    if(c >= t){ c = t; clearInterval(ti); }
                    el.textContent = Math.floor(c).toLocaleString();
                }, 16);
                cO.unobserve(el);
            }
        });
    }, {threshold:.5});
    counters.forEach(c => cO.observe(c));
}

// Hero carousel
const hImg = document.getElementById('heroImg');
if (hImg) {
    const hImgs = ['https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=800&q=80',
                   'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800&q=80',
                   'https://images.unsplash.com/photo-1494587416117-f102a2ac0a8d?w=800&q=80',
                   'https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=800&q=80'];
    let hI = 0;
    setInterval(()=>{
        hI = (hI + 1) % hImgs.length;
        hImg.style.opacity = 0;
        setTimeout(() => { hImg.src = hImgs[hI]; hImg.style.opacity = 1; }, 350);
    }, 4500);
}

// Gallery & Testimonials
if (document.querySelector('.gal-slider')) {
    const galSwiper = new Swiper('.gal-slider', {
        slidesPerView:3, spaceBetween:10, loop:true,
        autoplay:{delay:3000, disableOnInteraction:false},
        pagination:{el:'.gal-slider .swiper-pagination', clickable:true},
        breakpoints:{0:{slidesPerView:2},600:{slidesPerView:3},900:{slidesPerView:4}}
    });
    window.galSwiper = galSwiper;
}

if (document.querySelector('.testi-sw')) {
    new Swiper('.testi-sw', {slidesPerView:1, loop:true, autoplay:{delay:5000, disableOnInteraction:false}});
}

// Lightbox
const lb = document.getElementById('lb');
if (lb) {
    window.openLB = function(el) {
        document.getElementById('lbImg').src = el.querySelector('img').src;
        lb.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    window.closeLB = function() {
        lb.classList.remove('active');
        document.body.style.overflow = '';
    }
    lb.onclick = e => { if (e.target === lb) closeLB(); };
}

// Form to WhatsApp integration
const form = document.getElementById('enquiryForm');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const inputs = this.querySelectorAll('input, select, textarea');
        const name = inputs[0].value;
        const phone = inputs[1].value;
        const email = inputs[2].value;
        const interest = inputs[3].value;
        const msg = inputs[4].value;
        
        let waText = `Hi Sabla Singh Academy! ??\nI have a new enquiry from the website:\n\n*Name:* ${name}\n*Phone:* ${phone}`;
        if(email) waText += `\n*Email:* ${email}`;
        waText += `\n*Interested In:* ${interest}\n*Message:* ${msg}`;
        
        const encodedText = encodeURIComponent(waText);
        window.open('https://wa.me/918603388406?text=' + encodedText, '_blank');
        
        const b = this.querySelector('.form-submit');
        const oldHtml = b.innerHTML;
        b.innerHTML = '? Redirecting to WhatsApp...';
        b.style.background = '#25D366';
        setTimeout(()=>{
            b.innerHTML = oldHtml;
            b.style.background = '';
            this.reset();
        }, 3000);
    });
}

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

// Video Gallery Functions
window.togglePlay = function(vidId) {
    let vid = document.getElementById(vidId);
    if (!vid) return;
    
    // Pause all other videos first
    document.querySelectorAll('.vg-video-wrap video').forEach(v => {
        if (v.id !== vidId) {
            v.pause();
            v.controls = false;
        }
    });

    if (vid.paused) {
        vid.play();
        vid.controls = true;
    } else {
        vid.pause();
    }
}

window.hideOverlay = function(vidId) {
    let overlay = document.getElementById('overlay' + vidId.replace('vid', ''));
    if (overlay) overlay.style.display = 'none';
}

window.showOverlay = function(vidId) {
    let overlay = document.getElementById('overlay' + vidId.replace('vid', ''));
    if (overlay) {
        let vid = document.getElementById(vidId);
        if (!vid.controls || vid.paused) {
            overlay.style.display = 'flex';
        }
    }
}

// --- BACKEND API INTEGRATION --- //
async function submitEnquiry(event) {
    event.preventDefault();
    const form = event.target;
    const btn = form.querySelector('.form-submit');
    const originalText = btn.innerHTML;
    
    // Get form data
    const inputs = form.querySelectorAll('input, select, textarea');
    const data = {
        name: inputs[0].value,
        phone: inputs[1].value,
        email: inputs[2].value,
        interested_in: inputs[3].value,
        message: inputs[4].value
    };

    try {
        btn.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin"></i>';
        btn.disabled = true;

        const response = await fetch('http://localhost:3000/api/enquiry', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if (result.success) {
            btn.innerHTML = 'Sent Successfully! <i class="fas fa-check"></i>';
            btn.style.background = '#25D366';
            form.reset();
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.background = '';
                btn.disabled = false;
            }, 3000);
        } else {
            throw new Error(result.message);
        }
    } catch (error) {
        console.error(error);
        btn.innerHTML = 'Error! Try Again';
        btn.style.background = '#dc3545';
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.style.background = '';
            btn.disabled = false;
        }, 3000);
    }
}

// --- HERO SLIDESHOW --- //
const slides = document.querySelectorAll('.hero-slideshow .slide');
let currentSlide = 0;
if (slides.length > 0) {
    setInterval(() => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }, 3000);
}
// --- ABOUT SLIDESHOW --- //
const aboutSlides = document.querySelectorAll('.about-slideshow .slide');
let currentAboutSlide = 0;
if (aboutSlides.length > 0) {
    setInterval(() => {
        aboutSlides[currentAboutSlide].classList.remove('active');
        currentAboutSlide = (currentAboutSlide + 1) % aboutSlides.length;
        aboutSlides[currentAboutSlide].classList.add('active');
    }, 3000);
}
