all: *

INSTALL_INIT = install

.PHONY: all

install:
	mkdir -p $(DESTDIR)/usr/local/node-server
	mkdir -p $(DESTDIR)/etc/systemd/system
	cp -r src/* $(DESTDIR)/usr/local/node-server
	cp -r etc/systemd/system/node-server.service $(DESTDIR)/etc/systemd/system/


