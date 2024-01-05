# web-api-eval
python web api repo for demonstrating api pattern, documentation, build, deploy and maintenance


### Built With

* Python Flask
* Docker
* Terraform
* Github Actions
* AWS

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Installation

To run the app locally clone the repo and run following commands. ( requires docker to be installed)

1. ```docker build -t flask-app . ```
2. ```docker run -d -p 5001:5000 --name flask-app-api flask-app ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Evalutaions aspects -->
## Evaluation aspects

* TLS Termination is implement using AWS Load Balancer where the ingress traffic is encrypted and egress to target groups attached to ECS fargate service

* ```/status``` - health check url is implemented to monitor application

* Sr Devops assessment apis are under ```web_api_eval/api/v1/routes```. following are the endpoints: ( all the calls require AUTHTOKE=Aiu1bFm1blAbfhab header and all the calls are scoped with user_id except for POST):


| Routes        | Method           | End point  |
| ------------- |:-------------:| -----:|
|  api_1.create_user | POST | /tenant_name>/api/v1/user |
| api_1.delete_users | DELETE | /tenant_name>/api/v1/user |
| api_1.get_users    | GET | /tenant_name>/api/v1/user |
| api_1.update_user  | PUT | /tenant_name>/api/v1/user  |
| health_check.get_status | GET|/status   |
|tenant.create_tenant  | POST| /tenant |
|tenant.get_tenants    | GET | /tenant |

*/default/api/v1/user - accepts token included in assessment. other tenants accept token provided during tenant creation
* payload for creating tenant:
    {
        "name":"tenant1",
        "token":"sdfg345"
    }
* Devops assessment api ```/api/v2/dictionary?word=hello```. Replace hello with word of choice to fetch definition

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* GitHUB Action : https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service
* Terraform : https://github.com/Rose-stack/docker-aws-ecs-using-terraform/blob/main/main.tf
* Flask : https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

<p align="right">(<a href="#readme-top">back to top</a>)</p>


