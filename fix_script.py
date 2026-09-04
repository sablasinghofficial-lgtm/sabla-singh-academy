# -*- coding: utf-8 -*-
new_js = '''
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

// Gallery & Testimonials (Swiper handles non-existent elements safely, but checking is cleaner)
if (document.querySelector('.gal-slider')) {
    const galSwiper = new Swiper('.gal-slider', {
        slidesPerView:3, spaceBetween:10, loop:true,
        autoplay:{delay:3000, disableOnInteraction:false},
        pagination:{el:'.gal-slider .swiper-pagination', clickable:true},
        breakpoints:{0:{slidesPerView:2},600:{slidesPerView:3},900:{slidesPerView:4}}
    });
    // Attach to window so onclick="galSwiper.slidePrev()" works
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
        
        let waText = Hi Sabla Singh Academy! ??\\nI have a new enquiry from the website:\\n\\n*Name:* \\n*Phone:* ;
        if(email) waText += \\n*Email:* ;
        waText += \\n*Interested In:* \\n*Message:* ;
        
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
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("script.js updated and robustified!")
