#P0st3r

`.__  _,     ,  _,
[__)|.|  __-+-'_) ._.
|   |_| _)  | ._) [`

##What it is ? 

An minimalistic tool for do huge amounts of $_POST's requisitions

##Why is useful ?

Well , for benchmarking , fuzzing , and flood things ( MUHAHAHA !)

##Example :

`$ - python p0st3r.py -u http://127.0.0.1/ -p "1:1 2:2 3:3 4:4" -r 666 -d 5`

##Usage :

|-h, --help         |   show this help message and exit
|-u http://url.com/,| --url http://url.com/
|                   |   URL to request
|-p variable:data,  | --parameters variable:data
|                   |   Parameters for $_POST
|-r x, --requests x |   Number of requests
|-d x, --delay x    |   Delay ( sec ) for each request


##Upcoming in next versions : 

1. Proxy 
2. Accept an list of parameters
3. Threads
4. $_GET type


