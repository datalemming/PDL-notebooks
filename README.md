# PDL-notebooks

The two Jupyter notebooks that I used for my talk to PyData London are here.  They will act as references for the code to interact with Riak through Python and PySpark.  The table creation notebook is also included if people want to run the entire set for themselves.  The load script is a stand alone Python script.  On my VM (8GB RAM single processor) it takes around 48 minutes to complete as I have not built in parallel processing of any description as I am lazy and this is a demo!  There should be no issue with the datetime objects.  If you experience one, please contact me and I will investigate. 

If people want to recreate the entire demo themselves they need to do the following:

1. Request the data file
2. Install Riak TS - there is excellent documentation on how to do this on [the basho website](http://docs.basho.com)
3. Install the Basho Riak python library ("pip install riak").
3. Create the relevant table using the notebook "Create table aarhus13-4ts1.3".  PLEASE remember to follow the noted instructions after the operating cells to change the replication factor, or performance on a single node will suffer.
4. Run the "load-data-ts13.py" script to load the raw data
5. Run the "PyData Querying examples notebook".
6. If you want to explore PySpark and Riak :
  
  a. Install Apache Spark 1.6 or above (God help you!)
  
  b. Download the Riak Spark Connector (see the website above to find the download link and it is very easy to do) and remember you must start jupyter as follows:

"SPARK_CLASSPATH=/path/to/where/ypu/put/the/connector jar jupyter notebook" - you will want to install the python findspark module.

If anyone wants the dataset to run the notebooks, please contact me at setheridge@basho.com. The csv file is 120MB zipped, so be warned we will have to be artistic about transfering it.
