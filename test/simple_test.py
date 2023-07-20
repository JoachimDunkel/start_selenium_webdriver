import sys
import os

sys.path.append(str(os.getcwd()))

from start_selenium_webdriver.webdriver_startup import setup_webdriver

end_point = "https://www.google.com/"
driver = setup_webdriver(num_sec_implicit_wait=0)
driver.get(end_point)

print("Done")