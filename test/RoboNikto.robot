*** Settings ***
Library     RoboNikto   /home/umar/Desktop/RobotFramework-Dev/nikto-master/program/nikto.pl

*** Variable ***
${TARGET_HOST}  127.0.0.1      
${TARGET_PORT}  80
${EXPORT_REPORT}  /home/umar/Desktop/dev/RoboNikto/test/localhost_nikto

*** Test Case ***

Run Nikto against the target host 
    run_nikto  ${TARGET_HOST}    ${TARGET_PORT}  ${EXPORT_REPORT}