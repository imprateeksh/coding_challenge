# IBM: coding_challenge
* Created a basic app that provides organization feedbacks.

* Randomly some parameters are taken to construct feedback data (can be seen in utils -> util_data.py)

* Feedback is stored in a file that is persisted.
* Peristence can be achieved as I have used the hostpath mounting in helm chart when deployed in K8s cluster
* If running as a docker container alone, docker volume mounting is done to persist the data


* Two endpoints are created to honor POST and GET calls. 
* One health endpoint and one Authentication token generator endpoint is used.
* Swagger document is created

** Yet to cover ***
Add API authentication
Docker file creation – try to use multi level approach
Docker file push to artifactory
Use gradle script to start build creation
Use Jenkins file to start project and progress
Configuring Jenkins
FMEAs
-------------------
Unit tests
Bdd creation – feature files (extra)
Reliability/load testing (extra)
Docker image vulnerability scan (extra)
Nexus/Artifactory usage (if not using Docker hub) - Creating pipeline step, post plugin addition
Terraform usage (Optional, can be thought)
KVM setup (extra)
------------------------

Pipeline stages that can be added - 

(1) Checkout code

(2) Build and unit test

(3) Create docker image and Helm chart

(4) Anchore/Twistlock Scan of Docker image for vulnerability

(5) Push image to any artifactory - dockerhub / Nexus

(6) helm install chart in Cloud machine as per configuration given

GITHUB -> API CODE -> JENKINS -> CLOUD MACHINE DEPLOYMENT
----------------------
** ASSUMPTION **

I have assumed the machine where helm chart will be installed has already Kubernetes environment setup ready i.e. docker, kubectl, minikube, kind or any other environment, helm 

If not, we can create a separate terraform project that is having machine configurations and different plugins to setup machine



