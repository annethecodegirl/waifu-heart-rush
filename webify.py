from pathlib import Path

SOURCE = Path("main")
OUTPUT_DIR = Path("game")
OUTPUT = OUTPUT_DIR / "main.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(
            f"Could not find {label}; the uploaded source layout may have changed."
        )
    return text.replace(old, new, 1)


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(
            "Expected the uploaded game source at repository root as a file named 'main'."
        )

    code = SOURCE.read_text(encoding="utf-8")

    code = replace_once(
        code,
        "import math\n",
        "import asyncio\nimport math\n",
        "the import section",
    )
    code = replace_once(
        code,
        "def main():\n",
        "async def main():\n",
        "the main function",
    )
    code = replace_once(
        code,
        "    fullscreen = True\n    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)\n",
        "    fullscreen = sys.platform != 'emscripten'\n"
        "    if fullscreen:\n"
        "        display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)\n"
        "    else:\n"
        "        # Browsers own the outer fullscreen/window controls.\n"
        "        display = pygame.display.set_mode((WIDTH, HEIGHT))\n",
        "the initial fullscreen setup",
    )
    code = replace_once(
        code,
        "        dt = clock.tick(FPS)\n",
        "        dt = clock.tick(FPS)\n"
        "        # Yield to the browser once per frame (required by pygbag).\n"
        "        await asyncio.sleep(0)\n",
        "the game loop clock tick",
    )
    code = replace_once(
        code,
        "                elif event.key == pygame.K_F11:\n",
        "                elif event.key == pygame.K_F11 and sys.platform != 'emscripten':\n",
        "the F11 fullscreen handler",
    )
    code = replace_once(
        code,
        "    pygame.quit()\n    sys.exit()\n\n\nif __name__ == \"__main__\":\n    main()\n",
        "    pygame.quit()\n\n\nif __name__ == \"__main__\":\n    asyncio.run(main())\n",
        "the program entry point",
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(code, encoding="utf-8")
    compile(code, str(OUTPUT), "exec")
    print(f"Generated browser-compatible game at {OUTPUT}")


if __name__ == "__main__":
    main()
