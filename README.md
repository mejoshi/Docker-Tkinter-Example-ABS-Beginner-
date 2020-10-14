# Docker Project

## Docker 
Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

## Tkinter
The Tkinter module (“Tk interface”) is the standard Python interface to the Tk GUI toolkit from Scriptics (formerly developed by Sun Labs).
Both Tk and Tkinter are available on most Unix platforms, as well as on Windows and Macintosh systems. Starting with the 8.0 release, Tk offers native look and feel on all platforms.
Tkinter consists of a number of modules. The Tk interface is provided by a binary extension module named _tkinter. This module contains the low-level interface to Tk, and should never be used directly by application programmers. It is usually a shared library (or DLL), but might in some cases be statically linked with the Python interpreter.

## Wordpress
WordPress is the simplest, most popular way to create your own website or blog. In fact, WordPress powers over 37.6% of all the websites on the Internet. Yes – more than one in four websites that you visit are likely powered by WordPress.

### Integration of Docker - Tkinter 

1. Mannual Config

- mysqlContainerName > MySQL Container name
- mySQLUsername > Username
- mySQLPassword > User's password
- mySQLDatabase > DB name
- createVolWordpress  > Volume name for Wordpress
- wordpressContainerName > Wordpress Container name
- portNumber > ex. 8080
- portNumber2 > ex. 80
- mysqlContainerName > MySQL Container name

2. Automatic COnfig

but In automatic config., you don't have to put all these thing, Just one click start and one click stop. I've use docker compose here.

Here is the screenshot 1, 

![](images/d.png)

Screenshot 2,

![](images/a.png)

Screenshot 3,

![](images/b.png)

Screenshot 4,

![](images/c.png)

