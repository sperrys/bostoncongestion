
# Inrix

This folder has all information regarding the inrix data set and it's parsing. 

### Getting Started 

1. Have python3 installed 
2. Install virtualenv globally through pip `pip install virtualenv`
3. Clone this repo with `git clone `
4. Create the virtual environment with `virtualenv -p python3 env`
5. Activate the environment with `source env/bin/activate`
6. Install dependencies with `pip install -r requirements.txt`



#### main.py 

The program for parsing the inrix data from a per **month** perspective. 

Run the main script with  `python main.py`

##### Command Line Options
 
* `--data` 
    * This variable specifies the input directory of the **Inrix** data set. This directory should have an unzipped version
    * **Required**: YES
    * **Default**: YES, `/data` directory
    * **Options**: Any valid directory path
* `month`
    * The name of the month that is being currently processed
    * **Required**: YES
    * **Options**: `True` or `False`
* `--unzip`
    * Whether or not to unzip the files in the data directory
    * **Required**: NO
    * **Default**: YES, `False` directory
    * **Options**: `True` or `False`
        
 
##### Examples

Parses from the  `data` directory, all available data for `January

`python main.py January`

