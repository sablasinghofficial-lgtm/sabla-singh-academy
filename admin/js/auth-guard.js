// Admin Authentication Guard for Sabla Singh Academy
(function() {
    // If not logged in, redirect to login page
    if (!localStorage.getItem('admin_logged_in')) {
        // Only redirect if not already on login.html
        if (!window.location.pathname.endsWith('login.html')) {
            window.location.href = 'login.html';
        }
    }
})();

window.logout = function() {
    localStorage.removeItem('admin_logged_in');
    localStorage.removeItem('admin_user');
    window.location.href = 'login.html';
};
