# Problem 1: Variables and Data Types
print("=== Problem 1 ===") 
market_name ='Balogun Market'
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False
Total_revenue = 25000000 
print('market:'+ market_name + ',Type:'+str(type(market_name)))
print('traders:'+ str(num_traders)+ ',Type:'+str(type(num_traders)))
print('Coordinates:'+str(location_coords)+ ', Type:'+str(type(location_coords)))
print('Open Sundays:',is_open_sundays,', Type:', type(is_open_sundays))
print('Average Daily Revenue per Trader:', str(float(Total_revenue/num_traders)))

# Problem 2: Lists and Basic Operations 
print("=== Problem 2 ===")
host_countries =  ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"] 
host_countries.append('Ivory Coast')
host_countries.insert(1,'Morocco')
host_countries.remove('Senegal')
print('Total number of countries:', len(host_countries))
print('alphabetical order:', sorted(host_countries))
print('every second country:', host_countries [::2])

# Problem 3: Dictionaries
print('===Problem 3 ===')
river_data = { 
"Nile": {"length_km": 6650, "countries": 11}, 
"Congo": {"length_km": 4700, "countries": 9}, 
"Niger": {"length_km": 4180, "countries": 5} 
} 
river_data['zambezi'] = {'length_km':2574, 'countries': 6}
river_data['Niger']['countries'] = 6
print('river names:', list(river_data))
print('Congo flows through', river_data['Congo']['countries'], 'countries')
total_length = sum(river['length_km'] for river in river_data.values())
print('total combined length:', total_length, 'km')

# Problem 4: Loops
print('=== Problem 4===')
# Part A: For Loops
for i in range(1, 11):
    print('7 * ' + str(i)+ ' = '+ str(7* i))
for each_letter in 'AFRICA':
    print(each_letter)
    total= 0
for i in range(1,51):
    if i % 2 == 0:
        total +=i
print(total)
#Part B: While Loop 
i = 20
while i >= 1:
    print(i)
    i = i - 1

i = 501
while i%3 != 0 or i%7 != 0:
    i += 1
print(i)

# Problem 5: Conditional Statements
print('=== Problem 5===')
def classify_rainfall(mm):
    if mm > 300:
        return 'Flood Risk'
    elif 200 <= mm <= 300:
        return 'Heavy Rain'
    elif 100 <= mm <= 199:
        return 'Moderate Rain'
    elif 1 <= mm <= 99:
        return 'Light Rain'
    elif mm == 0:
        return 'Dry'
    else:
        return 'Invalid Rainfall Value'
print('350mm:', classify_rainfall(350))
print('250mm:', classify_rainfall(250))
print('150mm:', classify_rainfall(150))
print('50mm:', classify_rainfall(50))
print('0mm:', classify_rainfall(0))

# Problem 6: Functions
print('=== Problem 6===')
# Part A: Basic Function
def calculate_exchange(amount, rate):
       return float(amount * rate)
print('Expected result:', calculate_exchange(100, 1580))
# Part B: Function with Default Parameters
def format_price(amount, currency = "NGN"):
     return f'{currency} {amount:,}'
print(format_price(5000))
print(format_price(200, "GHS"))
# Part C: Function Returning Multiple Values
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)
    return lowest, highest, average
score_list = [55, 72, 88, 61, 94, 47, 79]
lowest, highest, average = analyze_scores(score_list)
print('lowest score:', lowest)
print('highest score:', highest)
print('average score:', average)
