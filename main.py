import webapp2
import cgi

def build_page(textarea_content):
   username_label = "<label>Username</label>"
   textarea_username = "<textarea name='username' style='height: 30; width: 100;'>" + textarea_content + "</textarea><br>"


   password_label = "<label>Password</label>"
   textarea_password = "<textarea name='password' style='height: 30; width: 100;'>" + textarea_content + "</textarea><br>"

   verifyPassword_label = "<label>Verify Password</label>"
   textarea_verifyPassword = "<textarea name='verifyPassword' style='height: 30; width: 100;'>" + textarea_content + "</textarea><br>"

   email_label = "<label>Email (optional)</label>"
   textarea_email = "<textarea name='email' style='height: 30; width: 100;'>" + textarea_content + "</textarea><br>"

   submit = "<input type='submit'/>"
   form = ("<form method='post'>" +
       username_label + textarea_username + "<br>" +
       password_label + textarea_password + "<br>" +
       verifyPassword_label + textarea_verifyPassword + "<br>" +
       email_label + textarea_email + "<br>" +
       submit + "</form>")

<body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;"></textarea>
      <br>
      <input type="submit">
    </form>
  </body>

   header = "<h1>Signup</h1>"

   return header + form


class MainHandler(webapp2.RequestHandler):

   def get(self):
       content = build_page("")
       self.response.write(content)

   def post(self):
       username = self.request.get("username")
       password = self.request.get("password")
       verifyPassword = self.request.get("verifyPassword")
       email = self.request.get("email")


       returned_messages = username + password + verifyPassword + email
       escaped_messages = cgi.escape(returned_messages)
       content = build_page(escaped_messages)
       self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
