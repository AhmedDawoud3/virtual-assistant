from modules.model import Model


class Main():
    def main(self):
        model = Model()

        while True:
            command = self._in("Enter your command: ")
            respond = model.process(command)
            if respond[0]:
                self._out(respond[1])
            else:
                respond[1](self._in, self._out)

    def _in(self, text):
        return input(text)

    def _out(self, text):
        print(text)


if __name__ == "__main__":
    main = Main()
    main.main()
