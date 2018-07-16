"""
Nikto Python Library 
written By: Umar Farook
Nikto Command: perl nikto.pl -h <host> -p port> -o <report_namae>

"""
import subprocess


class RoboNikto(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self,nikto_path):
        self.nikto_path = nikto_path

    def run_nikto(self,host,port,export_report):
        output = export_report + '.xml'
        cmd = ['perl',self.nikto_path,'-h', host, '-p', port, '-o', output]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in proc.stdout:
            print(line.decode('utf-8').strip())
        # print("Scan is completed on " + datetime.datetime.now().strftime("%I:%M%p"))

