# Web Scrapping News

In this project we try to get the news with the API of the news website, then we creating a json file with all the news, at last we can run these project using docker.


## Installation and Running

The first thing to do is to install the dependencies using pip install -r requirements.txt

* You can run the project directly in the command line at the root directory with the comman *python main.py*

* If you want to run it with docker you need to first build the image using *"docker build -t tag_you_want ."*   this command only work if you are in the root directory

* At last with the docker to run you can use this command *"docker run -v root_project:/usr/src/app tag_you_want"*

tag_you_want: Just a name to reference your docker image

root_project: Where the directory is in your PC for Windows you need to use absolute path for other users you can use related paths or pwd command in brackets.

Hope you find this project helpful
