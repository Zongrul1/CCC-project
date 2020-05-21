# CCC Assignment 2


## Deadlines
Wednesday **27th May**.

## Schedule

| Date | Task |
| ---- | ---- |
| 29 April - 5 May | xxx |
| 6 May - 12 May  | xxx |
| 13 May - 19 May | xxx |

## Report 

[Google Docs](https://docs.google.com/document/d/1cmAZPMd_cMoZovoOQ9oAVQEcvcezhG1WOlRujWO3Qxw/edit)

## About instances

Four instances exist. Each one has 2 VCPU, 9 GB RAM and private IP address.
One instance for running program, which is 172.26.133.24(demo1)
And the rest instances are for storage.

#### How to connect to an instance

Move to the directory where ins1.pem is located, then use the following commands:  
```
Execute only once
chmod 600 ins1.pem
Execute every time you wanna connect to the instance
The IP could be changed to the corresponding one
ssh -i ins2.pem ubuntu@172.26.130.129
 ```

## Technical Framework

- TBD  
- Ansible  
- Docker  
- CouchDB  
- Twitter API
- Python

## For Reference

#### LaTeX

[A short introduction to LaTeX](https://www.latex-project.org/help/documentation/usrguide.pdf)

#### Git Workflow

[Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) & [Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request)

#### What is REST

- [First](https://www.ruanyifeng.com/blog/2011/09/restful.html)
- [Second](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
- [Third](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)