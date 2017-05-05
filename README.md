# Status Update for Collins

## Description

Collins is a distributed task processor which can control worker nodes at various sites from a central console. Tasks can be scheduled, and executed at a regular frequency or be executed in an ad-hoc file. The worker nodes require only outbound IP access to the Cloud based API. A task is anything that can be wrapped in a Docker container, and output some basic HTML tags which will be rendered at the central console.

## Completed
- Added ability to add/delete jobs to UI
- ACI linter plugin Completed
- implemented DRF adapter for ember-data
- verified ability to traverse firewalls

## In Progress

- continuing to cleanup UI
- integration testing
- some backend automations when jobs are submitted

## Need help

If someone is familiar with Ansible, I think a cool next plugin would be to execute and arbitrary ansible-playbook and bubble the output up.

# Development

This project is under heavy development.  The easiest way to start contributing is to run a dev environment using
docker-compose. The current docker file will map local volumes so your code is live at all times.

```
docker-compose build
docker-compose up
```
# Server

```
virtualenv venv
source venv/bin/activate
pip install -r requirementst.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

# Beat Service

To start the beat service on the server side the following command is ran:

```
celery -A api beat -l info -S django
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
- [x] Save results from jobs ran on celery workers
- [ ] Job/Results detail view
- [ ] complete executioner code
- [ ] build executioner dockerfile
- [ ] Job Schedule(periodicTask)
- [ ] determine standard for plugin names _ or -
- [ ] always_fail plugin pushed to dockerhub
- [ ] always_pass plugin pushed to dockerhub
- [ ] apic-api-test plugin pushed to dockerhub
- [ ] apic-acitoolkit-lint plugin pushed to dockerhub
- [ ] remote workers
