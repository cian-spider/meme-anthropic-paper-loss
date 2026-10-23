#!/usr/bin/env python3
"""Render the 'Best Meme of the Week' entry: an accounting statement.

Original work. Every pixel is drawn here from primitives; no template, no
stock image, no third-party asset, no faces. Figures come from the Reuters
report of 2026-10-20 (net loss $80.7B, of which a ~$72B non-cash fair-value
charge on convertible bonds) and the only arithmetic performed is the
subtraction 80.7 - 72.0 = 8.7, labelled as "the rest".

    python3 zero/assets/meme/make_meme.py
"""

from __future__ import annotations

import pathlib

from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "meme.png"

W, H = 1080, 1350
INK = (18, 18, 20)
PAPER = (247, 244, 236)
RED = (176, 32, 32)
GREY = (110, 108, 104)
GREEN = (26, 92, 58)

FONTS = "/usr/share/fonts/truetype/dejavu/"
MONO_B = FONTS + "DejaVuSansMono-Bold.ttf"
MONO = FONTS + "DejaVuSansMono.ttf"
MONO_O = FONTS + "DejaVuSansMono-Oblique.ttf"


def f(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- letterhead -----------------------------------------------------
    d.rectangle([0, 0, W, 12], fill=INK)
    m = 72

    d.text((m, 58), "STATEMENT OF OPERATIONS", font=f(MONO_B, 26), fill=INK)
    d.text((W - m - d.textlength("H1 2026", font=f(MONO_B, 26)), 58),
           "H1 2026", font=f(MONO_B, 26), fill=INK)
    d.line([m, 104, W - m, 104], fill=INK, width=3)

    d.text((m, 126), "ACCOUNT HOLDER", font=f(MONO, 20), fill=GREY)
    d.text((m, 152), "ANTHROPIC  (draft IPO prospectus, via WSJ)", font=f(MONO_B, 24), fill=INK)

    # ---- the headline number --------------------------------------------
    d.text((m, 214), "NET LOSS", font=f(MONO_B, 24), fill=GREY)
    big = f(MONO_B, 132)
    d.text((m - 6, 244), "-$80.7B", font=big, fill=RED)
    d.text((m, 396), "in six months, against a $13B loss the year before.",
           font=f(MONO, 22), fill=INK)
    d.text((m, 424), "revenue over the same period: $16.3B, and rising.",
           font=f(MONO, 22), fill=INK)

    d.line([m, 470, W - m, 470], fill=INK, width=3)
    d.text((m, 488), "ITEMISED", font=f(MONO_B, 22), fill=GREY)

    # ---- the two bars ----------------------------------------------------
    bar_x, bar_w = m, W - 2 * m
    rows = [
        ("fair-value charge on convertible bonds",
         "$72.0B", 1.00, RED,
         "the bonds became MORE valuable, so the paper loss grew"),
        ("everything else",
         "$8.7B", 8.7 / 72.0, INK,
         "this is the part that resembles a loss"),
    ]
    y = 530
    for label, amount, frac, colour, sub in rows:
        d.text((bar_x, y), label, font=f(MONO_B, 26), fill=INK)
        d.text((W - m - d.textlength(amount, font=f(MONO_B, 26)), y), amount,
               font=f(MONO_B, 26), fill=colour)
        by = y + 40
        d.rectangle([bar_x, by, bar_x + bar_w, by + 54], outline=INK, width=3)
        fill_w = max(10, int(bar_w * frac))
        d.rectangle([bar_x + 3, by + 3, bar_x + 3 + fill_w - 6, by + 51], fill=colour)
        d.text((bar_x, by + 66), sub, font=f(MONO, 19), fill=GREY)
        y = by + 132

    # ---- the punchline ---------------------------------------------------
    d.line([m, y + 6, W - m, y + 6], fill=INK, width=3)

    lines = [
        ("they sold bonds convertible into their own shares.", INK, MONO),
        ("the shares went up.", INK, MONO),
        ("the bonds therefore went up.", INK, MONO),
        ("so the accounting says: a loss of $80.7B.", INK, MONO),
    ]
    y += 34
    for text, colour, font_path in lines:
        d.text((m, y), text, font=f(font_path, 27), fill=colour)
        y += 38

    y += 18
    d.text((m, y), "record revenue. record loss. the same six months.", font=f(MONO_O, 27), fill=INK)
    d.text((m, y + 38), "one number is cash. the other is not.", font=f(MONO_B, 27), fill=RED)

    # ---- footer ----------------------------------------------------------
    d.line([m, H - 148, W - m, H - 148], fill=INK, width=3)
    d.text((m, H - 132), "SOURCE  reuters.com, 20 oct 2026  ·  $72B of it is non-cash",
           font=f(MONO, 19), fill=GREY)
    d.text((m, H - 106), "this image is satire. the arithmetic is not: 80.7 - 72.0 = 8.7",
           font=f(MONO, 19), fill=GREY)
    stamp = f(MONO_B, 22)
    d.text((m, H - 66), "ORIGINAL WORK  ·  NO TEMPLATE  ·  NO FACES", font=stamp, fill=GREEN)
    d.rectangle([0, H - 12, W, H], fill=INK)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {img.size[0]}x{img.size[1]} {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
