# -*- coding: utf-8 -*-
"""One-shot sync: replace header, CREA bar (inside main, Home-style), footer, WhatsApp float."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEADER = """  <header>
    <div class="container header-container">
      <a href="{root}" class="logo" aria-label="K Portas® Home">
        <img class="logo-site logo-kportas-inline" src="{p}assets/novo-logo-oficial-kportas.webp" width="600" height="148" alt="K Portas®" loading="eager" fetchpriority="high" decoding="async">
      </a>
      <nav class="main-nav" id="site-nav">
        <ul class="nav-links">
          <li class="nav-item--dropdown">
            <a href="{prod}">Produtos</a>
            <ul class="nav-dropdown" role="menu">
              <li role="none"><a href="{res}" role="menuitem">Residencial</a></li>
              <li role="none"><a href="{com}" role="menuitem">Comercial e Industrial</a></li>
            </ul>
          </li>
          <li class="nav-item--dropdown">
            <a href="{manut}">Serviços</a>
            <ul class="nav-dropdown" role="menu">
              <li role="none"><a href="{manut}" role="menuitem">Manutenção especializada</a></li>
              <li role="none"><a href="{inst}" role="menuitem">Instalação técnica</a></li>
            </ul>
          </li>
          <li><a href="{parc}">Parceiros</a></li>
          <li class="nav-item--dropdown">
            <a href="{insti}">Institucional</a>
            <ul class="nav-dropdown" role="menu">
              <li role="none"><a href="{sobre}" role="menuitem">Sobre a K Portas</a></li>
              <li role="none"><a href="{blog}" role="menuitem">Blog técnico</a></li>
              <li role="none"><a href="{trab}" role="menuitem">Trabalhe conosco</a></li>
            </ul>
          </li>
          <li><a href="{faq}">FAQ</a></li>
          <li><a href="{cont}">Contato</a></li>
        </ul>
      </nav>
      <button class="mobile-menu-icon" id="mobile-menu-toggle" type="button" aria-label="Abrir menu de navegação" aria-controls="site-nav" aria-expanded="false">
        <i class="fa-solid fa-bars" style="color: #F5F5F5; font-size: 1.5rem;"></i>
      </button>
    </div>
  </header>"""

CREA = """  <div class="crea-announcement-bar" role="complementary" aria-label="Responsabilidade técnica CREA">
    <div class="container header-crea-wrap">
      <span class="header-crea-pill">
        Empresa com Responsabilidade Técnica - Registro<span class="crea-wordmark crea-wordmark--hero"><img src="{p}assets/logo-crea.png.webp" alt="Selo CREA-SP da engenharia K Portas® em São Paulo" width="90" height="21" loading="eager" decoding="async"><span class="visually-hidden">CREA</span></span>
      </span>
    </div>
  </div>"""

FOOTER = """  <footer id="contato" class="footer">
    <div class="container">
      
      <div class="cta-footer text-center">
        <h2>Transforme a segurança da sua obra hoje.</h2>
        <a href="https://wa.me/5511993123964" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          <i class="fa-brands fa-whatsapp"></i> Falar com o Engenheiro
        </a>
      </div>

      <div class="contact-grid">
        
        <div class="contact-info">
          
          <div class="contact-block">
            <i class="fa-solid fa-phone contact-icon"></i>
            <div>
              <h3 class="footer-contact__title">Telefones</h3>
              <a href="tel:+551122818474" class="contact-link" style="color: #F5F5F5; text-decoration: none; font-weight: 500; display: block; margin-bottom: 5px;">Fixo: (11) 2281-8474</a>
              <a href="https://wa.me/5511993123964" target="_blank" rel="noopener noreferrer" class="contact-link" style="color: #25D366; text-decoration: none; font-weight: 600; display: block;"><i class="fa-brands fa-whatsapp"></i> WhatsApp: (11) 99312-3964</a>
            </div>
          </div>
          
          <div class="contact-block">
            <i class="fa-solid fa-envelope contact-icon"></i>
            <div>
              <h3 class="footer-contact__title">Canais de Atendimento</h3>
              <a href="mailto:vendas@kportas.com.br" class="contact-link" style="color: #F5F5F5; text-decoration: none; font-weight: 500; display: block; margin-bottom: 5px;">Comercial: vendas@kportas.com.br</a>
              <a href="mailto:compras@kportas.com.br" class="contact-link" style="color: #A0AAB5; text-decoration: none; font-size: 0.9rem; display: block; margin-bottom: 5px;">Fornecedores: compras@kportas.com.br</a>
              <a href="mailto:contato@kportas.com.br" class="contact-link" style="color: #A0AAB5; text-decoration: none; font-size: 0.9rem; display: block;">Administrativo: contato@kportas.com.br</a>
            </div>
          </div>

          <div class="contact-block">
            <i class="fa-solid fa-location-dot contact-icon"></i>
            <div>
              <h3 class="footer-contact__title">Sede Principal</h3>
              <address class="footer-contact__address" style="font-style: normal; color: #F5F5F5; line-height: 1.5; font-weight: 500;">
              Rua Engenheiro Botelho Egas, 117<br>Mandaqui, São Paulo - SP<br>CEP 02416-020
              </address>
            </div>
          </div>
          
          <div class="contact-block">
            <i class="fa-solid fa-map-location-dot contact-icon"></i>
            <div style="color: #A0AAB5; font-size: 0.85rem; line-height: 1.6;">
              <h3 class="footer-contact__title">Cobertura Logística K Portas®</h3>
              <p style="margin:0;">Principais regiões atendidas com instalação: <strong style="color: #F5F5F5;">São Paulo (Capital), Grande ABC, Guarulhos, Campinas, Sorocaba, Jundiaí, Baixada Santista e Litoral Norte.</strong></p>
            </div>
          </div>

          <div class="contact-block">
            <i class="fa-regular fa-clock contact-icon"></i>
            <div style="color: #A0AAB5; font-size: 0.9rem; line-height: 1.6;">
              <h3 class="footer-contact__title">Horário de Funcionamento</h3>
              <span style="color: #F5F5F5; font-weight: 500;">Segunda a Quinta-feira:</span> 08:00 às 18:00<br>
              <span style="color: #F5F5F5; font-weight: 500;">Sexta-feira:</span> 08:00 às 17:00<br>
              <span style="color: #F5F5F5; font-weight: 500;">Intervalo de Almoço:</span> 12:00 às 13:00<br>
              <span style="color: #e74c3c; font-weight: 700; display: inline-block; margin-top: 5px; padding: 2px 6px; border: 1px solid rgba(231,76,60,0.5); border-radius: 4px; font-size: 0.8rem;">Sábado e Domingo: Fechado</span>
            </div>
          </div>
          
          <div class="social-links mt-4">
            <a href="https://www.instagram.com/kportas_/" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
            <a href="#" class="social-icon" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
            <a href="#" class="social-icon" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          </div>

          <nav class="footer-aux-nav" aria-label="Institucional">
            <a href="{foot_trab}">Trabalhe Conosco</a>
            <span class="footer-aux-nav__sep" aria-hidden="true">·</span>
            <a href="{foot_blog}">Blog</a>
            <span class="footer-aux-nav__sep" aria-hidden="true">·</span>
            <a href="{foot_parc}">Parceiros</a>
          </nav>
          
        </div>

        <div class="map-container">
          <div
            class="map-facade"
            data-map-src="https://maps.google.com/maps?q=R.%20Engenheiro%20Botelho%20Egas,%20117%20-%20Mandaqui,%20S%C3%A3o%20Paulo&t=&z=15&ie=UTF8&iwloc=&output=embed"
            style="width:100%;min-height:350px;background:#0A192F;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid rgba(212,175,55,0.3);gap:12px;cursor:pointer;padding:24px;"
            role="button"
            tabindex="0"
            aria-label="Carregar mapa de localização da K Portas® em São Paulo"
          >
            <i class="fa-solid fa-map-location-dot" style="font-size:2.8rem;color:#D4AF37;" aria-hidden="true"></i>
            <p style="color:#F5F5F5;font-family:'Montserrat',sans-serif;font-weight:700;margin:0;text-align:center;font-size:1.05rem;">K Portas® — Mandaqui, São Paulo</p>
            <p style="color:#A0AAB5;font-size:0.9rem;margin:0;text-align:center;">Rua Engenheiro Botelho Egas, 117 · CEP 02416-020</p>
            <span style="background:#D4AF37;color:#061020;padding:10px 22px;border-radius:6px;font-weight:700;font-size:0.88rem;font-family:'Montserrat',sans-serif;margin-top:4px;display:inline-flex;align-items:center;gap:6px;">
              <i class="fa-solid fa-map-pin" aria-hidden="true"></i>Ver Localização no Mapa
            </span>
          </div>
        </div>
        
      </div>
      
      <div class="crea-seal text-center">
        <div class="footer-brand-bar">
          <a href="{root}" class="footer-brand-bar__link" aria-label="K Portas® — início">
            <img src="{p}assets/novo-logo-oficial-kportas.webp" class="footer-logo-kportas" width="600" height="148" alt="K Portas®" loading="lazy" decoding="async">
          </a>
          <div class="footer-brand-bar__middle" aria-hidden="true">
          </div>
          <div class="footer-brand-bar__crea">
            <img src="{p}assets/logo-crea.png.webp" class="footer-logo-crea" width="200" height="46" alt="CREA — Conselho Regional de Engenharia e Agronomia" loading="lazy" decoding="async">
          </div>
        </div>
        <p class="crea-seal__tagline">Responsabilidade técnica e em conformidade com os órgãos competentes da construção civil</p>
        <p style="font-size: clamp(1rem, 1.45vw, 1.08rem); margin: 20px 0 0 0; max-width: 750px; line-height: 1.7;">Especialistas em projeto, fabricação e manutenção de portas de enrolar manuais e automáticas. Atendemos galpões logísticos, comércio de rua e de shopping com porta de aço de enrolar de <strong style="color: #D4AF37; font-weight: 600;">alto padrão</strong> de qualidade e <strong style="color: #D4AF37; font-weight: 600;">extrema durabilidade</strong>.</p>
        <span style="font-size: clamp(0.98rem, 1.3vw, 1.05rem); margin-top: 5px;">K Portas® é uma marca registrada. Excelência em engenharia de portas de aço. <br> © 2026 Todos os direitos reservados.</span>
      </div>

    </div>
  </footer>

  <a href="https://wa.me/5511993123964?text=Olá,%20estou%20no%20site%20da%20K%20Portas%C2%AE%20e%20gostaria%20de%20falar%20com%20um%20consultor%20técnico." target="_blank" rel="noopener noreferrer" class="whatsapp-float" aria-label="Falar no WhatsApp">
    <i class="fa-brands fa-whatsapp"></i>
  </a>"""

# Per-file nav + paths (matches index.html Home semantics)
CONFIG = {
    "produtos/index.html": dict(
        p="../", root="../",
        prod="./", res="residencial/", com="comercial-e-industrial/",
        manut="../servicos/manutencao-em-sp/", inst="../servicos/instalacao-tecnica/",
        parc="../parcerias/serralheiro/", insti="../institucional/trabalhe-conosco/",
        sobre="../index.html#diferencial", blog="../institucional/blog/", trab="../institucional/trabalhe-conosco/",
        faq="../index.html#faq", cont="../index.html#contato",
        foot_trab="../institucional/trabalhe-conosco/", foot_blog="../institucional/blog/", foot_parc="../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "produtos/residencial/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../../servicos/manutencao-em-sp/", inst="../../servicos/instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="../../institucional/trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="../../institucional/blog/", trab="../../institucional/trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../../institucional/trabalhe-conosco/", foot_blog="../../institucional/blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "produtos/comercial-e-industrial/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../../servicos/manutencao-em-sp/", inst="../../servicos/instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="../../institucional/trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="../../institucional/blog/", trab="../../institucional/trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../../institucional/trabalhe-conosco/", foot_blog="../../institucional/blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "servicos/manutencao-em-sp/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="./", inst="../instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="../../institucional/trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="../../institucional/blog/", trab="../../institucional/trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../../institucional/trabalhe-conosco/", foot_blog="../../institucional/blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=True,
    ),
    "servicos/instalacao-tecnica/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../manutencao-em-sp/", inst="./",
        parc="../../parcerias/serralheiro/", insti="../../institucional/trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="../../institucional/blog/", trab="../../institucional/trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../../institucional/trabalhe-conosco/", foot_blog="../../institucional/blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "parcerias/serralheiro/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../../servicos/manutencao-em-sp/", inst="../../servicos/instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="../../institucional/trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="../../institucional/blog/", trab="../../institucional/trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../../institucional/trabalhe-conosco/", foot_blog="../../institucional/blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "institucional/trabalhe-conosco/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../../servicos/manutencao-em-sp/", inst="../../servicos/instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="./",
        sobre="../../index.html#diferencial", blog="../blog/", trab="./",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="./", foot_blog="../blog/", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "institucional/blog/index.html": dict(
        p="../../", root="../../",
        prod="../../produtos/", res="../../produtos/residencial/", com="../../produtos/comercial-e-industrial/",
        manut="../../servicos/manutencao-em-sp/", inst="../../servicos/instalacao-tecnica/",
        parc="../../parcerias/serralheiro/", insti="../trabalhe-conosco/",
        sobre="../../index.html#diferencial", blog="./", trab="../trabalhe-conosco/",
        faq="../../index.html#faq", cont="../../index.html#contato",
        foot_trab="../trabalhe-conosco/", foot_blog="./", foot_parc="../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
    "institucional/blog/portas-de-aco-automaticas-guia-2026/index.html": dict(
        p="../../../", root="../../../",
        prod="../../../produtos/", res="../../../produtos/residencial/", com="../../../produtos/comercial-e-industrial/",
        manut="../../../servicos/manutencao-em-sp/", inst="../../../servicos/instalacao-tecnica/",
        parc="../../../parcerias/serralheiro/", insti="../../trabalhe-conosco/",
        sobre="../../../index.html#diferencial", blog="../index.html", trab="../../trabalhe-conosco/",
        faq="../../../index.html#faq", cont="../../../index.html#contato",
        foot_trab="../../trabalhe-conosco/", foot_blog="../", foot_parc="../../../parcerias/serralheiro/",
        inject_main_wrapper=False,
    ),
}


def fmt(template: str, kw: dict) -> str:
    keys = {k: kw[k] for k in [
        "p", "root", "prod", "res", "com", "manut", "inst", "parc", "insti",
        "sobre", "blog", "trab", "faq", "cont",
        "foot_trab", "foot_blog", "foot_parc",
    ]}
    return template.format(**keys)


def sync_file(rel: str) -> None:
    kw = {k: v for k, v in CONFIG[rel].items() if k != "inject_main_wrapper"}
    inject = CONFIG[rel]["inject_main_wrapper"]
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")

    text = re.sub(r"<header>.*?</header>", fmt(HEADER, kw), text, count=1, flags=re.DOTALL)

    text = re.sub(
        r"\s*<aside class=\"crea-announcement-bar\"[^>]*>.*?</aside>\s*",
        "\n\n",
        text,
        count=1,
        flags=re.DOTALL,
    )

    crea_html = fmt(CREA, kw)

    if inject:
        text = re.sub(
            r"(</header>\s*)",
            r"\1\n  <main id=\"conteudo-principal\">\n" + crea_html + "\n",
            text,
            count=1,
        )
        text = re.sub(
            r"(\s*)<footer id=\"contato\"",
            r"\n  </main>\n\n\1<footer id=\"contato\"",
            text,
            count=1,
        )
    else:
        if 'id="conteudo-principal"' not in text:
            raise RuntimeError(f"{rel}: expected <main id=\"conteudo-principal\"> or inject_main_wrapper")
        marker = '<main id="conteudo-principal">'
        if text.count(marker) != 1:
            raise RuntimeError(f"{rel}: single main marker expected")
        after_main = text.split(marker, 1)[1][:1200]
        if "crea-announcement-bar" in after_main:
            pass
        else:
            text = text.replace(marker, marker + "\n" + crea_html, 1)

    text = re.sub(
        r"<footer id=\"contato\" class=\"footer\">[\s\S]*?</footer>\s*<a[^>]*class=\"whatsapp-float\"[^>]*>[\s\S]*?</a>",
        fmt(FOOTER, kw),
        text,
        count=1,
    )

    path.write_text(text, encoding="utf-8")
    print("OK", rel)


def main():
    for rel in CONFIG:
        sync_file(rel)


if __name__ == "__main__":
    main()
