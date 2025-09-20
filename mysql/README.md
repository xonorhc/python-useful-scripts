# PyMySQL

Cliente MySQL feito em Python Puro

[Doc](https://pymysql.readthedocs.io/en/latest/)
[Pypy](https://pypi.org/project/pymysql/)
[GitHub](https://github.com/PyMySQL/PyMySQL)

Intall: `pip install PyMySQL types-pymysql`

## MySQL with Docker

Iniciar o mysql: `docker-compose up -d`

> [!NOTE]
> Verificar o nome do container `docker ps -a`
> Iniciar o container `docker start <container-name>`
> Parar o container `docker stop <container-name>`

Acessar usando CLI: `docker exec -it mysql-db-1 mysql --user=myuser --password=password mydb`

Acessar usando LazySQL: `lazysql mysql://myuser:password@localhost/mydb`
