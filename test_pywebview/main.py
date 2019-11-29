import webview


class Api():

    def addItem(self, title):
        print(f"add item: {title}")
        return "title"


if __name__ == "__main__":
    window = webview.create_window("pami",
                                   url="assets/index.html",
                                   js_api=Api())
    webview.start(debug=True)
