
For apache

add /etc/httpd/conf/httpd.conf

```
LoadModule wsgi_module modules/mod_wsgi.so
 
WSGISocketPrefix /var/run/wsgi
<VirtualHost *:80>
    ServerName example.com
 
    DocumentRoot /var/www/html
    <Directory /var/www/html>
        Order allow,deny
        Allow from all
    </Directory>
 
    WSGIDaemonProcess example.com user=apache group=apache threads=5
    WSGIScriptAlias / /home/foo/flask/flasktest.wsgi
    WSGIScriptReloading On
 
    <Directory /home/foo/flask>
        WSGIProcessGroup example.com
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```
