import webapp2
import cgi


def build_page(textarea_content):
   username_label = "<label>Username</label>"
   username_input = "<input type='text' name='username'>"

   password_label = "<label>Password</label>"
   password_input = "<input type='text' name='password'>"

   verifyPassword_label = "<label>Verify Password</label>"
   verifyPassword_input = "<input type='text' name='verifyPassword'>"

   email_label = "<label>Email (optional)</label>"
   email_input = "<input type='text' name='email'>"

   submit = "<input type='submit'/>"
   form = ("<form method='post'>" +
       username_label + username_input + "<br>" +
       password_label + password_input + "<br>" +
       verifyPassword_label + verifyPassword_input + "<br>" +
       email_label + email_input + "<br>" +
       submit + "</form>")

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
       escaped_messages = cgi.escape(returned_messages, quote=True)
       content = build_page(escaped_messages)
       self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
