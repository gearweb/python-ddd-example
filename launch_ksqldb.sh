#!/bin/bash
docker-compose -f docker-compose.yml up -d
docker exec zookeeper kafka-topics --create --zookeeper localhost:2181  --replication-factor 1 --partitions 1 --topic users
