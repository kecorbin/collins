# Collins

Collins is your one stop shop for validating Cisco ACI against a published ecosystems of best practices.

# Server

```
virtualenv venv
source venv/bin/activate
pip install -r requirementst.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```


# Client

The client is the plugin manager, it is responsible for executing jobs



## Plugins

* always_pass
* always_fail
* apic-acitoolkit-lint - Sample plugin using the acitoolkit lint application
* apic-api-test - Test Authentication to APIC


# Milestones
- [x] API can send/receive jobs
- [x] Sample plugins
- [x] Execute Jobs on celery workers
- [x] Results associated with jobs (django ORM)
- [x] API can send/receive results by job id
- [x] last result functionality Dockerjob.results.last().result should populate last_result on Job
- [ ] Save results from jobs ran on celery workers
- [ ] Job Schedule(periodicTask)
- [ ] determine standard for plugin names _ or -
- [ ] always_fail plugin
- [ ] always_pass plugin
- [ ] apic-api-test plugin
- [ ] apic-acitoolkit-lint plugin
- [ ] remote workers
