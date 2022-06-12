Sotwares required for the project:
For Designing and 3D printing:
	1. Fusion 360
	2. CURA software
For programming:
	We used Raspbian operating system for entire controlling
	1. Python 3.7 or above(required modules need to be installed)
	2. Anaconda environment
For Webstreaming:
	1. OpenCV
	2. Django
For Simulation
	1. Pybullet and it's dependencies


Setup:
Designing and 3D printing setup:
	Goto https://www.autodesk.in/products/fusion-360/overview?term=1-YEAR 
	choose how you want to install Fusion360(Free trail for 30 days or Student 
	version).
	Follow instructions provided in website for setting up Fusion 360.  
	Goto https://ultimaker.com/software/ultimaker-cura for installing CURA software. 

programming setup:
Goto Raspberry pi terminal
	Type python3 --version
	If python3 is present goto https://gitlab.com/custom_robots/spotmicroai
	Install and extract all files from zip

Webstreaming:
	There is an excellent documentation on how to install opencv on Raspberry pi 
	in the below link(Follow steps mentioned to insatll opencv)
	https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
	Follow instructions specified in below link for installing django on Raspberry pi

Simulation:
Goto https://docs.anaconda.com/anaconda/install website.
	Choose ur respective operating system.
	Click on Download the Anaconda installer
	Double click the installer to launch
	Navigate to Anconda prompt
	Find pip version using pip --version
	Install pybullet using the following command conda install -c conda-forge pybullet
	(dependencies were automatically installed)



