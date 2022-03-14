---
title: Python Compatibility Requirements
kind: documentation
description: 'Compatibility Requirements for the Python tracer'
aliases:
  - /tracing/compatibility_requirements/python
code_lang: python
type: multi-code-lang
code_lang_weight: 10
further_reading:
    - link: 'tracing/setup/python'
      tag: 'Documentation'
      text: 'Instrument Your Application'
---

The Python Datadog Trace library is open source. View the [GitHub repository][1] for more information.

Python versions `2.7+` and `3.5+` are supported in the latest version of the tracer. Python `3.4` is supported in versions `0.35.x` and below of the Python tracer.

## Integrations

To request support for additional libraries, contact our awesome [support team][2].

### Web framework compatibility

The `ddtrace` library includes support for a number of web frameworks, including:

| Framework                 | Supported Version | Automatic | Library Documentation                                              |
| ------------------------- | ----------------- | --------- |------------------------------------------------------------------ |
| [asgi][3]                 | >= 2.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#asgi    |
| [aiohttp][4]              | >= 1.2            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#aiohttp |
| [Bottle][5]               | >= 0.11           | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#bottle  |
| [CherryPy][6]            | >= 11.2.0         | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#cherrypy|
| [Django][7]               | >= 1.8            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#django  |
| [djangorestframework][7]  | >= 3.4            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#django  |
| [Falcon][8]               | >= 1.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#falcon  |
| [Flask][9]                | >= 0.10           | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#flask   |
| [FastAPI][10]              | >= 0.51           | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#fastapi |
| [Molten][11]               | >= 0.7.0          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#molten  |
| [Pylons][12]              | >= 0.9.6          | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#pylons  |
| [Pyramid][13]             | >= 1.7            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#pyramid |
| [pytest][14]              | >= 3.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#pytest  |
| [Sanic][15]               | >= 19.6.0         | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#sanic   |
| [Starlette][16]           | >= 0.13.0         | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#starlette |
| [Tornado][17]             | >= 4.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#tornado |



### Datastore compatibility

The `ddtrace` library includes support for the following data stores:

| Datastore                          | Supported Version | Automatic |  Library Documentation                                                                         |
| ---------------------------------- | ----------------- | --------- | --------------------------------------------------------------------------------------------- |
| [algoliasearch][18]                | >= 1.20.0         | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#algoliasearch                       |
| [asyncpg][19]                      | >= 0.18           | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#asyncpg                             |
| [Cassandra][20]                    | >= 3.5            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#cassandra                           |
| [Elasticsearch][21]                | >= 1.6            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#elasticsearch                       |
| [Flask Cache][22]                  | >= 0.12           | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#flask-cache                         |
| [Mariadb][23]                      | >= 1.0.0          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#mariadb                             |
| [Memcached][24] [pylibmc][25]      | >= 1.4            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#pylibmc                             |
| [Memcached][24] [pymemcache][26]   | >= 1.3            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#pymemcache                          |
| [MongoDB][27] [Mongoengine][28]    | >= 0.11           | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#mongoengine                         |
| [MongoDB][27] [Pymongo][29]        | >= 3.0            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#pymongo                             |
| [MySQL][30] [MySQL-python][31]     | >= 1.2.3          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#module-ddtrace.contrib.mysqldb      |
| [MySQL][30] [mysqlclient][32]      | >= 1.3            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#module-ddtrace.contrib.mysqldb      |
| [MySQL][30] [mysql-connector][33]  | >= 2.1            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#mysql-connector                     |
| [Postgres][34] [aiopg][35]         | >= 0.12.0, <=&nbsp;0.16        | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#aiopg                               |
| [Postgres][34] [psycopg][36]       | >= 2.4            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#module-ddtrace.contrib.psycopg      |
| [PynamoDB][37]                     | >= 4.0            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#pynamodb                               |
| [PyODBC][38]                       | >= 4.0            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#pyodbc                               |
| [Redis][39]                        | >= 2.6            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#redis                               |
| [Redis][39] [redis-py-cluster][40] | >= 1.3.5          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#module-ddtrace.contrib.rediscluster |
| [SQLAlchemy][41]                   | >= 1.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#sqlalchemy                          |
| [SQLite3][42]                      | Fully Supported   | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#sqlite                              |
| [Vertica][43]                      | >= 0.6            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#vertica                             |

### Library compatibility

The `ddtrace` library includes support for the following libraries:

| Library           | Supported Version |  Automatic       | Library Documentation                                                    |
| ----------------- | ----------------- | ---------------- | ------------------------------------------------------------------------ |
| [aiobotocore][44] | >= 0.2.3          | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#aiobotocore |
| [asyncio][45]     | Fully Supported   | > Python 3.7 yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#asyncio     |
| [Botocore][46]    | >= 1.4.51         | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#botocore    |
| [Boto2][47]       | >= 2.29.0         | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#boto2       |
| [Celery][48]      | >= 3.1            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#celery      |
| [Consul][49]      | >= 0.7            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#consul      |
| [Futures][50]     | Fully Supported   | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#futures     |
| [gevent][51]      | >= 1.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#gevent      |
| [Grpc][52]        | >= 1.8.0          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#grpc        |
| [httplib][53]     | Fully Supported   | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#httplib     |
| [Jinja2][54]      | >= 2.7            | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#jinja2      |
| [Kombu][55]       | >= 4.0            | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#kombu       |
| [Mako][56]        | >= 0.1.0          | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#mako        |
| [Requests][57]    | >= 2.08           | yes | https://ddtrace.readthedocs.io/en/stable/integrations.html#requests    |
| [urllib3][58]     | >= 1.22           | no | https://ddtrace.readthedocs.io/en/stable/integrations.html#urllib3     |

## Further Reading

{{< partial name="whats-next/whats-next.html" >}}

[1]: https://github.com/DataDog/dd-trace-py
[2]: /help
[3]: http://asgi.readthedocs.io/
[4]: https://aiohttp.readthedocs.io
[5]: https://bottlepy.org
[6]: https://cherrypy.org/
[7]: https://www.djangoproject.com
[8]: https://falconframework.org
[9]: http://flask.pocoo.org
[10]: https://fastapi.tiangolo.com/
[11]: https://moltenframework.com
[12]: http://pylonsproject.org
[13]: https://trypyramid.com
[14]: https://docs.pytest.org/en/stable/
[15]: https://sanic.readthedocs.io/en/latest/
[16]: https://www.starlette.io/
[17]: http://www.tornadoweb.org
[18]: https://www.algolia.com/doc/
[19]: https://magicstack.github.io/asyncpg
[20]: https://cassandra.apache.org
[21]: https://www.elastic.co/products/elasticsearch
[22]: https://pythonhosted.org/Flask-Cache
[23]: https://mariadb-corporation.github.io/mariadb-connector-python/index.html
[24]: https://memcached.org
[25]: http://sendapatch.se/projects/pylibmc
[26]: https://pymemcache.readthedocs.io
[27]: https://www.mongodb.com/what-is-mongodb
[28]: http://mongoengine.org
[29]: https://api.mongodb.com/python/current
[30]: https://www.mysql.com
[31]: https://pypi.org/project/MySQL-python
[32]: https://pypi.org/project/mysqlclient
[33]: https://dev.mysql.com/doc/connector-python/en/
[34]: https://www.postgresql.org
[35]: https://aiopg.readthedocs.io
[36]: http://initd.org/psycopg
[37]: https://pynamodb.readthedocs.io/en/latest/
[38]: https://pypi.org/project/pyodbc/
[39]: https://redis.io
[40]: https://redis-py-cluster.readthedocs.io
[41]: https://www.sqlalchemy.org
[42]: https://www.sqlite.org
[43]: https://www.vertica.com
[44]: https://pypi.org/project/aiobotocore/
[45]: https://docs.python.org/3/library/asyncio.html
[46]: https://pypi.org/project/botocore/
[47]: http://docs.pythonboto.org/en/latest
[48]: http://www.celeryproject.org
[49]: https://python-consul.readthedocs.io/en/latest/
[50]: https://docs.python.org/3/library/concurrent.futures.html
[51]: http://www.gevent.org
[52]: https://grpc.io
[53]: https://docs.python.org/2/library/httplib.html
[54]: http://jinja.pocoo.org
[55]: https://kombu.readthedocs.io/en/latest
[56]: https://www.makotemplates.org
[57]: https://requests.readthedocs.io/en/master/
[58]: https://urllib3.readthedocs.io/en/stable/
