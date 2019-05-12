# selenium-headless
Selenium webdriver with headless chrome.

# Setup
Your first step, before writing a single line of Python, is to install a Selenium supported WebDriver for your favorite web browser. In what follows, you will be working with Firefox, but Chrome could easily work too.

Assuming that the path ~/.local/bin is in your execution PATH, here’s how you would install the chrome WebDriver on a Linux machine:

```Download chrome driver from official chrome webshite http://chromedriver.chromium.org/downloads ```
```$ tar xvfz chroedriver-v0.19.1-linux64.tar.gz```
```$ mv chromedriver ~/.local/bin```

Next, you install the selenium package, using pip or whatever you like. If you made a virtual environment for this project, you just type:

```$ pip install selenium```

