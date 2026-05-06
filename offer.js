const sections = document.querySelectorAll(".offer-section");
const links = document.querySelectorAll(".offers-menu a");

window.addEventListener("scroll", () => {
  let current = "";

  sections.forEach(section => {
    if (scrollY >= section.offsetTop - 200) {
      current = section.id;
    }
  });

  links.forEach(link => {
    link.classList.remove("active");
    if (link.getAttribute("href") === "#" + current) {
      link.classList.add("active");
    }
  });
});
