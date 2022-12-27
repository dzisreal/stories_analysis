Sau khi giai nen, keo het ve path /usr/local/<dat lai ten>, eg: /usr/local/kafka

---------------------------------------------------
Kafka:
sudo systemctl start zookeeper
sudo systemctl start kafka

Create Topic:kafka-topics.sh --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic topic_test

Xem messages cua topic: 

kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic topic_test 

Xoa topic: kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic <topic_name>

Xem list topic: kafka-topics.sh --list --bootstrap-server localhost:9092

--------------------------------------------------------
Hadoop:
cd /usr/local/hadoop/sbin
./start-dfs.sh
./start-yarn.sh
co loi thi stop all bang "./stop-all.sh" roi "hdfs namenode -format" sau do start lai
UI: localhost:9870
yarn resource manager: localhost:8088

neu loi k run duoc data node, xem log, xem log lay datanode clusterID, chay "stop-dfs.sh" roi chay "hdfs namenode -format -clusterID <datanode clusterID>"



------------------------------------------------------
Spark:
cd /usr/local/spark/sbin
./start-all.sh, UI: localhost:8080
./stop-all.sh de tat

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 Spark.py

-------------------------------------------------------
Hive:
cd $HIVE_HOME/bin
hiveserver2
beeline
!connect jdbc:mysql://localhost/metastore_db

create table cryptodata (symbol string, price float, time_ timestamp, volume int) STORED AS PARQUET LOCATION '/user/hadoop/data';



-------------------------------------------------------
Superset:
localhost:8088

export FLASK_APP=superset ( neu loi flask...)

account: admin/1
superset run -p 8089 --with-threads --reload --debugger






