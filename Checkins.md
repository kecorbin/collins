# Status Update for Collins

## Project Name
Collins

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
