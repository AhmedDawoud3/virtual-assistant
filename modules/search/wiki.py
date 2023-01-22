import wikipedia
import webbrowser as wb


class Wiki:
    def wiki_search(self, text):
        try:
            self.result = wikipedia.summary(text, sentences=1)
            return True

        except wikipedia.DisambiguationError as pages:
            return self.wiki_search(pages.options[0])

        except wikipedia.exceptions.PageError:
            Wiki.google_search(text)
            return False

    def get_result(self):
        return f"According to wikipedia: {self.result}"

    def google_search(text):
        wb.open_new_tab(f'https://www.google.com/search?q={text}')
        return True
