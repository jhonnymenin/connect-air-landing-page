#!/usr/bin/env python3
"""Deriva as imagens da página a partir de assets/ (originais baixados, creditados).

Regra do projeto (docs/05-PIPELINE-DE-ASSETS.md):
  - cada original gera NO MÁXIMO as larguras listadas em PLAN
  - o destino é LIMPO antes de escrever: arquivo órfão é impossível
  - nomes determinísticos: <assunto>-<largura>.webp
Rodar:  python3 tools/build-assets.py
"""
import os, shutil, sys

try:
    from PIL import Image, ImageEnhance, ImageChops
except ImportError:
    sys.exit(
        "Pillow não encontrado em " + sys.executable + ".\n"
        "O python3 padrão da máquina pode ter mudado de versão. Rode com um que\n"
        "tenha Pillow, ou instale:  " + sys.executable + " -m pip install Pillow"
    )

SRC, OUT = "assets", "src/assets/img"
QUALITY = 46

# Teto próprio de peso das imagens. Subiu de 500 para 560 KB em 06/11/2026, ao
# trocar o duotone azul pela cor original: cor custa mais bytes que uma rampa de
# um canal só, e baixar a qualidade até caber nos 500 deixava artefato visível
# nas fotos coloridas. A página inteira fica em ~665 KB, contra o teto
# contratual de 1,5 MB. Não é licença para crescer: é o custo declarado de uma
# decisão de direção. Quando as fotos do Márcio chegarem, as de acervo saem e
# este teto volta para 500.
MAX_FILES, MAX_KB = 25, 450

# origem -> (nome de saída, larguras, recorte opcional (l,t,r,b) em fração)
PLAN = {
    "ventilation-ductwork-in-a-mechanical-room-of.jpg":
        ("casa-de-maquinas",[420, 760], (0.0, 0.0, 0.93, 0.83)),  # corta o carimbo de data do canto
    # os expostos
    "chiller.jpg":
        ("chiller",         [520, 1040], None),
    "disassembled-chiller-heat-exchanger.jpg":
        ("trocador-aberto", [520, 920], None),
    "kitchen-exhaust-fans.jpg":
        ("exaustao-cozinha",[520, 920], (0.0, 0.40, 1.0, 1.0)),  # fora o céu: a sala é escura
}

def treat(im):
    """Cor original. O duotone azul existia para unir fotografias de origens
    diferentes numa página que não tinha nenhuma foto do cliente; ele custava a
    própria cor da imagem e deixava a página monocromática. Agora a foto entra
    como ela é, com um empurrão discreto de contraste e saturação para aguentar
    a compressão — nada que invente o que não estava lá."""
    im = ImageEnhance.Contrast(im).enhance(1.04)
    return ImageEnhance.Color(im).enhance(1.06)


# Logos de parceiros e credenciamento: cor original, altura normalizada,
# derivada única em WebP com transparência. Não passam pelo duotone.
LOGOS = {
    "1_logo_cacau_show.png":        "parceiro-cacau-show",
    "2_logo_jtc_distribuidora.png": "parceiro-jtc",
    "3_logo_oswaldo_cruz.png":      "parceiro-oswaldo-cruz",
    "4_logo_utc_engenharia.png":    "parceiro-utc",
    "5_logo_ykp.png":               "parceiro-ykp",
    # entregue pelo cliente em 05/11/2026, depois da primeira leva
    "logo_wolfmann_construtora.png": "parceiro-wolfmann",
}
LOGO_DIR = ("Connect-Air/CONNECT•AIR/02 - DOC SITE + ASSESTS/02 - LOGO PARCEIROS")
CRT_SRC  = ("Connect-Air/CONNECT•AIR/02 - DOC SITE + ASSESTS/"
            "03 - ASSETS AVALIAÇÃO DO GOOGLE/logo_sistema_cft_crt.png")
LOGO_H = 120   # 60px renderizado, 2x


def build_logos(out):
    n = total = 0
    for src, stem in LOGOS.items():
        path = os.path.join(LOGO_DIR, src)
        if not os.path.exists(path):
            sys.exit(f"logo ausente: {path}")
        im = Image.open(path).convert("RGBA")
        w = round(im.width * LOGO_H / im.height)
        im = im.resize((w, LOGO_H), Image.LANCZOS)
        dest = os.path.join(out, f"{stem}.webp")
        im.save(dest, "WEBP", quality=78, method=6)
        total += os.path.getsize(dest); n += 1
        print(f"  {stem}.webp  {w}x{LOGO_H}  {os.path.getsize(dest)//1024} KB")
    im = Image.open(CRT_SRC).convert("RGBA")
    im.thumbnail((320, 320), Image.LANCZOS)
    dest = os.path.join(out, "selo-cft-crt.webp")
    im.save(dest, "WEBP", quality=78, method=6)
    total += os.path.getsize(dest); n += 1
    print(f"  selo-cft-crt.webp  {im.width}x{im.height}  {os.path.getsize(dest)//1024} KB")
    return n, total


def main():
    if not os.path.isdir(SRC):
        sys.exit(f"falta {SRC}/")
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)          # limpeza destrutiva: sem órfãos
    os.makedirs(OUT)

    total = count = 0
    for src_name, (stem, widths, crop) in PLAN.items():
        path = os.path.join(SRC, src_name)
        if not os.path.exists(path):
            sys.exit(f"original ausente: {path}")
        im = treat(Image.open(path).convert("RGB"))
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
        for w in widths:
            d = im.copy()
            d.thumbnail((w, w * 4), Image.LANCZOS)
            out = os.path.join(OUT, f"{stem}-{w}.webp")
            d.save(out, "WEBP", quality=QUALITY, method=6)
            n = os.path.getsize(out)
            total += n; count += 1
            print(f"  {stem}-{w}.webp  {d.width}x{d.height}  {n//1024} KB")

    ln, lt = build_logos(OUT)
    count += ln; total += lt

    print(f"\n{count} arquivos · {total//1024} KB")
    if count > MAX_FILES:
        sys.exit(f"ERRO: teto de {MAX_FILES} arquivos estourado ({count})")
    if total > MAX_KB * 1024:
        sys.exit(f"ERRO: teto de {MAX_KB} KB estourado ({total//1024} KB)")
    print(f"dentro do orçamento ({MAX_FILES} arquivos / {MAX_KB} KB)")

if __name__ == "__main__":
    main()
