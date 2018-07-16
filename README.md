# RoboNikto

Robot Framework Library for Nikto -  Web Server Scanner

**Supports Python 2**

### Install Instructions
- Clone Nikto repo from [here](https://github.com/sullo/nikto)
- Edit the `program/nikto.conf` and change the `NIKTODTD=docs/nikto.dtd` to absolute path
- Clone the RoboNikto Library from [here](https://github.com/we45/RoboNikto) 
- Install with command: `python setup.py install`
- Create a `.robot` file that includes the keywords used by RoboNikto Library


### Keywords

`run nikto`  

`| run nikto  | target host | target_port  | nikto report path |`

* target host:  host for which nikto need to be run against
* target_port : port for which nikto need to be run against
* nikto report path: where your nikto report will be exported

**Note:**

- Report path should be an absolute path and don't specific any extension in the file name
- Check the `RoboNikto.robot` inside the test directory for sample robot script