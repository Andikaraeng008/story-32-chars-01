"""Write the winning Wi-Fi network name to /output/entry.txt.

The name is 29 characters, and its last words are the twist: he
proposed, and the WiFi said no.
"""

SSID = "He Proposed, the WiFi Said No"  # 29 characters


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SSID)


if __name__ == "__main__":
    main()
