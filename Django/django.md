http 
hyper test  transfer protcol

client ---> server

get / http/1.1
www.example.com
server process   reqeu


http/1.1 200 0k    (respoonse)
content-type :text/html


status 

<!-- 200 ok
301  Website redirected to a new domain.
401 Unauthorized	Authentication is required or invalid.	Missing or invalid JWT token.
403 Forbidden	User is authenticated but doesn't have permission.	Normal user tries to access the admin page.
404 Not Found	Requested resource does not exist.	Wrong API URL or page doesn't exist.
500 intereal server -->

When a user opens a URL, the request goes to the server, then through middleware for security checks. Django matches the URL in urls.py and calls the correct view. The view uses models to get data from the database, sends that data to a template, and returns a response. Middleware runs again on the way out, and the browser shows the page

When a user sends a request, it first reaches Nginx, which acts as a reverse proxy and serves static files. Dynamic requests are forwarded to Gunicorn, a WSGI application server that runs the Django application. The request then passes through Django middleware, is matched in urls.py, and the corresponding view is executed. The view may interact with models to query the database. The retrieved data is used to render an HTML template or create a JSON response. The response passes back through middleware, then Gunicorn, then Nginx, and is finally returned to the user's browser


Nginx is a web server that receives requests from users and forwards dynamic requests to Gunicorn. It can also serve static files like CSS, JavaScript, and images.


middle ware is one kind of sotware communcation is between request and response 

SecurityMiddleware	Adds security headers and HTTPS-related protections
SessionMiddleware	Manages user sessions
CommonMiddleware	URL normalization and common HTTP behavior
CsrfViewMiddleware	Protects against CSRF attacks
AuthenticationMiddleware	Identifies the logged-in user
MessageMiddleware	Supports one-time messages (success/error/info)
ClickjackingMiddleware	Protects against clickjacking attacks

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before View")

        response = self.get_response(request)

        print("After View")

        return response

Nginx checks:

Is it a CSS file?
Is it an image?
Is it a JavaScript file?
Or is it a Django request?


Gunicorn is a WSGI application server for Python web applications. It runs the Django application in production, receives requests from Nginx, passes them to Django through the WSGI interface, manages multiple worker processes to handle concurrent requests, and sends the response back to Nginx.



permission_classes = [IsAuthenticated]
permission_classes = [IsAdminUser]
django-admin startproject PROJECT_NAME
python manage.py startapp APP_NAME.


Permission	Who can access?
AllowAny	Everyone (login not required)
IsAuthenticated	Any logged-in user
IsAdminUser	Only admin/staff users
IsAuthenticatedOrReadOnly	Everyone can GET; only logged-in users can POST, PUT, DELETE


: What is Authentication?

Authentication is the process of verifying the identity of a user. In Django, this can be done using a username/password or a JWT token. If the credentials or token are valid, the user is authenticated.

Q: What is Authorization?

Authorization is the process of determining what an authenticated user is allowed to access. In Django REST Framework, this is implemented using permission classes such as IsAuthenticated, IsAdminUser, and IsAuthenticatedOrReadOnly

