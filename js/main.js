(function () {
  var header = document.querySelector(".header");
  var hero = document.querySelector(".hero");
  var navToggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  var navBackdrop = document.getElementById("nav-backdrop");
  var yearEl = document.getElementById("year");
  var form = document.getElementById("form-contato");
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = lightbox && lightbox.querySelector(".lightbox__img");
  var lightboxCaption = lightbox && lightbox.querySelector(".lightbox__caption");
  var lightboxClose = lightbox && lightbox.querySelector(".lightbox__close");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  if (header && hero) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            header.classList.remove("header--solid");
          } else {
            header.classList.add("header--solid");
          }
        });
      },
      { threshold: 0, rootMargin: "-72px 0px 0px 0px" }
    );
    io.observe(hero);
  }

  function setNavOpen(open) {
    if (nav) {
      nav.classList.toggle("is-open", open);
    }
    if (navToggle) {
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    }
    if (navBackdrop) {
      navBackdrop.hidden = !open;
      navBackdrop.setAttribute("aria-hidden", open ? "false" : "true");
    }
    document.documentElement.classList.toggle("nav-open", open);
  }

  function closeNav() {
    setNavOpen(false);
  }

  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      setNavOpen(!nav.classList.contains("is-open"));
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        closeNav();
      });
    });
  }

  if (navBackdrop) {
    navBackdrop.addEventListener("click", closeNav);
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      var nome = String(fd.get("nome") || "").trim();
      var telefone = String(fd.get("telefone") || "").trim();
      var mensagem = String(fd.get("mensagem") || "").trim();
      var text =
        "Olá! Tenho interesse no apartamento novo frente mar no Residencial Dubai. Quero saber valor, condições e disponibilidade.\n\n" +
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
    if (ev.key !== "Escape") {
      return;
    }
    if (lightbox && !lightbox.hidden) {
      closeLightbox();
      return;
    }
    if (nav && nav.classList.contains("is-open")) {
      closeNav();
    }
  });

  var carousel = document.querySelector("[data-carousel]");
  if (carousel) {
    var track = carousel.querySelector(".gallery-carousel__track");
    var slides = carousel.querySelectorAll(".gallery-carousel__slide");
    var prevBtn = carousel.querySelector(".gallery-carousel__arrow--prev");
    var nextBtn = carousel.querySelector(".gallery-carousel__arrow--next");
    var curEl = carousel.querySelector(".gallery-carousel__current");
    var totalEl = carousel.querySelector(".gallery-carousel__total");
    var n = slides.length;
    var idx = 0;
    var touchStartX = null;

    if (totalEl) {
      totalEl.textContent = String(n);
    }

    function go(delta) {
      idx = (idx + delta + n) % n;
      if (track) {
        track.style.transform = "translateX(-" + idx * 100 + "%)";
      }
      if (curEl) {
        curEl.textContent = String(idx + 1);
      }
    }

    if (prevBtn) {
      prevBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        go(-1);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        go(1);
      });
    }

    carousel.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        go(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        go(1);
      }
    });

    var vp = carousel.querySelector(".gallery-carousel__viewport");
    if (vp) {
      vp.addEventListener(
        "touchstart",
        function (e) {
          if (e.changedTouches && e.changedTouches[0]) {
            touchStartX = e.changedTouches[0].screenX;
          }
        },
        { passive: true }
      );
      vp.addEventListener(
        "touchend",
        function (e) {
          if (touchStartX == null || !e.changedTouches || !e.changedTouches[0]) {
            return;
          }
          var x = e.changedTouches[0].screenX;
          var d = x - touchStartX;
          touchStartX = null;
          if (Math.abs(d) < 50) {
            return;
          }
          if (d < 0) {
            go(1);
          } else {
            go(-1);
          }
        },
        { passive: true }
      );
    }
  }
})();
