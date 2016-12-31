from radish import given, then
from selenium.webdriver.common.keys import Keys


dic = {"python": "https://www.python.org/"}


@given('entrar no site do {site:w}')
def test(scenario, site):
    scenario.context.ff.get(dic[site])


@then('buscar "{palavra:w}"')
def test(scenario, palavra):
    busca = scenario.context.ff.find_element_by_id(scenario.context.e['busca'])
    busca.clear()
    busca.send_keys('collections')
    busca.send_keys(Keys.RETURN)
