
Enter user-name: sys as sysdba
Enter password: 

alter session set "_ORACLE_SCRIPT"=true;

commit;

create user PORTAFOLIO identified by PORTAFOLIO;

grant all privileges to PORTAFOLIO;

commit;