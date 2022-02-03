## The Csvserver Assignment

### Part 1

**Pull and Run the Docker CSVSERVER image**

```sh
root@instance-1:~/infracloud/csvserver/solution# docker pull infracloudio/csvserver
Using default tag: latest
latest: Pulling from infracloudio/csvserver
ae43b40a9945: Pull complete
7bb33bb2db38: Pull complete
c82d72e1bb76: Pull complete
Digest: sha256:20bc5a93fac217270fe5c88d639d82c6ecb18fc908283e046d9a3917a840ec1f
Status: Downloaded newer image for infracloudio/csvserver:latest
docker.io/infracloudio/csvserver:latest

root@instance-1:~/infracloud/csvserver/solution# docker run -d infracloudio/csvserver
3c86214e560a9cfd72d38f6fd0e8fba899272af517eac17b14d6ca98cf78f3b3

root@instance-1:~/infracloud/csvserver/solution# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

root@instance-1:~/infracloud/csvserver/solution# docker ps -a
CONTAINER ID   IMAGE                    COMMAND                  CREATED              STATUS                          PORTS     NAMES
3c86214e560a   infracloudio/csvserver   "/csvserver/csvserver"   About a minute ago   Exited (1) About a minute ago             focused_mendel

root@instance-1:~/infracloud/csvserver/solution# docker logs 3c86214e560a
2022/01/30 07:35:28 error while reading the file "/csvserver/inputdata": open /csvserver/inputdata: no such file or directory
```
**Problems and Soultions**

- As per our requirement, the container has run with detach mode, but it exiting beacuse of absent of the inputdata file.
- From the logs, it's clear that csvserver app expecting a file named inputdata and that should be present in conatiner's `/csvserver`.
- Before rerunning the container, you should make sure that the inputdata file being mounted inside container.
- As a next step of action, we are going to create a script named `gencsv.sh` that could generate an inputFile file and statisfies the csv format.

**Create script with name gencsv.sh**

```sh
#!/bin/bash
gencsv(){
    x=0;for i in $(shuf -i 10-999 -n 10); do echo "${x}, ${i}"; (( x = x+1 )); done
}
gencsv > inputFile
```
**Instruction**

- Create the above script inside the `solution` directory and give the execute permission by executing `chmod +x genscv.sh`.
-  Now run the script `./gencsv.sh` and check if the `inputFile` being created.

**Re-run the conatiner with volume**
```sh
root@instance-1:~/infracloud/csvserver/solution# docker run -d -v "$(pwd)"/inputFile:/csvserver/inputdata  infracloudio/csvserver
cd269201c359a077f4fe7fb082a2a785db80ddfbbada04657fcf7cbeb34d3d40

root@instance-1:~/infracloud/csvserver/solution# docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS      NAMES
cd269201c359   infracloudio/csvserver   "/csvserver/csvserver"   5 seconds ago   Up 4 seconds   9300/tcp   sweet_meitner
```
**Instructions**

- Try to mount the `inputFile` file as bind mount and destination file name should be `inputdata` as container app expecting that name.
- Check the container state. It should be up and running.

**Login to container and check the IP and App url**
```sh
root@instance-1:~/infracloud/csvserver/solution# docker exec -it cd269201c359 bash

[root@cd269201c359 csvserver]# ls
csvserver  inputdata

[root@cd269201c359 csvserver]# netstat -tulnpa
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp6       0      0 :::9300                 :::*                    LISTEN      1/csvserver

[root@cd269201c359 csvserver]# curl http://localhost:9300
```
<!DOCTYPE html>
<html>
<head>
  <title>CSV Server</title>
  <style>
  th, td {
    padding: 5px;
  }
  </style>
</head>
<body>
<!-- Y3N2c2VydmVyIGdlbmVyYXRlZCBhdDogMTY0MzU2MDY5Mw== -->
<h3>Welcome to the CSV Server</h3><table><tr><th>Index</th><th>Value</th></tr><tr><td>0</td><td> 574</td></tr><tr><td>1</td><td> 186</td></tr><tr><td>2</td><td> 39</td></tr><tr><td>3</td><td> 570</td></tr><tr><td>4</td><td> 466</td></tr><tr><td>5</td><td> 318</td></tr><tr><td>6</td><td> 231</td></tr><tr><td>7</td><td> 575</td></tr><tr><td>8</td><td> 671</td></tr><tr><td>9</td><td> 350</td></tr></table></body></html>

**Instructions**

- Login to the running container and list the active ports.
- In this container, port 9300 is in listening state and mapped to process `csvserver`.
- As the host port was not defined while running the container, lets try to hit the app url from the container it self by executing `curl http://localhost:9300`. The result should be as above.

**Run the container with ENV variable Host Port**

```sh
root@instance-1:~/infracloud/csvserver/solution# docker run -d -v "$(pwd)"/inputFile:/csvserver/inputdata -e CSVSERVER_BORDER=Orange -p 9393:9300 infracloudio/csvserver
ef186c3858ce96e5795e591ddc507750877d9adea3c51f1a130e07bc9fa1470d
```

**Hit the URL from host by passing Host Port**
```sh
root:solution# curl http://localhost:9393
```
<!DOCTYPE html>
<html>
<head>
  <title>CSV Server</title>
  <style>
  th, td {
    padding: 5px;
  }
  </style>
</head>
<body>
<!-- Y3N2c2VydmVyIGdlbmVyYXRlZCBhdDogMTY0MzU2MjEwNw== -->
<h3 style="border:3px solid Orange">Welcome to the CSV Server</h3><table><tr><th>Index</th><th>Value</th></tr><tr><td>0</td><td> 574</td></tr><tr><td>1</td><td> 186</td></tr><tr><td>2</td><td> 39</td></tr><tr><td>3</td><td> 570</td></tr><tr><td>4</td><td> 466</td></tr><tr><td>5</td><td> 318</td></tr><tr><td>6</td><td> 231</td></tr><tr><td>7</td><td> 575</td></tr><tr><td>8</td><td> 671</td></tr><tr><td>9</td><td> 350</td></tr></table></body></html>

**Output**
- Now http response being generated with Orange bordered heading.

**Create part-1-output file**
```sh
root@instance-1:~/infracloud/csvserver/solution# curl -o ./part-1-output http://localhost:9393/raw
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   153  100   153    0     0   149k      0 --:--:-- --:--:-- --:--:--  149k
```
**Generate the container log file**

```sh
root@instance-1:~/infracloud/csvserver/solution# docker logs 9b8018c8f5e5 >& part-1-logs
```

