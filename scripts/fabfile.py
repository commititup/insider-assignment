from   fabric import *

connect_kwargs = {"key_filename":["<keyfile path for ssh>"]}
c = Connection(host="<hostname>", user="<user>", connect_kwargs=connect_kwargs)


@task
def bootstrap_node(ctx):    
     c.run("sudo apt-get update")
     c.run("sudo apt-get install nodejs nginx mailutils -y")

@task
def config_nginx(ctx):
     c.put('nginx_conf',remote='.')
     c.put('nginx.key', remote='.')
     c.put('nginx.crt', remote='.')
     c.run("sudo mkdir /etc/nginx/ssl")
     c.run("sudo mv nginx.key nginx.crt /etc/nginx/ssl")
     c.run("sudo mv nginx_conf /etc/nginx/sites-available/default")
     c.run("sudo systemctl restart nginx")
     c.run("sudo systemctl enable nginx")

@task 
def config_express_app_with_apt(ctx):
     c.run("sudo apt-get install node-server")

@task
def start_nginx_app(ctx):
    c.run("sudo systemctl start nginx")

