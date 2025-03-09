#!/usr/bin/env bash

rsync --info=DEL --verbose --recursive --delete --checksum ~/github/upload/ root@web.localdomain:/var/www/html/
