# Waifu Heart Rush 💖🐉

A tiny Pygame romance-arcade game made during summer school in Milan.

Catch hearts, dodge red flags, travel through alternate realities, and defeat the dragon guarding each new world with heart-magic.

## Play in your browser

Once GitHub Pages is enabled, the game will be available here:

**https://annethecodegirl.github.io/waifu-heart-rush/**

The GitHub Actions workflow automatically rebuilds and republishes the browser version whenever the `main` branch changes.

## Controls

### Normal levels

- **A / D** or **arrow keys** — move
- **N** — jump toward the next reality
- **B** — summon a practice dragon
- **F11** — toggle fullscreen in the desktop version
- **Esc** — quit the desktop version

### Dragon battles

- **A / D** or **arrow keys** — move
- **Space** or **Z** — cast heartfire

## Realities

- Bubblegum Daydream
- Basement Techno
- Milan Afterglow
- Midnight Bookstore
- Last Train Home
- Neon Rooftop
- Dragon Cathedral

## Run locally

Install the dependency:

```bash
py -m pip install -r requirements.txt
```

Then run the uploaded source file:

```bash
py main
```

## Browser build

The game is packaged for the web with [pygbag](https://github.com/pygame-web/pygbag). The `webify.py` script converts the desktop loop into an async browser-compatible loop during deployment, then GitHub Actions publishes the generated WebAssembly build to GitHub Pages.
