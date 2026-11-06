document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[onsubmit]").forEach(form => {
    form.addEventListener("submit", event => {
      if (form.dataset.confirmed === "false") event.preventDefault();
    });
  });
});
