Spark/UCSD Integration Readme

by: Brett Kugler (brett.kugler@gdt.com)
for: Cisco APO Cloud Rotation Program

For this simple integration, you will need a Spark developer account and your Spark Account Key.

Files:
	sparkroom.cfg - this is where you will put all your key information and URLs
	sparkbridge.py - Due to the Lab UCSD not having outbound connectivity, this file is required to bridge UCSD and Spark and should live on the Lab jumphost
	requirements.txt - all modules required to run this python application in a fresh virtualenv
	UCSD_HTTP_workflow_script.js - the workflow script component of a UCSD Workflow Template