import webapp2
import cgi
import re

form = """
<h1>User Signup</h1>
<form method = "post">
<table>
<tr>
<td>
<label>Username: <input type="text" name="username" value="{username}"/></label>
</td>
<td>
<label style="color:red">{username_message}</label>
</td>
</tr>

<tr>
<td>
<label>Password: <input type="text" name="password"/></label>
<td>
<label style="color:red">{password_message}</label>
</td>
</td></tr>

<tr>
<td>
<label>Verify Password: <input type="text" name="verify_password"/>
</label>

<td>
<label style="color:red">{password_match_message}</label>
</td>
</td></tr>

<tr>
<td>
<label>Email (optional): <input type="text" name="email" value="{email}"/></label>
<td>
<label style="color:red">{email_message}</label>
</td>
</td></tr>

</table>
<input type = 'submit'/>
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

def equal_password(verify_password, password):
    if password == verify_password:
        return True
    else:
        return False

EMAIL_RE = re.compile(r'^[\S]+@[\S\+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def helper(self, user_message="", user_password="", match_password="",
               user_email=""):
        #string substitution
        self.response.write(form.format(username_message= user_message,
                              password_message= user_password,
                              password_match_message= match_password,
                              email_message= user_email
                              ))
    def get(self):
        self.helper()

    def post(self):
        # look inside the request to figure out what the user typed
        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email = self.request.get("email")

        params = dict(username = username,
                      email = email)

        #if valid_username(username) == "" or ! valid_username
        user_message=""
        user_password=""
        match_password=""
        user_email=""
        if valid_username(username) and valid_password(password) and equal_password(password, verify_password) and valid_email(email):
            self.redirect('/welcome?username=' + username)

        if not valid_username(username):
            user_message="Username not valid"
        if not valid_password(password):
            user_password="Password not valid"
        if not equal_password(password, verify_password):
            match_password="Passwords must match"
        if email is not "" and not valid_email(email):
            user_email="Please enter a valid email"

        self.response.write(form.format(username_message= user_message,
                                    username = username,
                                  password_message= user_password,
                                  password_match_message= match_password,
                                  email_message= user_email,
                                  email = email
                                  ))

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.write(welcome.format(username = username))

#html for welcome page
welcome = """
<!DOCTYPE html>

<html>
<head>
    <title>
    User Signup
    </title>
</head>

<body>
#string substitution for username
<h2>Welcome, {username}!</h2>
</body>
</html>
"""

app = webapp2.WSGIApplication([
            ('/', MainHandler),
            ('/welcome', Welcome)
            ], debug=True)
