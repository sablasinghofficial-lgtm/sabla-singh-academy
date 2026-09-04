const express = require('express');
const session = require('express-session');
const Database = require('better-sqlite3');
const bcrypt = require('bcrypt');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 3000;
const db = new Database('db/database.sqlite');

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'admin'))); // Serve admin panel files
app.use(express.static(path.join(__dirname, 'uploads'))); // Serve uploaded files
app.use(express.static(path.join(__dirname, ''))); // Serve existing public assets from root

app.use(session({
    secret: 'sablasingh_academy_super_secret',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 24 * 60 * 60 * 1000 } // 24 hours
}));

// Auth Middleware
const requireAuth = (req, res, next) => {
    if (req.session.userId) {
        next();
    } else {
        res.status(401).json({ error: 'Unauthorized' });
    }
};

const requireAuthRedirect = (req, res, next) => {
    if (req.session.userId) {
        next();
    } else {
        res.redirect('/admin/login.html');
    }
};

// Protect admin HTML routes (except login)
app.use('/admin', (req, res, next) => {
    if (req.path === '/login.html' || req.path.startsWith('/css') || req.path.startsWith('/js')) {
        next();
    } else {
        requireAuthRedirect(req, res, next);
    }
});

// --- API ROUTES --- //

// Auth API
app.post('/api/auth/login', (req, res) => {
    const { username, password } = req.body;
    const admin = db.prepare('SELECT * FROM admin WHERE username = ?').get(username);
    
    if (admin && bcrypt.compareSync(password, admin.password)) {
        req.session.userId = admin.id;
        req.session.username = admin.username;
        res.json({ success: true, message: 'Logged in successfully' });
    } else {
        res.status(401).json({ success: false, message: 'Invalid credentials' });
    }
});

app.post('/api/auth/logout', (req, res) => {
    req.session.destroy();
    res.json({ success: true, message: 'Logged out successfully' });
});

app.get('/api/auth/me', requireAuth, (req, res) => {
    res.json({ username: req.session.username });
});

// Enquiries API (Public & Protected)
app.post('/api/enquiry', (req, res) => {
    try {
        const { name, phone, email, interested_in, message } = req.body;
        const stmt = db.prepare('INSERT INTO queries (name, phone, email, interested_in, message) VALUES (?, ?, ?, ?, ?)');
        stmt.run(name, phone, email, interested_in, message);
        res.json({ success: true, message: 'Enquiry submitted successfully' });
    } catch (error) {
        res.status(500).json({ success: false, message: error.message });
    }
});

app.get('/api/admin/queries', requireAuth, (req, res) => {
    const queries = db.prepare('SELECT * FROM queries ORDER BY created_at DESC').all();
    res.json(queries);
});

app.put('/api/admin/queries/:id/status', requireAuth, (req, res) => {
    const { status } = req.body;
    db.prepare('UPDATE queries SET status = ? WHERE id = ?').run(status, req.params.id);
    res.json({ success: true });
});

app.delete('/api/admin/queries/:id', requireAuth, (req, res) => {
    db.prepare('DELETE FROM queries WHERE id = ?').run(req.params.id);
    res.json({ success: true });
});

// Stats API
app.get('/api/admin/stats', requireAuth, (req, res) => {
    const services = db.prepare('SELECT COUNT(*) as count FROM services').get().count;
    const courses = db.prepare('SELECT COUNT(*) as count FROM courses').get().count;
    const gallery = db.prepare('SELECT COUNT(*) as count FROM gallery').get().count;
    const vlogs = db.prepare('SELECT COUNT(*) as count FROM vlogs').get().count;
    const queries = db.prepare('SELECT COUNT(*) as count FROM queries').get().count;
    const newQueries = db.prepare("SELECT COUNT(*) as count FROM queries WHERE status = 'New'").get().count;
    
    res.json({ services, courses, gallery, vlogs, queries, newQueries });
});

// Services CRUD
app.get('/api/admin/services', requireAuth, (req, res) => res.json(db.prepare('SELECT * FROM services ORDER BY display_order').all()));
app.post('/api/admin/services', requireAuth, (req, res) => {
    const { title, subtitle, description, image, icon, features, whatsapp_text, display_order } = req.body;
    db.prepare('INSERT INTO services (title, subtitle, description, image, icon, features, whatsapp_text, display_order) VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
      .run(title, subtitle, description, image, icon, features, whatsapp_text, display_order || 0);
    res.json({ success: true });
});
app.put('/api/admin/services/:id', requireAuth, (req, res) => {
    const { title, subtitle, description, image, icon, features, whatsapp_text, display_order, status } = req.body;
    db.prepare('UPDATE services SET title=?, subtitle=?, description=?, image=?, icon=?, features=?, whatsapp_text=?, display_order=?, status=? WHERE id=?')
      .run(title, subtitle, description, image, icon, features, whatsapp_text, display_order, status, req.params.id);
    res.json({ success: true });
});
app.delete('/api/admin/services/:id', requireAuth, (req, res) => {
    db.prepare('DELETE FROM services WHERE id=?').run(req.params.id);
    res.json({ success: true });
});

// Courses CRUD
app.get('/api/admin/courses', requireAuth, (req, res) => res.json(db.prepare('SELECT * FROM courses ORDER BY display_order').all()));
app.post('/api/admin/courses', requireAuth, (req, res) => {
    const { title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order } = req.body;
    db.prepare('INSERT INTO courses (title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)')
      .run(title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order || 0);
    res.json({ success: true });
});
app.put('/api/admin/courses/:id', requireAuth, (req, res) => {
    const { title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order, status } = req.body;
    db.prepare('UPDATE courses SET title=?, subtitle=?, duration=?, description=?, image=?, badge=?, features=?, whatsapp_text=?, display_order=?, status=? WHERE id=?')
      .run(title, subtitle, duration, description, image, badge, features, whatsapp_text, display_order, status, req.params.id);
    res.json({ success: true });
});
app.delete('/api/admin/courses/:id', requireAuth, (req, res) => {
    db.prepare('DELETE FROM courses WHERE id=?').run(req.params.id);
    res.json({ success: true });
});


// Vlogs CRUD
app.get('/api/admin/vlogs', requireAuth, (req, res) => res.json(db.prepare('SELECT * FROM vlogs ORDER BY display_order').all()));
app.post('/api/admin/vlogs', requireAuth, (req, res) => {
    const { title, video_url, thumbnail, display_order } = req.body;
    db.prepare('INSERT INTO vlogs (title, video_url, thumbnail, display_order) VALUES (?, ?, ?, ?)')
      .run(title, video_url, thumbnail, display_order || 0);
    res.json({ success: true });
});
app.put('/api/admin/vlogs/:id', requireAuth, (req, res) => {
    const { title, video_url, thumbnail, display_order, status } = req.body;
    db.prepare('UPDATE vlogs SET title=?, video_url=?, thumbnail=?, display_order=?, status=? WHERE id=?')
      .run(title, video_url, thumbnail, display_order, status, req.params.id);
    res.json({ success: true });
});
app.delete('/api/admin/vlogs/:id', requireAuth, (req, res) => {
    db.prepare('DELETE FROM vlogs WHERE id=?').run(req.params.id);
    res.json({ success: true });
});

// Redirect root to admin dashboard
app.get('/', (req, res) => res.redirect('/admin/dashboard.html'));
app.get('/admin', (req, res) => res.redirect('/admin/dashboard.html'));

app.listen(port, () => {
    console.log(`Admin Panel API server running at http://localhost:${port}`);
});



