from pycukes import *
from selenium import webdriver

@step('setar o browser no selenium')
def test(context):
    context.ff = webdriver.Firefox()

@step('entrar em "(.*)"')
def test(step, string):
    context.ff.get(site)

@step('que o browser esteja na pagina "(.*)"')
def test(step, string):
    assert context.ff.current_url == "https://www.python.org/"

@step('a palavra "(.*)" deve estar no titulo')
def test(step, string):
    assert "Python" in context.ff.title
    context.ff.close()
