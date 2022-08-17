#!/bin/bash
sshpass -p '123456789' ssh ben2@192.168.1.2 'mkdir Net4U && cd Net4U && touch 1.txt 2.txt 3.txt 4.txt && tar -cvzf Net4u.tgz 1.txt 2.txt 3.txt 4.txt'
