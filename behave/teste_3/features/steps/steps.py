from behave import step
from selenium.webdriver.common.keys import Keys


@step('entro no site "{site}"')
def test(context, site):
    context.ff.get(site)


@step('buscar "{palavra:w}"')
def test(context, palavra):
    busca = context.ff.find_element_by_id(context.e['busca'])
    busca.clear()
    busca.send_keys('collections')
    busca.send_keys(Keys.RETURN)


@step('fechar o browser')
def test(context):
    context.ff.quit()
