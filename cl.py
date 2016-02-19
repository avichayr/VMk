import  socket

c = socket.socket()

c.connect(("avichayr.koding.io", 5677))
c.send("hello world!")
c.close()