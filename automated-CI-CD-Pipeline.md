# Courtesy of Brett Kugler , Brett.kugler@gdt.com
Using Jenkins to deploy a heat template
1. Create a Jenkins service following the instructions found here:
Installing Jenkins - https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins+on+Red+Hat+distributions

We are using a minimal CentOS 7 install so some steps may be different depending on your choice of OS (denoted by +)

+sudo yum install wget
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins
+yum install java-1.7.0-openjdk
+yum install git

+firewall-cmd --zone=public --add-port=8080/tcp --permanent
+firewall-cmd --zone=public --add-service=http --permanent
+firewall-cmd --reload

+yum group install "Development Tools"
+yum install python-devel
+easy_install pip
+pip install python-openstackclient
+pip install python-heatclient

2. Start the Jenkins service
sudo service jenkins start
sudo chkconfig jenkins on

Tieing Jenkins to GitHub 
1. Create a new job in Jenkins (Freestyle Project)
2. Under Source Code Management select Git and paste the URL to your repository.
3. Under Tiggers, select Poll SCM and enter '* * * * *' in the schedule box.
4. Select Build -> Add Build Step -> Execture Shell:
	python -c "print 'OpenStack Heat Deploy'"
	source /var/<project>-openrc.sh **** See the next section for details on how to access this file
	heat stack-create -f two_tier.yaml STACKONE
	nova list
5. Note that the Heat template is in the GitHub repository

Firing a Heat template from Jenkins using OpenStack CLI tools
1. Log into your OpenStack instance and browse to Project -> Access & Security -> API Access and click
	Download OpenStack RC File
2. Copy the RC file to /var to match the path in the build script above (step 4)
3. Edit the RC file and substitute the username and password for your environment
4. You can now fire off the Jenkins build or make a change to the GitHub repo and verify the change fired off the Jenkins build and created the VMs from the Heat template
