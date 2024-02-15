import webbrowser as wb


def webAuto():
    urls = ("github.com/ahsanchez", "gmail.com", "google.com")

    for url in urls:
        print("Open URL=", url)
        wb.get().open(url)


webAuto()
