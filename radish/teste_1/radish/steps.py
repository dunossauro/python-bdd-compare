from radish import given, then, step
from selenium import webdriver

dic = {"python": "https://www.python.org/"}


@given('setar o browser no selenium')
def test(step):
    step.context.ff = webdriver.PhantomJS()


@given('entrar no site do {site:w}')
def test(step, site):
    step.context.ff.get(dic[site])


@given("que o browser esteja na pagina {site:w}")
def test(step, site):
    assert step.context.ff.current_url == dic[site]


@then('a palavra {frase:w} deve estar no titulo')
def test(step, frase):
    assert frase in step.context.ff.title
    step.context.ff.close()
