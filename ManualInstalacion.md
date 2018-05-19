# Manual para la instalación de la aplicación
## Github
#### Realice un Fork del proyecto en su cuenta de github.

## Heroku
#### Crear cuenta de heroku
Diríjase a la pagina de [Heroku](https://www.heroku.com/) y cree una cuenta.

Una vez haya creado su cuenta, diríjase a el [dashboard](https://dashboard.heroku.com/apps) y cree una nueva aplicación.

Asígnele un nombre a su aplicación, recordando que debe estar disponible.

Una vez creada, busque la opción resources y haga click en esta.

#### En la pestaña resources, para agregar la base de datos postgres, haga click en el botón ```Find more add-ons```, y busque la opción [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)

#### Para obtener las variables de entorno de la base de datos, click en el ```add-on de heroku-postgres``` y ubíquese en la pantalla ```Settings```, en este punto debe hacer click en el botón ```view Credentials```. Esto le mostrara un listado de variables, las cuales debe completar en las variables de entorno que encontrara en ```settings``` de su aplicación en Heroku al hacer click en ```reveal config vars```.

#### Debe agregar las variables de entorno de la siguiente forma:
*  ```NAME_DB``` las credenciales de su Database en heroku-postgres
*  ```USER_DB``` las credenciales de su User en heroku-postgres
*  ```PASSWORD_DB``` las credenciales de su Password en heroku-postgres
*  ```HOST_DB```las credenciales de su Host en heroku-postgres
#####
## Azure
#### Cree una cuenta en [Azure](https://azure.microsoft.com/es-es/free/students) , (se aconseja crear la cuenta con las credenciales uniandes, ya que tiene convenios con esta plataforma) llene los campos con su información. Una vez creada, en el [portal](https://portal.azure.com) en el panel de servicios encontrar ```Cuentas de almacenamiento```. 

Allí agregue una cuenta de almacenamiento diligenciando el formulario, tenga en cuenta que  el nombre que se le asigne 
se tendrá que usar en las variables de entorno. Cuando se le notifique la creación, entre y seleccione los ```servicios Blobs```, y agregue un contenedor llamado ```pictures```, y deje el nivel de acceso en privada. 

Solo resta sacar las variables de entorno necesarias para la configuración de heroku, vuelva al almacenamiento creado y 
en configuraciones encontrará dos posibles ```ACCOUNT_KEY``` llamados key en el la opción de ```llaves de acceso```. 

También debe ir a ```firma de acceso compartido```, en los servicios compartidos seleccione solo blob y en permisos permitidos solo lectura. Configure un rango de fecha de caducidad adecuado y luego ya podrá generar la cadena de conexión y SAS

#### Debe agregar las variables de entorno en heroku:
*  ```ACCOUNT_NAME``` el nombre de la cuenta de almacenamiento que asignó
*  ```ACCOUNT_KEY``` clave de algún key en el menú de claves de acceso 
*  ```SAS``` token sas generado en firma de acceso compartido 
*  ```SORAGE_URL``` https://```nombre del almacenamiento que usted creo```.blob.core.windows.net/pictures/

## Servidor de correo electrónico
La aplicación cuenta con un servido de correo electrónico SMTP, para que el servicio de correo funcione correctamente se deben declarar de las siguientes variables de entorno. Consulte con su servidor de correo estos parámetros, acá se muestra un ejemplo para correos electrónicos de Gmail. 

* ```EMAIL_HOST```=smtp.gmail.com
* ```EMAIL_HOST_USER```= <cuenta>@gmail.com
* ```EMAIL_HOST_PASSWORD```=<contraseña>
* ```EMAIL_PORT```= 587
* ```EMAIL_USE_TLS```=True

## Heroku deployment

Ya con las variables de entorno definidas, se puede proceder a realizar el despliegue. 

* En el su aplicación en heroku dirígase a ```deploy``` 
* En ```Deployment method``` conectese con la cuenta de github donde realizó el fork del proyecto. 
* Esto le habilitará ```Connect to GitHub``` busque CatalogoCTE y seleccione ```connect```
* En ```Manual deploy``` realice un deployment de la rama master haciendo click en ```Deploy Branch```

## Configuración inicial base de datos

Ya con el primer despliegue se puede configurar la base de datos siguiendo estos pasos:

* En heroku en su aplicación en la parte superior derecha esta un botón ```more``` y seleccione ```run console```
* Secuencialmente ingrese los siguientes comandos: 
```
python manage.py migrate
python manage.py makemigrations posts   
python manage.py sqlmigrate posts 0001
python manage.py migrate 
```
nota: Despues de ingresar un comando y esperar las repuestas de la consola debe volver a abrir otra ```run console ```

* Por último ejecute el comando para crear la cuenta del administrador
```
python manage.py createsuperuser
```

En la consola se le solicitará ingresar un nombre , un correo y asignar una contraseña al administrador. 

## Configuración perfil administrador 

En este punto debe volver a realizar el deployment de la rama master, una vez terminado este despliegue se requiere hacer unas configuraciones en el perfil del administrador.

* Abra el modulo administrador de su aplicación ```https://<NOMBRE DE SU APP EN HEROKU>.herokuapp.com/admin/```
* Inicie sesión y en ```AUTHENTICATION AND AUTHORIZATION``` abra  ```users```
* Seleccione la cuenta del administrador, edite ```Personal info``` y asigne el rol administrador al perfil y guarde los cambios. 

## Use la aplicación catálogo

Solo resta entrar a la pagina donde esta desplegado su proyecto ```https://<NOMBRE DE SU APP EN HEROKU>.herokuapp.com/``` y crear las cuentas de los otros miembros de la organización. 



