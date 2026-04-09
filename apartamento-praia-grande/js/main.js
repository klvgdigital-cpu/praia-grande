(function () {
  var header = document.querySelector(".header");
  var navToggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  var yearEl = document.getElementById("year");
  var form = document.getElementById("form-contato");
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = lightbox && lightbox.querySelector(".lightbox__img");
  var lightboxCaption = lightbox && lightbox.querySelector(".lightbox__caption");
  var lightboxClose = lightbox && lightbox.querySelector(".lightbox__close");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  function onScroll() {
    if (!header) return;
    if (window.scrollY > 40) {
      header.classList.add("is-scrolled");
    } else {
      header.classList.remove("is-scrolled");
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      var nome = String(fd.get("nome") || "").trim();
      var telefone = String(fd.get("telefone") || "").trim();
      var mensagem = String(fd.get("mensagem") || "").trim();
      var text =
        "Olá! Tenho interesse no apartamento na Torre A do Residencial Dubai (Praia Grande).\n\n" +
        "Nome: " +
        nome +
        "\n" +
        "WhatsApp: " +
        telefone +
        (mensagem ? "\n\n" + mensagem : "");
      var encoded = encodeURIComponent(text);
      var base = "https://wa.me/5511983905635?text=";
      window.open(base + encoded, "_blank", "noopener,noreferrer");
    });
  }

  function openLightbox(src, caption) {
    if (!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    lightboxImg.alt = caption || "";
    if (lightboxCaption) {
      lightboxCaption.textContent = caption || "";
    }
    lightbox.hidden = false;
    document.body.classList.add("lightbox-open");
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.hidden = true;
    document.body.classList.remove("lightbox-open");
    if (lightboxImg) {
      lightboxImg.src = "";
    }
  }

  document.querySelectorAll("[data-gallery] .gallery__item").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var src = btn.getAttribute("data-src");
      var cap = btn.getAttribute("data-caption") || "";
      if (src) openLightbox(src, cap);
    });
  });

  if (lightboxClose) {
    lightboxClose.addEventListener("click", closeLightbox);
  }

  if (lightbox) {
    lightbox.addEventListener("click", function (ev) {
      if (ev.target === lightbox) closeLightbox();
    });
  }

  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && lightbox && !lightbox.hidden) {
      closeLightbox();
    }
  });
})();
