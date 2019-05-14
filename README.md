Assumptions
  - some build server is used to build  debian pacakge and push to apt repo
  - python fabric is install on local to run automated script
  - user runnning with setup commands has sudo privileges without password
  - required Port is opened (25,443)
  
what you need to update:
  - hostname,username,keyfile path in scripts/fabfile.py
  - update email address to receive mail on failure on service stop inside etc/systemd/system/node-server.service file
