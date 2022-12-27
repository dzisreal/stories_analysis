

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


# In[4]:


#Create Sparksession and Sparkcontext
spark = (SparkSession
         .builder
         .appName('CryptoConsumer')
         .getOrCreate())
sc = spark.sparkContext.setLogLevel("WARN")


# In[ ]:


schema = schema = StructType([ 
        StructField("symbol", StringType(), True),
        StructField("price" , StringType(), True),
        StructField("time_" , TimestampType(), True),
        StructField("volume" , StringType(), True),
        ])


# In[6]:


# Create stream dataframe setting kafka server, topic and offset option
sampleDataframe = (
        spark.read.format("kafka")   #for Batch Process
        # spark.readStream.format("kafka")    #for Stream Process
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "topic_test")
        .option("startingOffsets", "earliest")
        .load()
        .select(from_json(col("value").cast("string"), schema).alias("parsed_value"))
        .select(col("parsed_value.*"))
    )


# In[ ]:


df = sampleDataframe.select('*')

#Batch Process
# df.write.save('/user/hadoop/data', format='parquet', mode='append')

#Stream Process
# run = df.writeStream \
#    .outputMode("append") \
#    .format("parquet") \
#    .option("path", "/user/hadoop/data") \
#    .option("checkpointLocation", "/user/hadoop/checkpoint") \
#    .start()
# run.awaitTermination()

df.write.format('jdbc').options(
      url='jdbc:mysql://localhost:3306/crypto_data',
      driver='com.mysql.cj.jdbc.Driver',
      dbtable='crypto',
      user='admin',
      password='admin').mode('append').save()

