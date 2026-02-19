// Main JavaScript for JobPortal

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    
    // Initialize interactive features
    initInteractivity();
});

function initAnimations() {
    // Add fade-in animation to elements as they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all job cards
    document.querySelectorAll('.job-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

function initInteractivity() {
    // Search functionality
    const searchBtn = document.querySelector('.search-section .btn-primary');
    if (searchBtn) {
        searchBtn.addEventListener('click', function(e) {
            e.preventDefault();
            // Add loading state
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="loading"></span> Searching...';
            this.disabled = true;
            
            // Simulate search (replace with actual search logic)
            setTimeout(() => {
                this.innerHTML = originalText;
                this.disabled = false;
            }, 2000);
        });
    }

    // Apply button functionality
    document.querySelectorAll('.btn-apply').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="loading"></span> Applying...';
            this.disabled = true;
            
            // Simulate application process
            setTimeout(() => {
                this.innerHTML = '<i class="fas fa-check me-1"></i>Applied';
                this.classList.remove('btn-apply');
                this.classList.add('btn-success');
                
                // Show success message
                showNotification('Application submitted successfully!', 'success');
            }, 1500);
        });
    });

    // View button functionality
    document.querySelectorAll('.btn-view').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            // Add view functionality here
            showNotification('Job details will be shown here', 'info');
        });
    });

    // Grid/List view toggle
    document.querySelectorAll('.btn-group button').forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            document.querySelectorAll('.btn-group button').forEach(b => {
                b.classList.remove('active');
            });
            // Add active class to clicked button
            this.classList.add('active');
            
            // Toggle view (implement grid/list view logic here)
            const isGridView = this.querySelector('.fa-th-large');
            if (isGridView) {
                document.querySelectorAll('.job-card').forEach(card => {
                    card.parentElement.className = 'col-lg-6 col-xl-4 mb-4';
                });
            } else {
                document.querySelectorAll('.job-card').forEach(card => {
                    card.parentElement.className = 'col-12 mb-4';
                });
            }
        });
    });
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 3000);
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading states to forms
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="loading"></span> Processing...';
            submitBtn.disabled = true;
        }
    });
});