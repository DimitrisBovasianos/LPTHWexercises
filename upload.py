import web

urls = (
  '/upload', 'upload'
)

class upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) #this is the filename
        web.debug(x['myfile'].value) #this is the file contents
        web.debug(x['myfile'].file.read())
        raise web.seeother('/upload')



if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
