document.addEventListener('click', e => {
  if (e.target.closest('header [data-ui^="#"]')) window.scrollTo({ top: 0, behavior: 'instant' });
});


