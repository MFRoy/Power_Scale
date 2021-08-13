# Practical Project

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Kanban Board](#kanban-board)
  * [Test Analysis](#analysis-of-testing)
* [Infrastructure](#infrastructure)
  * [Jenkins](#jenkins)
  * [Entity Diagram](#entity-diagram)
  * [Docker Swarm](#interactions-diagram)
  * [The 4 Services](#the-4-services)
* [Development](#development)
  * [Front-End Design](#front-end)
  * [Unit Testing](#unit-testing)
* [Footer](#footer)

## Introduction
### Objective
The objective provided for this project is as follows:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

The 4 containers must comprise of 1 front end service, 2 back end services and 1 other back end service that utalises data from the previus two back end services.

The following constraints were aso in place:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

### Proposal
In order to furfil all of the requirements i decided to focus on the infastructure implementation of the CI/CD this allows for a fairly simple application. For the aplication i decide as to keep it simple i made a power scale utalising the following.
* Service 1 (front-end): displays the results of the following 3 services for the user to see, as well as a brief history of past results
* Service 2: returns a random occupation
* Service 3: returns a random species
* Service 4: returns a number based on the prior two services as a power level

## Architecture
### Risk Assessment
My detailed risk assessment can be seen below, outlining the risks that have potential to impact the project. A risk  assesment is an important tool to avoid issues wher epossible but also to be aware of solutions when risks arise.
