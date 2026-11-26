"""Write the winning Wi-Fi network name to /output/entry.txt.

The name is exactly 32 characters, the most the gate allows, and its
last word is the twist: a baby's first word is not mama or dada.
"""

SSID = "He Proposed on the WiFi Password"  # 32 characters, gate limit


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SSID)


if __name__ == "__main__":
    main()
