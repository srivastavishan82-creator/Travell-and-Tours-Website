const sections = document.querySelectorAll(".flight-section");
const links = document.querySelectorAll(".flight-menu a");

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
