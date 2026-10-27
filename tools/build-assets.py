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
QUALITY = 52
SHADOW = (0x03, 0x0d, 0x2b)   # sombra: mais escura que --bg, para a foto afundar no fundo
HIGH   = (0xcc, 0xdd, 0xf4)   # luz: azul frio, o "objeto iluminado"

# origem -> (nome de saída, larguras, recorte opcional (l,t,r,b) em fração)
PLAN = {
    # os dois retratos do hero
    "pantex-plant-building-12-44-1-air.png":
        ("duto-1957",       [420, 840], None),
    "ventilation-ductwork-in-a-mechanical-room-of.jpg":
        ("casa-de-maquinas",[420, 840], (0.0, 0.0, 0.93, 0.83)),  # corta o carimbo de data do canto
    # os expostos
    "chiller.jpg":
        ("chiller",         [520, 1040, 1600], None),   # 1600: sangra a largura toda no contato
    "disassembled-chiller-heat-exchanger.jpg":
        ("trocador-aberto", [520, 1040], None),
    "pantex-plant-building-12-44-1-air-2.png":
        ("controles-1957",  [520, 1040], None),
    "kitchen-exhaust-fans.jpg":
        ("exaustao-cozinha",[520, 1040], (0.0, 0.40, 1.0, 1.0)),  # fora o céu: a sala é escura
}

def treat(im):
    """Tratamento único da 'sala escura': duotone entre SHADOW e HIGH.
    A luminância vira posição numa rampa do azul quase preto ao azul claro, com
    uma curva que empurra os meios-tons para baixo. As sombras caem no tom do
    fundo da página, então a foto não precisa de moldura: ela se dissolve."""
    g = ImageEnhance.Contrast(im.convert("L")).enhance(1.18)
    ramp = []
    for ch in range(3):
        lo, hi = SHADOW[ch], HIGH[ch]
        ramp += [int(lo + (hi - lo) * ((i / 255) ** 1.55)) for i in range(256)]
    return g.convert("RGB").point(ramp)


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

    print(f"\n{count} arquivos · {total//1024} KB")
    if count > 25:
        sys.exit(f"ERRO: teto de 25 arquivos estourado ({count})")
    if total > 450 * 1024:
        sys.exit(f"ERRO: teto de 450 KB estourado ({total//1024} KB)")
    print("dentro do orçamento (25 arquivos / 450 KB)")

if __name__ == "__main__":
    main()
