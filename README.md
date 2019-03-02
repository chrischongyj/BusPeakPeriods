# BusPeakPeriods
To illustrate the daily volume of passengers on buses in Singapore so that commuters can plan a comfortable commute.

Motivation: During peak periods, buses get too full to the point where drivers just skip a stop. This project aims to educate commuters about timings when buses are extremely packed (little to no standing space) so that they may plan their commute better.

Tools we are going to be using:
1. Python
2. Visual Studio Code
3. Git
4. LTA DataMall API
5. Google, our saviour 



============
Day One:

Completed:
1. Querying all bus services and their Load for a specified bus stop number

Learning lessons:
1. I forced push my local repo to Github without pulling my existing README first, so its lost. This is my second attempt at a README.
2. Requests has two parameters that is useful in this case, params and headers.
3. Json library for 'loads' (converts JSON to Python) and 'dumps' method (Python to JSON)

To do:
1. Extract data from API JSON response (SOLVED)
2. Figure how to extract all BusNo data using BusStopNo
3. Write data on excel and re-run code every minute to update excel
4. Continuously run script for a week to collect data and find out the daily average of the busiest peak periods (Might need cloud hosting)
5. Enquire if able to extract past data? Because we can only extract live data, so we need to do Step 4.

Every minute there will be data for next 3 buses. We might only need to look at Next Bus 1. 





