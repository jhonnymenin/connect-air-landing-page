#!/usr/bin/env python3
"""Deriva as imagens da página a partir de assets/ (originais baixados, creditados).

Regra do projeto (docs/05-PIPELINE-DE-ASSETS.md):
  - cada original gera NO MÁXIMO as larguras listadas em PLAN
  - o destino é LIMPO antes de escrever: arquivo órfão é impossível
  - nomes determinísticos: <assunto>-<largura>.webp
Rodar:  python3 tools/build-assets.py
"""
import os, shutil, sys
from PIL import Image, ImageEnhance, ImageChops

SRC, OUT = "assets", "src/assets/img"
QUALITY = 48
SHADOW = (0x08, 0x1c, 0x4d)   # sombra: o azul profundo da marca
HIGH   = (0xf4, 0xf8, 0xfd)   # luz: quase o papel da página

# origem -> (nome de saída, larguras, recorte opcional (l,t,r,b) em fração)
PLAN = {
    # os dois retratos do hero
    "pantex-plant-building-12-44-1-air.png":
        ("duto-1957",       [420, 760], None),
    "ventilation-ductwork-in-a-mechanical-room-of.jpg":
        ("casa-de-maquinas",[420, 760], (0.0, 0.0, 0.93, 0.83)),  # corta o carimbo de data do canto
    # os expostos
    "chiller.jpg":
        ("chiller",         [520, 1040, 1440], None),   # 1600: sangra a largura toda no contato
    "disassembled-chiller-heat-exchanger.jpg":
        ("trocador-aberto", [520, 920], None),
    "pantex-plant-building-12-44-1-air-2.png":
        ("controles-1957",  [520, 1040], None),
    "kitchen-exhaust-fans.jpg":
        ("exaustao-cozinha",[520, 920], (0.0, 0.40, 1.0, 1.0)),  # fora o céu: a sala é escura
}

def treat(im):
    """Tratamento único: duotone discreto entre o azul profundo da marca e o
    papel da página. Numa página clara a foto não precisa afundar no fundo —
    precisa ler como fotografia. Então a rampa é quase linear e as luzes vão
    até perto do branco, unindo o conjunto sem apagá-lo."""
    g = ImageEnhance.Contrast(im.convert("L")).enhance(1.06)
    ramp = []
    for ch in range(3):
        lo, hi = SHADOW[ch], HIGH[ch]
        ramp += [int(lo + (hi - lo) * ((i / 255) ** 0.92)) for i in range(256)]
    return g.convert("RGB").point(ramp)


# Logos de parceiros e credenciamento: cor original, altura normalizada,
# derivada única em WebP com transparência. Não passam pelo duotone.
LOGOS = {
    "1_logo_cacau_show.png":        "parceiro-cacau-show",
    "2_logo_jtc_distribuidora.png": "parceiro-jtc",
    "3_logo_oswaldo_cruz.png":      "parceiro-oswaldo-cruz",
    "4_logo_utc_engenharia.png":    "parceiro-utc",
    "5_logo_ykp.png":               "parceiro-ykp",
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
    if count > 25:
        sys.exit(f"ERRO: teto de 25 arquivos estourado ({count})")
    if total > 500 * 1024:
        sys.exit(f"ERRO: teto de 500 KB estourado ({total//1024} KB)")
    print("dentro do orçamento (25 arquivos / 500 KB)")

if __name__ == "__main__":
    main()
