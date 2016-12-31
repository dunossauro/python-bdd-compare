from pytest_bdd import scenarios, given, then, parsers
from selenium import webdriver

scenarios('features')

ff = None


@given('setar o browser no selenium')
def set():
    global ff
    ff = webdriver.Firefox()


@given(parsers.parse('entrar em {site}'))
def ent(site):
    ff.get(site)


@given(parsers.parse('que o browser esteja na pagina {site}'))
def chek(site):
    assert ff.current_url == site


@then(parsers.parse('a palavra {palavra} deve estar no titulo'))
def tassert(palavra):
    assert palavra in ff.title
    ff.quit()
