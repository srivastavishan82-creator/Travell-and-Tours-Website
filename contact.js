const pages = document.querySelectorAll(".page");
const navItems = document.querySelectorAll(".contact-nav span");

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        pages.forEach(p => p.classList.remove("active"));
        entry.target.classList.add("active");

        navItems.forEach(n => n.classList.remove("active"));
        document
          .querySelector(`[data-target="${entry.target.classList[1]}"]`)
          .classList.add("active");
      }
    });
  },
  { threshold: 0.6 }
);

pages.forEach(page => observer.observe(page));

navItems.forEach(item => {
  item.addEventListener("click", () => {
    document
      .querySelector(`.${item.dataset.target}`)
      .scrollIntoView({ behavior: "smooth" });
  });
});
