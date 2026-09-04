const Database = require('better-sqlite3');
const bcrypt = require('bcrypt');

const db = new Database('db/database.sqlite');

// Initialize tables
db.exec(`
  CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
  );

  CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    subtitle TEXT,
    description TEXT,
    image TEXT,
    icon TEXT,
    features TEXT,
    whatsapp_text TEXT,
    display_order INTEGER,
    status TEXT DEFAULT 'published'
  );

  CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    subtitle TEXT,
    duration TEXT,
    description TEXT,
    image TEXT,
    badge TEXT,
    features TEXT,
    whatsapp_text TEXT,
    display_order INTEGER,
    status TEXT DEFAULT 'published'
  );

  CREATE TABLE IF NOT EXISTS gallery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    image TEXT,
    display_order INTEGER,
    status TEXT DEFAULT 'published'
  );

  CREATE TABLE IF NOT EXISTS vlogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    video_url TEXT,
    thumbnail TEXT,
    display_order INTEGER,
    status TEXT DEFAULT 'published'
  );

  CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT,
    interested_in TEXT,
    message TEXT,
    status TEXT DEFAULT 'New',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

  CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
  );
`);

// Seed Admin User
const stmt = db.prepare('SELECT * FROM admin WHERE username = ?');
const admin = stmt.get('Sablasingh@0404');
if (!admin) {
  const hash = bcrypt.hashSync('sablasingh123', 10); // Replace with actual default password logic if needed, or leave as a default that they must change. User said: "Password: Use the same existing password configured for the website." Wait, there wasn't an existing backend. So I'll use a placeholder like sablasingh123 and they can change it in settings.
  db.prepare('INSERT INTO admin (username, password) VALUES (?, ?)').run('Sablasingh@0404', hash);
  console.log('Admin user seeded.');
}

// Seed Settings
const insertSetting = db.prepare('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)');
insertSetting.run('academy_name', 'Sabla Singh Academy');
insertSetting.run('founder_name', 'Sabla Singh');
insertSetting.run('phone', '8603388406');
insertSetting.run('alt_phone', '9334180760');
insertSetting.run('email', 'sablasinghofficial@gmail.com');
insertSetting.run('address', 'Studio S, Shivshakti Nagar, Opp. Sarala Birla Public School, Mahilong, Ranchi, Jharkhand 835103');
insertSetting.run('whatsapp', 'https://wa.me/918603388406');
insertSetting.run('instagram', 'https://instagram.com/SablaSinghOfficial');
insertSetting.run('facebook', 'https://facebook.com/SablaSinghOfficial');
insertSetting.run('youtube', 'https://youtube.com/@SablaSinghOfficial');

// Seed Services if empty
const serviceCount = db.prepare('SELECT COUNT(*) as count FROM services').get().count;
if (serviceCount === 0) {
  const insertService = db.prepare('INSERT INTO services (title, subtitle, description, image, icon, features, whatsapp_text, display_order) VALUES (?, ?, ?, ?, ?, ?, ?, ?)');
  insertService.run('Bridal Makeup', 'HD, Airbrush & Party Makeup — Make your special day unforgettable.', '', 'gal1.jpg', 'fas fa-gem', 'Full HD Bridal Makeup|Airbrush & Matte Finish|Engagement & Party Looks|International Brand Products', 'Hi, I want to book Bridal Makeup.', 1);
  insertService.run('Skin Care & Facial', 'Advanced facial treatments & skin rejuvenation by expert beauticians.', '', 'gal5.jpg', 'fas fa-spa', 'Deep Cleansing Facial|Skin Brightening Treatment|Gold Facial & D-Tan Cleanup|Anti-Acne & Glow Treatment', 'Hi, I want to book a Skin Facial Treatment.', 2);
  insertService.run('Hair Styling', 'Expert hair cuts, spa treatments & chemical styling for every occasion.', '', 'gal8.jpg', 'fas fa-scissors', 'Precision Haircut & Trim|Keratin & Smoothening|Global Coloring & Highlights|Bridal Updos & Open Hairstyle', 'Hi, I want to book Hair Styling.', 3);
  insertService.run('Nail Art & Extension', 'Nail art, extensions, manicure & pedicure with luxury products.', '', 'gal12.jpg', 'fas fa-hand-sparkles', 'Gel & Acrylic Extensions|Premium Nail Art Designs|Manicure & Pedicure Spa|French & Ombre Nails', 'Hi, I want to book Nail Art or Extension.', 4);
  insertService.run('Lash Extensions', 'Get gorgeous, dramatic lash extensions for a naturally stunning look.', '', 'gal16.jpg', 'fas fa-eye', 'Classic & Volume Lashes|Mega Volume Extension|Lash Lift & Tint|Long-Lasting Premium Fibers', 'Hi, I want to book Lash Extensions.', 5);
  console.log('Services seeded.');
}

// Seed Courses if empty
const courseCount = db.prepare('SELECT COUNT(*) as count FROM courses').get().count;
if (courseCount === 0) {
  const insertCourse = db.prepare('INSERT INTO courses (title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)');
  insertCourse.run('Advanced Makeup Artistry', 'Bridal HD & Airbrush Expert', '3-6 Months', 'From HD Bridal to Airbrush — master every makeup style and become a top-tier artist.', 'gal1.jpg', 'MOST POPULAR', 'International Airbrush Techniques|Advanced HD Bridal Artistry|Editorial & Fashion Styling', 'Hi, I want details for the Advanced Makeup Artistry Course.', 1);
  insertCourse.run('Elite Hair Design & Styling', 'Precision Cuts & Chemicals', '2-4 Months', 'Master precision cuts, global coloring, keratin treatments and luxury bridal hairstyling.', 'gal8.jpg', 'ADVANCED', 'Precision Cuts & Global Coloring|Advanced Chemical Work (Keratin/Botox)|Luxury Bridal Updos & Styling', 'Hi, I want details for the Elite Hair Design Course.', 2);
  insertCourse.run('Master Diploma in Cosmetology', 'Skin, Hair & Nails Expert', '6-12 Months', 'All-in-one course covering skin, hair, nails and salon management — your complete career package.', 'gal15.jpg', 'ALL-IN-ONE', 'Advanced Skin Aesthetics & Facials|Complete Hair Mastery & Chemical|Nail Art, Lash Extensions & Management', 'Hi, I want details for the Master Diploma in Cosmetology.', 3);
  console.log('Courses seeded.');
}

// Seed Gallery if empty
const galleryCount = db.prepare('SELECT COUNT(*) as count FROM gallery').get().count;
if (galleryCount === 0) {
    const insertGallery = db.prepare('INSERT INTO gallery (title, image, display_order) VALUES (?, ?, ?)');
    for(let i=1; i<=18; i++) {
        insertGallery.run(`Gallery Image ${i}`, `gal${i}.jpg`, i);
    }
    console.log('Gallery seeded.');
}

// Seed Vlogs if empty
const vlogCount = db.prepare('SELECT COUNT(*) as count FROM vlogs').get().count;
if (vlogCount === 0) {
    const insertVlog = db.prepare('INSERT INTO vlogs (title, video_url, thumbnail, display_order) VALUES (?, ?, ?, ?)');
    const vlogs = [
        {title: "Vlog 1", url: "sablasinghofficial-20260903-0001.mp4"},
        {title: "Vlog 2", url: "sablasinghofficial-20260903-0002.mp4"},
        {title: "Vlog 3", url: "sablasinghofficial-20260903-0003.mp4"},
        {title: "Vlog 4", url: "sablasinghofficial-20260903-0004.mp4"},
        {title: "Vlog 5", url: "sablasinghofficial-20260903-0005.mp4"},
        {title: "Vlog 6", url: "sablasinghofficial-20260903-0006.mp4"},
        {title: "Vlog 7", url: "sablasinghofficial-20260903-0007.mp4"},
        {title: "Vlog 8", url: "sablasinghofficial-20260903-0008.mp4"},
        {title: "Vlog 9", url: "sablasinghofficial-20260903-0009.mp4"},
        {title: "Vlog 10", url: "sablasinghofficial-20260903-0010.mp4"}
    ];
    vlogs.forEach((v, index) => {
        insertVlog.run(v.title, v.url, '', index + 1);
    });
    console.log('Vlogs seeded.');
}

console.log('Database initialization complete.');
