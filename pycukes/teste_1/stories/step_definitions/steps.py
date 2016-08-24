from behave import step
from selenium import webdriver

@step('setar o browser no selenium')
def test(context):
    context.ff = webdriver.Firefox()

@step('entrar em "{site}"')
def test(context, site):
    context.ff.get(site)

@step('que o browser esteja na pagina "{site}"')
def test(context, site):
    assert context.ff.current_url == "https://www.python.org/"

@step('a palavra "{frase}" deve estar no titulo')
def test(context, frase):
    assert "Python" in context.ff.title
    context.ff.close()
