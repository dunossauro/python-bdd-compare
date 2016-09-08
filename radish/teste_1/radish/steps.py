from radish import given, then, feature, world
from selenium import webdriver

dic = {"python" : "https://www.python.org/"}

@given('setar o browser no selenium')
def test(feature):
    feature.context.ff = webdriver.Firefox()

@given('entrar no site do {site:w}')
def test(feature, site):
    feature.context.ff.get(dic[site])

@given("que o browser esteja na pagina {site:w}")
def test(feature, site):
    assert feature.context.ff.current_url == dic[site]

@then('a palavra {frase:w} deve estar no titulo')
def test(feature, frase):
    assert frase in feature.context.ff.title
    feature.context.ff.close()
