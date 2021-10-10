from selenium import webdriver
import math

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome(executable_path='/Users/antonzimaev/PycharmProjects/stepik_selenium/chromedriver-1')
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value')
x = x_element.text
print(x)
y = calc(x)

input_field = browser.find_element_by_id('answer')
input_field.send_keys(y)
the_robot = browser.find_element_by_id('robotCheckbox').click()
robots_rule = browser.find_element_by_css_selector("label[for='robotsRule']").click()
button = browser.find_element_by_tag_name('button').click()
msg = browser.switch_to.alert.text

