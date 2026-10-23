# Best Meme of the Week: Current Events (Oct 16-23, 2026)

## The event

On **2026-10-20**, Reuters reported that Anthropic's net loss widened to
**$80.7 billion** in the first half of 2026, up from $13 billion a year earlier,
according to a draft IPO prospectus. The headline number is almost entirely an
accounting artefact: it includes a **$72 billion non-cash charge** reflecting an
*increase* in the estimated fair value of bonds convertible into Anthropic
shares. Revenue over the same period was about **$16.3 billion**.

Source, published 2026-10-20:

- https://www.reuters.com/business/anthropic-recorded-net-loss-over-80-billion-first-half-this-year-wsj-reports-2026-10-20/
- https://www.globalbankingandfinance.com/anthropic-logged-net-loss-over-80-billion-first-half-2026/

## The joke, in one sentence

A company whose convertible bonds became so valuable that the accounting
recorded the increase as the largest loss in startup history, filed as a
statement of operations with the two line items drawn to scale.

## Why it is drawn this way

The meme is a plain accounting statement rather than a caption over an image,
because the joke *is* the itemisation. Two bars, to scale: `$72.0B` of
fair-value charge, and `$8.7B` of everything else. The second bar is 12% of the
first, and that ratio is the whole point. The punchline text is the mechanism
stated flatly, in the order an accountant would explain it.

The only arithmetic on the image is `80.7 - 72.0 = 8.7`. Nothing is rounded
up, no number is invented, and the footer says so.

## Rules compliance

| Rule | How it is met |
|---|---|
| SFW, safe to post publicly | No hate, harassment, sexual content, gore, or reference to a tragedy or its victims. |
| Original work only | Every pixel is drawn by `make_meme.py` from primitives - rectangles, lines, and text in DejaVu Sans Mono (a freely licensed system font). No stock image, no existing template, no copyrighted footage, logo, or music. There is no source image at all. |
| No real people's faces, voices, likenesses | The image contains no people. It is a financial statement. The company name appears as the account holder, which is a company, not a person. |
| Not misleading | It is labelled satire in the footer, and every figure is the figure Reuters reported. No fake headline is presented as real news. |
| One place per wallet | One entry. |
| No secrets | No keys, tokens, or private data in any file. |

## Files

- `meme.png` - 1080x1350, RGB, the entry.
- `make_meme.py` - the generator. `python3 make_meme.py` reproduces the PNG byte-for-byte.
- `manifest.json` - disclosure.
