
# About Project
Change Confidential records like  in CSV file 
* name
* address
* email
* phone 



# install venv and start
```
$ python3 -m venv venv
$ source venv/bin/activate
```


# install moduls and lib
```
pip install -r requirement.txt
```
# run
```
python3 run.py
```

# input 
| "id" | "first_name" | "last_name" | "email"                  | "phone"         | "address"                                        | "city"    | "state" | "country" | "country_code" | "zip_code" | "user_id" |
|------|--------------|-------------|--------------------------|-----------------|--------------------------------------------------|-----------|---------|-----------|----------------|------------|-----------|
| "17" | "Jordan"     | "Ramirez"   | "jordan.ramirez@xyz.com" | "(911)719-8880" | "470 Dennis Points Suite 016 Garyside, CO 34444" | "Sidhi"   |         | "India"   | "IN"           | "488949"   | "1"       |
| "18" | "Kayla"      | "Jones"     | "kayla.jones@xyz.com"    | "(748)872-8106" | "04415 Brian Expressway New Michelle, SD 63926"  |           |         |           |                | "847987"   | "51"      |
| "19" | "Anna"       | "Le"        | "anna.le@xyz.com"        | "(921)850-9267" | "4294 Mccarthy Road Aliport, OK 07890"           | "Katangi" |         | "India"   | "IN"           | "8449844"  | "1"       |


# output
|      |           |            |                          |                 |                                                       |           |    |         |      |           |      |
|------|-----------|------------|--------------------------|-----------------|-------------------------------------------------------|-----------|----|---------|------|-----------|------|
| "17" | "James"   | "Anderson" | "james.anderson@xyz.com" | "(793)777-9254" | "163 Tonya Circle Calvinland, VT 46143"               | "Sidhi"   | "" | "India" | "IN" | "488949"  | "1"  |
| "18" | "Deborah" | "Burke"    | "deborah.burke@xyz.com"  | "(728)892-9540" | "217 Jennifer Hills Suite 414 Peterview, GU 42534"    | ""        | "" | ""      | ""   | "847987"  | "51" |
| "19" | "Brian"   | "Sherman"  | "brian.sherman@xyz.com"  | "(855)714-9560" | "52076 Nicole Course Apt. 482 Andersonport, MP 32858" | "Katangi" | "" | "India" | "IN" | "8449844" | "1"  |
