
# Preface

This is a set of notes that can be compiled into a book for getting started with Programming like a pro.

# This is a book on solving problems with Computers.

In order to solve problems with computers, we need to understand how does a computer understand human language? It also teaches how to assign tasks to computers in short and precise set of instructions.

# A short history of computer programming languages.

In the world of electronics we learn about instruction sets that small IC (Integrated Circuits) chips understand. Instructions such as ADD, SUB, MUL, MOV, COPY etc. Then we humans learn to weave together these basic instructions in a set of commands that achieve fundamental computer interactions like Creating a folder on the computer, creating a text file to write some text in English, or a set of text in a particular language. From here on, we learn to represent information from these files in various human-perceivable information. 

# Human perceivable information displayed from files.

Some examples are:

1. Text file:
    Programs, Notes, Journals, Calendars, Documentations
2. Image files:
    Pictures from camera, pictures drawn by using a program that facilitates drawing, Image generated from fax machine etc..
3. Audio files
4. Video files

# Algorithms

Algorithms are a means to work with information stored in the files and creating new files. In other words algorithms is about creating and consuming information.

# Basic algorithms

Basic algorithms are about mathematics. How to compute information by application of mathematics that a computer can understand. For instance the following must be considered as the basic problems in algorithms:

##  List of algorithm problems as mentioned on wikipedia page:

I found the page https://en.wikipedia.org/wiki/List_of_algorithms, that claims to list the algorithms. I will try to extract the table of contents here:

List of Algorithms from wikipedia:




```python
import urllib2
```


```python
from bs4 import BeautifulSoup
```


```python
url = "https://en.wikipedia.org/wiki/List_of_algorithms"
```


```python
page = urllib2.urlopen(url)
```


```python
soup = BeautifulSoup(page)
```


```python
toc = soup.find(id="toc").find_all("li")
```


```python
toc_text = [tc.find("a").find(class_="toctext").string for tc in toc]
```


```python
toc_link = [tc.find("a")["href"] for tc in toc]
```


```python
toc_link2 = [url+ext for ext in toc_link]
```


```python
from IPython.core.display import display, HTML
```


```python
html_string = ['<li>' + '<a href="'+ toc_link2[i] + '">'+ toc_text[i] +'</a>' + '</li>' for i in xrange(len(toc_text))]
```


```python
html_string2 = '<ul>' + ''.join(html_string) + '</ul>'
```


```python
display(HTML(html_string2))
```


<ul><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Automated_planning">Automated planning</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Combinatorial_algorithms">Combinatorial algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#General_combinatorial_algorithms">General combinatorial algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Graph_algorithms">Graph algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Graph_drawing">Graph drawing</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Network_theory">Network theory</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Routing_for_graphs">Routing for graphs</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Graph_search">Graph search</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Subgraphs">Subgraphs</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_algorithms">Sequence algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Approximate_sequence_matching">Approximate sequence matching</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Selection_algorithms">Selection algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_search">Sequence search</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_merging">Sequence merging</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_permutations">Sequence permutations</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_alignment">Sequence alignment</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Sequence_sorting">Sequence sorting</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Subsequences">Subsequences</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Substrings">Substrings</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computational_mathematics">Computational mathematics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Abstract_algebra">Abstract algebra</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computer_algebra">Computer algebra</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Geometry">Geometry</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Number_theoretic_algorithms">Number theoretic algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Numerical_algorithms">Numerical algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Differential_equation_solving">Differential equation solving</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Elementary_and_special_functions">Elementary and special functions</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Geometric">Geometric</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Interpolation_and_extrapolation">Interpolation and extrapolation</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Linear_algebra">Linear algebra</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Monte_Carlo">Monte Carlo</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Numerical_integration">Numerical integration</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Root_finding">Root finding</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Optimization_algorithms">Optimization algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computational_science">Computational science</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Astronomy">Astronomy</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Bioinformatics">Bioinformatics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Geoscience">Geoscience</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Linguistics">Linguistics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Medicine">Medicine</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Physics">Physics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Statistics">Statistics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computer_science">Computer science</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computer_architecture">Computer architecture</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Computer_graphics">Computer graphics</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Cryptography">Cryptography</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Digital_logic">Digital logic</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Machine_learning_and_statistical_classification">Machine learning and statistical classification</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Programming_language_theory">Programming language theory</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Parsing">Parsing</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Quantum_algorithms">Quantum algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Theory_of_computation_and_automata">Theory of computation and automata</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Information_theory_and_signal_processing">Information theory and signal processing</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Coding_theory">Coding theory</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Error_detection_and_correction">Error detection and correction</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Lossless_compression_algorithms">Lossless compression algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Lossy_compression_algorithms">Lossy compression algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Digital_signal_processing">Digital signal processing</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Image_processing">Image processing</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Software_engineering">Software engineering</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Database_algorithms">Database algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Distributed_systems_algorithms">Distributed systems algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Memory_allocation_and_deallocation_algorithms">Memory allocation and deallocation algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Networking">Networking</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Operating_systems_algorithms">Operating systems algorithms</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Process_synchronization">Process synchronization</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Scheduling">Scheduling</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#Disk_scheduling">Disk scheduling</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#See_also">See also</a></li><li><a href="https://en.wikipedia.org/wiki/List_of_algorithms#References">References</a></li></ul>



```python

```
