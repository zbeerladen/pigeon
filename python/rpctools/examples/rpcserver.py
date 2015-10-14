from rpctools.rpctools import RPCServer

class App(RPCServer):

    def rpc_greeting(self, text):
        self.message("Hello %s!" % text, meta="hello")
        while self.ask("Do you want me to say it again?", meta="hello_again?") == "yes":
            self.message("Hello again %s!" % text, meta="hello_again")
            continue


app = App()
app.connect("localhost", 1234)
app.run(True)
app.disconnect()
