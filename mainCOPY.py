import webapp2
import cgi
import re
from string import letters
from google.appengine.ext import db

def build_page(username_error="", password_error="", verifyPassword_error="", email_error=""):

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
       "<table>" +
       "<tr>" + "<td>" + username_label + "</td>" + "<td>" + username_input + "</td>" + "<td>" + username_error + "</td>" + "</tr>" + "<br>" +
       "<tr>" + "<td>" + password_label + "</td>" + "<td>" + password_input + "</td>" + "<td>" + password_error + "</td>" + "</tr>" + "<br>" +
       "<tr>" + "<td>" + verifyPassword_label + "</td>" + "<td>" + verifyPassword_input + "</td>" + "<td>" + verifyPassword_error + "</td>" + "</tr>" + "<br>" +
       "<tr>" + "<td>" + email_label + "</td>" + "<td>" + email_input + "</td>" + "<td>" + email_error + "</td>" + "</tr>" + "<br>" +
       "</table>" + submit + "</form>")

   header = "<h1>Signup</h1>"

   return header + form


class Index(webapp2.RequestHandler):
   def get(self):
       content = build_page("")
       self.response.write(content)

   def post(self):
       have_error = False
       username = self.request.get('username')
       password = self.request.get('password')
       verifyPassword = self.request.get('verifyPassword')
       email = self.request.get('email')

       params = dict(username = username,
                     password = password,
                     verifyPassword = verifyPassword,
                     email = email)

     #check if username is empty, password empty
       if username == "":
           params['username_error'] = "That's not a valid username."
           have_error = True

       if password == "":
           params['password_error'] = "That wasn't a valid password."
           have_error = True

       if verifyPassword == "":
           params['verifyPassword_error'] = "Please enter a matching password."
           have_error = True

       if password != verifyPassword:
           params['verifyPassword_error'] = "Please enter a matching password."
           have_error = True

       if have_error:
           self.redirect('/' + params)
       else:
           self.redirect('/welome', username = username)

      #more validation
       USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
       def valid_username(username):
           return username and USER_RE.match(username)

       PASS_RE = re.compile(r"^.{3,20}$")
       def valid_password(password):
           return password and PASS_RE.match(password)

       def equal_password(verifyPassword, password):
       if password == verify_password:
           return True
       else:
           return False

       EMAIL_RE = re.compile(r'^[\S]+@[\S\+\.[\S]+$')
       def valid_email(email):
           return not email or EMAIL_RE.match(email)

       def helper(self, user_message="", user_password="", match_password="", user_email=""):
      #string substitution
           self.response.write(form.format(username_message= user_message,
                                       password_message= user_password,
                                       password_match_message= match_password,
                                       email_message= user_email
                                       ))

       signup = username + password + verifyPassword + email
       escaped_signup = cgi.escape(signup, quote=True)
       content = build_page(escaped_signup)
       self.response.write(content)

class Welcome(webapp2.RequestHandler):
   def post(self):
       username = self.request.get('username')
       if valid_username(username):
           self.redirect('/welcome', username = username)
       else:
           self.redirect('/')

app = webapp2.WSGIApplication([('/', Index),
                               ('/welcome', Welcome)],
                               debug=True)
