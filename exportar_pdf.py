#!/usr/bin/env python3
"""Exporta um HTML do manual Instituto ISC em PDF (seção 21.6 do brand book).
Uso, na pasta do manual: python3 exportar_pdf.py [arquivo.html]
O arquivo pode estar na pasta do manual ou em qualquer caminho.
Sem Playwright (ex.: agente Hermes), usa o Chrome instalado em modo headless.
"""
import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path

# o arquivo fica na mesma pasta do script, salvo caminho próprio
PASTA = Path(__file__).resolve().parent
NOME = sys.argv[1] if len(sys.argv) > 1 \
    else "brand-book.html"
ARQUIVO = Path(NOME) if Path(NOME).is_file() else PASTA / NOME
ARQUIVO = ARQUIVO.resolve()
SAIDA = ARQUIVO.with_suffix(".pdf")


def com_playwright(sync_playwright):
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(
            viewport={"width": 1200, "height": 900})
        pag.goto(ARQUIVO.as_uri(),
                 wait_until="networkidle")
        # fotos de carregamento tardio entram já
        pag.evaluate(
            "document.querySelectorAll("
            "'img[loading=lazy]')"
            ".forEach(i => i.loading = 'eager')")
        # espera cada foto terminar de carregar
        pag.wait_for_function(
            "Array.from(document.images)"
            ".every(i => i.complete)",
            timeout=60000)
        # fontes e gráficos montados na página
        pag.evaluate("document.fonts.ready")
        pag.wait_for_timeout(1500)
        # print_background=True é obrigatório:
        # sem ele, o preto e o ouro somem.
        # prefer_css_page_size=True respeita a
        # página e as margens do próprio arquivo.
        # Não passe margin: a capa sai sem margem.
        pag.pdf(path=str(SAIDA),
                print_background=True,
                prefer_css_page_size=True)
        nav.close()


def achar_chrome():
    """Chrome ou Chromium já instalado (variável CHROME_PATH primeiro)."""
    candidatos = [os.environ.get("CHROME_PATH", "")]
    candidatos += sorted(glob.glob(
        os.path.expanduser("~/browser-runtime/chrome-*/chrome")), reverse=True)
    candidatos += [shutil.which(n) or "" for n in (
        "chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome")]
    candidatos += [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    for c in candidatos:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


def com_chrome(chrome):
    # Os modelos do manual já pedem print-color-adjust: exact,
    # então o preto e o ouro saem no PDF; o @page de cada arquivo
    # define o tamanho da página.
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--hide-scrollbars", "--no-pdf-header-footer",
           "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=20000",
           f"--print-to-pdf={SAIDA}", ARQUIVO.as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, timeout=180)


try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None

if sync_playwright:
    com_playwright(sync_playwright)
else:
    chrome = achar_chrome()
    if not chrome:
        sys.exit("Sem Playwright e sem Chrome: instale um dos dois "
                 "ou informe o caminho em CHROME_PATH.")
    com_chrome(chrome)
print("PDF gravado em", SAIDA)
