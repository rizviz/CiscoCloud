# Becoming a Command Line Commando

## Installing the Openstack Command Line tools

The Openstack Command Line tools are essentially a Python library.  If you are not familiar with Python, it is a modern interpreted language that has a simple syntax and is easy to learn while also being full-featured and extremely powerful.  

So, the first step in installing the Openstack Command Line tools is to first get Python installed.  One important thing to understand about Python is that there are currently two distinct versions of Python; Python 2 and Python 3.  The Openstack Openstack Command Line tools are currently only work with the older Python 2 and so that is what we will install.

Below are some great tutorials if you need help installing Python 2 on Windows, Mac, or Linux:

[Installing Python on Linux](http://docs.python-guide.org/en/latest/starting/install/linux/)

[Installing Python on Mac OS X](http://docs.python-guide.org/en/latest/starting/install/osx/)

(If you run into any issues, feel free to open an issue on this Github repository for help)

## Becoming Pythonic

Once you have Python installed pat yourself on the back and bask in the knowledge that your assimiliation into the Python collective has begun!

Now, lets test out your Python and make sure it works.  Open you command line and type:

```
$ python --version
```

You should get back something like: `Python 2.7.11`

## Using `pip` to install the Openstack Command Line tools

Pip is the Python package manager and will manage all the dependencies that any library requires.  Its like apt-get for Python.

We first need to make sure it is installed though.  It usually comes built in to most Python installs these days.

```
pip list
```

Output you should see:

```
Flask (0.10.1)
itsdangerous (0.24)
Jinja2 (2.8)
MarkupSafe (0.23)
pip (8.1.1)
setuptools (18.2)
virtualenv (15.0.1)
Werkzeug (0.11.5)
```

Note: Your install may show different libraries.

Now lets install the Openstack Command Line tools:

```
pip install python-openstackclient
```

## Getting the “RC" file

Every project gets an rc file when it is created.

1)	Log onto Horizon (The Openstack Web Dashboard) and go to your project  
2)	Navigate to Access and Security>API Access  
3)	Click the button “Download Openstack rc file”.  
![https://i.imgur.com/VZc37UR.png](https://i.imgur.com/VZc37UR.png)

4)	store the file in an easily found directory.  It will have an “.sh” suffix  

## Source the RC file in command line

1)	open terminal and navigate to folder where rc file is located  
2)	type:

```
source MyProject.sh
```

3)	enter your openstack password when prompted  

## Using the Openstack Command Line tools


#### 1)	Test your setup by typing simple command such as:

```
$ nova list
```

#### 2)	Create a keypair

You can create a new key pair by using the keypair-add command for nova. You pass a name for the key pair as an argument. The public key is then stored in your user profile via the API. The output of the command is the private key.

```
nova keypair-add myNewKey > ~/.ssh/myNewKey_rsa
```

#### 3)	Identify your network name, flavors, images, and security groups by issuing following commands :

```
$ nova flavor-list
```

```
$ nova image-list
```
```
$ nova network-list
```
```
$ nova secgroups-list
```


#### 4)	Create a simple instance by leveraging the “nova boot” command!

a.	Nova boot command syntax is :

``` 
nova boot --image imageID --flavor flavorID --nic net-id=nicID <Instance Name> 
```

example:

```
nova boot --image "Ubuntu 14.04 LTS" --flavor "Standard"  --nic net-id=705a8134-a01e-4282-836e-10cb40540283 --security-groups "Allow All" --key-name myNewKey cliCreatedTestInstance
```
	
#### 5)	Show details of the instance

```
nova  show  cliCreatedTestInstance
```


#### 6)	Connect via ssh using the keypair to the newly created instance

```
ssh -i ~/.ssh/myNewKey_rsa user@10.128.134.129
```

# Have Fun!!!







