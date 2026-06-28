// main.js — students will add JavaScript here as features are built

// Demo modal
(function () {
    const overlay = document.getElementById('demo-modal');
    if (!overlay) return;

    const iframe = document.getElementById('demo-iframe');
    const openBtn = document.getElementById('open-demo-modal');
    const closeBtn = document.getElementById('close-demo-modal');

    function openModal() {
        iframe.src = iframe.dataset.src;
        overlay.classList.add('is-open');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        overlay.classList.remove('is-open');
        iframe.src = '';
        document.body.style.overflow = '';
    }

    openBtn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal();
    });

    closeBtn.addEventListener('click', closeModal);

    overlay.addEventListener('click', function (e) {
        if (e.target === overlay) closeModal();
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeModal();
    });
}());
