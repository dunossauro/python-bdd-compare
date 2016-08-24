# Pycukes

Logo na execução do primeiro teste obtive o seguinte resultado:

```
File "/usr/lib/python3.5/site-packages/pycukes/__init__.py", line 1, in <module>
  from runner import StoryRunner
ImportError: No module named 'runner'
```

Então fui dar uma olhada no [github do projeto](https://github.com/hugobr/pycukes), não tem requirements.
Vamos então ao [setup.py](https://github.com/hugobr/pycukes/blob/master/setup.py):

```python
install_requires=[
     'story_parser>=0.1.2',
     'should_dsl',
     'pyhistorian>=0.6.8',
]
```

Também não fala sobre o runner, então, tudo certo: `pip install runner`

```
Requirement already satisfied (use --upgrade to upgrade): runner in /usr/lib/python3.5/site-packages
```

Vamos tentar pelo modo convencional, só por precução:

```
In [1]: import runner
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-a8239a62d2de> in <module>()
----> 1 import runner

ImportError: No module named 'runner'

In [2]: import Runner

In [3]: dir(Runner)
Out[3]:
['Run',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '__version__']
```

Bom, as respostas não foram positivas, nem negativas. Só não foi possível obter a resposta esperada. Então abri uma [issue](https://github.com/hltbra/pycukes/issues/9) no projeto (23/ago/16) e quando obter a resposta volto a executar os testes
