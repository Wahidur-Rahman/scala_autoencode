

# Requriements  
* Python 2.7.8 or later (Python 3.x is not supported)  
* open-mpi 1.8.1 or later (other MPI implementation supported by mpi4py should also be OK)  
* Numpy 1.8.1 or later  
* Scipy 0.14.0 or later  
* mpi4py 1.3.1 or later  
* genism (Word2vec dependency package)  
* Jdk1.8.0_152   
`The above environment is suitable for Linux system. If you are a windows system, we recommend that you install anaconda.At the same time you need to replace open-mpi, the specific steps are as follows:`  
* Install the v8 version of Microsoft MPI  
* run `conda install -c dhirschfeld mpi4py=1.3.1.post152.g2b55fb2` to install the 1.3.1 version of mpi4py   

Note: `we find some API(s) of mpi4py or open-mpi had been changed in recent versions. If you meet errors such as "TypeError: bcast() takes at least 1 positional argument (0 given)", please fall back to the versions as above.`  

Python is easy to install. open-mpi is usually available on most Linux platforms. Numpy, Scipy and mpi4py are available from pip. Alternatively, you can install all these softwares from source code if you like or you do care about efficiency.   

# Example  

```
# install python, python development files and pip
sudo apt-get install python python-dev python-pip
# install open-mpi runtime and development files and tools
sudo apt-get install openmpi-bin libopenmpi-dev
# install mpi4py
sudo pip install mpi4py
# install numpy and scipy
sudo apt-get install g++ gfortran build-essential
sudo apt-get install libopenblas-dev liblapack-dev
sudo pip install numpy scipy
```


# Execution  

## Corpus  

### Extract representations  

run `java -Dfile-encoding=utf-8 -jar scala_parser.jar -identifier/-AST  {input file path}`    
*  `-identifier`: extract representation 1  
*  `-AST`: extract representation 2   
* `input file path` :  project path to be tested  

After running the above command, you will get a `sample-training-file.txt`. You need to put this file into the `input` folder.  

## Learn Word embeddings  

### run_word2vec.sh  

`./run_word2vec.sh`  


## Learn Sentence embeddings  

In this stage we use a recursive autoencoder which recursively combines embeddings - starting from the word embeddings generated in the previous stage - to learn sentence-level embeddings. Then, distances among the embeddings are computed and saved in a distance matrix which can be analyzed in order to discover similarities among the sentences in the corpus.  

### Recursive Autoencoder  

run `./mpi-train.sh {coreNum}`  

* `coreNum`:  Use the number of cores in your computer  

run `./compute-vector.sh`  

At this time, a `sample-training-file.vec.txt` will be generated in the output folder. And then  

run `java -Dfile-encoding=utf-8 -jar scala_parser.jar -find-source-code {input file path} {sample-training-file.vec.txt path}`  

* `input file path`:  project path to be tested    
# Execution Example   
```
java -Dfile-encoding=utf-8 -jar scala_parser.jar -identifier D:/Git/spark/  
mv sample-training-file.txt input/ 
./run_word2vec.sh  
./mpi-train.sh 2  
./compute-vector.sh  
cd input
mv sample-training-file.vec.txt ..
java  -Dfile-encoding=utf-8 -jar scala_parser.jar -find-source-code D:/Git/spark/  /output/sample-training-file.vec.txt
```

