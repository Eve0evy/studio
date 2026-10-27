document.documentElement.classList.add("js");

// Sektionen einblenden
const reveal = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add("visible");
      reveal.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll(".reveal").forEach((el) => reveal.observe(el));

// Aktiven Tab beim Scrollen markieren
const links = document.querySelectorAll("nav.tabbed a");
const spy = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      links.forEach((l) =>
        l.classList.toggle("active", l.getAttribute("href") === "#" + e.target.id)
      );
    }
  });
}, { rootMargin: "-40% 0px -55% 0px" });
document.querySelectorAll("main > div[id]").forEach((s) => spy.observe(s));