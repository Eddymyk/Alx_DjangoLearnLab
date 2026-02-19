// Simple JS: highlight posts on hover
document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.post');

    posts.forEach(post => {
        post.addEventListener('mouseenter', () => {
            post.style.backgroundColor = '#e8f5e9';
        });
        post.addEventListener('mouseleave', () => {
            post.style.backgroundColor = 'white';
        });
    });
});
