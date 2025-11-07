import urllib.request

# the Jane Eyre text link from Project Gutenberg
url = "https://www.gutenberg.org/cache/epub/1260/pg1260.txt"

try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode("utf-8")

        # show first few lines to check it worked
        print(text[:500])  

        with open("jane_eyre.txt", "w", encoding="utf-8") as out:
            out.write(text)
        print("\n✅ Download complete! Saved as jane_eyre.txt")
except Exception as e:
    print(" An error occurred:", e)
