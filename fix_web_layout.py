from pathlib import Path
import re

INDEX = Path("game/build/web/index.html")


def main() -> None:
    if not INDEX.exists():
        raise FileNotFoundError(f"Expected generated page at {INDEX}")

    html = INDEX.read_text(encoding="utf-8")

    # Pygbag's default template assumes a widescreen 1.77 framebuffer.
    # This game is 900x600, so the correct ratio is 1.5.
    html = html.replace("fb_ar   :  1.77", "fb_ar   :  1.5")

    canvas_css = r"""canvas.emscripten {
            border: 0 none !important;
            background-color: transparent;
            width: min(100vw, calc(100vh * 1.5)) !important;
            height: min(100vh, calc(100vw / 1.5)) !important;
            max-width: 100vw !important;
            max-height: 100vh !important;
            aspect-ratio: 3 / 2 !important;
            z-index: 5;
            padding: 0;
            margin: auto;
            position: fixed;
            inset: 0;
            display: block;
        }"""

    html, replacements = re.subn(
        r"canvas\.emscripten\s*\{.*?\}",
        canvas_css,
        html,
        count=1,
        flags=re.DOTALL,
    )
    if replacements != 1:
        raise RuntimeError("Could not find Pygbag canvas CSS to replace")

    responsive_page_css = r"""
        html, body {
            width: 100%;
            height: 100%;
            min-height: 100%;
            overflow: hidden;
            margin: 0;
            padding: 0;
            background: #7f7f7f;
        }
"""

    if "</style>" not in html:
        raise RuntimeError("Could not find the generated style block")
    html = html.replace("</style>", responsive_page_css + "    </style>", 1)

    INDEX.write_text(html, encoding="utf-8")
    print("Fixed browser canvas to preserve the game's 3:2 aspect ratio")


if __name__ == "__main__":
    main()
