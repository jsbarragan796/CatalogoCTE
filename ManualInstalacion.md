# Manual para la instalación de la aplicación
## GITHUB
#### Realice un Fork del proyecto en su cuenta de github.

## Heroku
#### Crear cuenta de heroku
#### Dirígase a la pagina de [Heroku](https://www.heroku.com/) y cree una cuenta.

#### Una vez haya creado su cuenta, diríjase a el [dashboard](https://dashboard.heroku.com/apps) y cree una nueva aplicación.

#### Asígnele un nombre a su aplicación, recordando que debe estar disponible.

#### Una vez creada, busque la opción resources y haga click en esta.

#### En la pestaña resources, para agregar la base de datos postgres, haga click en el botón Find more add-ons, y busque la opción [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
#### Para obtener las variables de entorno de la base de datos, click en el add-on de heroku-postgres y ubíquese en la pantalla Settings, en este punto debe hacer click en el botón view Credentials. Esto le mostrara un listado de variables de entorno, las cuales debe completar en las variables de entorno que encontrara en los ajustes de su aplicación en Heroku al hacer click en ```reveal config vars```.

#### Debe completar la variables de entorno de la siguiente forma:
*  ```NAME_DB``` las credenciales de su Database en heroku-postgres
*  ```USER_DB``` las credenciales de su User en heroku-postgres
*  ```PASSWORD_DB``` las credenciales de su Password en heroku-postgres
*  ```HOST_DB```las credenciales de su Host en heroku-postgres
#####
## Azure
#### Cree una cuenta en [Azure](https://azure.microsoft.com/es-es/free/students) , (se aconseja crear la cuenta con las credenciales uniandes, ya que tiene convenios con la plataforma) llene los campos con su información. Una vez creada, en el [portal](https://portal.azure.com) en el panel de servicios encontrar Cuentas de almacenamiento. 

Allí agregue una cuenta de almacenamiento diligenciando el formulario, tenga en cuenta que  el nombre que se le asigne 
se tendrá que usar en las variables de entorno. Cuando se le notifique la creación, entre a 
esta y seleccione los servicios Blobs, y agregue un contenedor llamado ```pictures```, y deje el nivel de acceso en privada. 

Solo resta sacar las variables de entorno necesarias en la configuración de heroku, vuelva al almacenamiento creado y 
en configuraciones obtenga el ```ACCOUNT_KEY``` en el la opcion de llaves de acceso. 

También debe ir a firma de acceso compartido, en los servicios compartidos seleccione solo blob y en permisos permitidos solo lectura 
configure un rango de fecha de caducidad adecuado. Luego de llenar el formulario puede generar la cadena de conexión y SAS
#### Debe agregar las variables de entorno en heroku:
*  ```ACCOUNT_NAME``` el nombre de la cuenta de almacenamiento que asignó
*  ```ACCOUNT_KEY``` clave de algún key en el menu de claves de acceso 
*  ```SAS``` token sas generado en firma de acceso compartido 
*  ```SORAGE_URL`` https://```nombre del almacenamiento que usted creo```.blob.core.windows.net/pictures/
