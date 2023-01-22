#captcha solver python
from twocaptcha import TwoCaptcha

# Create a client with your 2Captcha API key
client = TwoCaptcha('YOUR_API_KEY')

# Submit the reCAPTCHA for solving
response = client.solve_recaptcha(
    sitekey='YOUR_SITE_KEY',
    pageurl='https://example.com/page-with-captcha'
)

# Get the solution
solution = response.await_solution()

# Use the solution to complete the form
# ...
