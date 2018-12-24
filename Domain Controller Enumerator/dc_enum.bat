REM ##################################################
REM # Tool    : Domain Controller Enumerator         #
REM # Version : 1.0                                  #
REM # Runs on : Windows                              #
REM # Source  : https://github.com/pr2h/             #
REM # .bat file                                      #
REM ##################################################
echo ------------------------------------------------------------------------------------------------- > dc_enum_out.txt
echo "Computer Domain:" >> dc_enum_out.txt
systeminfo | findstr /B /C:Domain >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "User Domain:" >> dc_enum_out.txt
echo %userdomain% >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "Computer Domain Name:" >> dc_enum_out.txt
wmic computersystem get domain >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "nltest /dclist:%userdomain%" >> dc_enum_out.txt
nltest /dclist:%userdomain% >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "LOGONSERVER:" >> dc_enum_out.txt
echo %LOGONSERVER% >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "nslookup -type=any %userdnsdomain%" >> dc_enum_out.txt
nslookup -type=any %userdnsdomain% >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
echo "_ldap._tcp.dc._msdcs.DOMAIN_NAME" >> dc_enum_out.txt
set type=all >> dc_enum_out.txt
_ldap._tcp.dc._msdcs.%userdomain% >> dc_enum_out.txt
echo ------------------------------------------------------------------------------------------------- >> dc_enum_out.txt
