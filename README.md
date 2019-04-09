
# Inrix

This folder has all information regarding the inrix data set and it's parsing. 

### Getting Started 

1. Have python3 installed 
2. Install virtualenv globally through pip `pip install virtualenv`
3. Clone this repo with `git clone https://github.com/sperrys/bostoncongestion.git`
4. Create the virtual environment with `virtualenv -p python3 env`
5. Activate the environment with `source env/bin/activate`
6. Install dependencies with `pip install -r requirements.txt`


### Format 

#### Columns 
* **tmc_code**	
    - TMC in 9 digit format	
    - Traffic Message Channel – this identifies the road segment in question
* **measurement_tstamp**	
    - Date and time in local time (format yy-mm-dd hh:mm:ss.nnn)
    - DOW = ‘Day of Week’
    - CTPS has expanded the ‘measurement_tstamp field in the delivered data into month, day, hour,
and minute fields to simplify querying.
    - The ‘DOW’ field is encoded as an INTEGER: 0 == Monday, 1 == Tuesday, ... etc. ... 5 == Saturday, 6 == Sunday.
     
* **speed**			
    - Speed in mph	
* **average_speed**	
    - Historical average speed for the TMC and time period
* **reference_speed**	
    - Calculated "free flow" speed for the TMC
* **travel_time_minutes**	
    - Current estimate of time to traverse the TMC in minutes
* **confidence_score**	
    - Gives an indication of the source of individual speed values: 
		- 30 indicates real time component, 
		- 20 does not have real time component (historical or prediction values only), 
		- 10 indicates reference speed is used
* **cvalue**			
    - The probability that the speed represents the actual roadway conditions based on trends.  
	- Only present when confidence_score = 30,
	- 0 = low probability 
	- 100 = high probability.


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

