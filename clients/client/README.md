# Collins Client

This is the collins worker client, the client is usually ran as a docker container

# Docker Daemon

Currently we bind map to docker socket

```
-v /var/run/docker.sock:/var/run/docker.sock

```

# Environment

The following environment variables are supported

- RESULTS_API_URL (required)
- RESULTS_API_USER
- RESULTS_API_PASSWORD


### Interactively review results
```
(venv) KECORBIN-M-90Y9:client kecorbin$ docker run -ti --net=c8b9500cb16d collins-worker /bin/bash
root@456794991d9e:/code# export REDIS_URL=redis://redis
root@456794991d9e:/code# export RABBITMQ_URL=pyamqp://guest:guest@rabbit//
root@456794991d9e:/code# python
Python 2.7.6 (default, Oct 26 2016, 20:30:19)
[GCC 4.8.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> pyamqp://guest:guest@rabbit//
KeyboardInterrupt
>>> import docker
>>> from celery import Celery
>>> import os
>>>
>>>
>>> app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'),
...                       backend=os.getenv("REDIS_URL"),
...                       includes=['api.tasks']
...              )
>>>
>>> import api.tasks
>>>
>>> results = api.tasks.run_image.apply_async(args=['docker/whalesay'], kwargs={"command":"cowsay moo"}, queue="SITE_1")
>>> results.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'AsyncResult' object has no attribute 'read'
>>> results.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'AsyncResult' object has no attribute 'read'
>>> results.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'AsyncResult' object has no attribute 'read'
>>> results.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'AsyncResult' object has no attribute 'read'
>>> results = api.tasks.run_image.apply_async(args=['docker/whalesay'], kwargs={"command":"cowsay moo"}, queue="SITE_1")
KeyboardInterrupt
>>> results.
KeyboardInterrupt
>>> resp = api.tasks.run_image.apply_async(args=['docker/whalesay'], kwargs={"command":"cowsay moo"}, queue="SITE_1")
>>> resp
<AsyncResult: 32f8846d-e72a-4945-8312-0221f09b6ad7>
>>> resp.ready()
True
>>> resp.get()
u' _____ \n< moo >\n ----- \n    \\\n     \\\n      \\     \n                    ##        .            \n              ## ## ##       ==            \n           ## ## ## ##      ===            \n       /""""""""""""""""___/ ===        \n  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   \n       \\______ o          __/            \n        \\    \\        __/             \n          \\____\\______/   \n'
>>> print(resp.get())
 _____
< moo >
 -----
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/

>>>
```

#### Interactively schedule jobs

```
import docker
from celery import Celery
import os


app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'),
                      backend=os.getenv("REDIS_URL"),
                      includes=['api.tasks']
             )

import api.tasks

results = api.tasks.run_image.apply_async(args=['docker/whalesay'], kwargs={"command":"cowsay moo"}, queue="SITE_1")

```
