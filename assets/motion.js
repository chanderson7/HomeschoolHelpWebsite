/* Progressive enhancement: content is visible until a reveal is safely observed. */
(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const cards = [...document.querySelectorAll('.feature')];
  let observer;

  function revealAll() {
    observer?.disconnect();
    cards.forEach(card => card.classList.remove('reveal-pending'));
  }

  if (!preference.matches && 'IntersectionObserver' in window) {
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove('reveal-pending');
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0, rootMargin: '0px 0px -32px 0px' });

    cards.forEach(card => {
      // Never hide content already in view, including restored scroll positions.
      if (card.getBoundingClientRect().top < window.innerHeight) return;
      observer.observe(card);
      card.classList.add('reveal-pending');
    });
  }

  preference.addEventListener('change', event => {
    if (event.matches) revealAll();
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted) revealAll();
  });
})();
