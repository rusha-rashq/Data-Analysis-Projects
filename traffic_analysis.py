import json

def read_traffic_data(filename):
    # Read data from JSON file
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def analyze_peak_hours(data):
    # Analyze and find peak traffic hours
    peak_hours = {}
    for entry in data:
        time = entry['time']
        intensity = entry['traffic_intensity']

        if intensity == 'high':
            peak_hours[time] = peak_hours.get(time, 0) + 1

    # Sort by frequency of high intensity
    sorted_peak_hours = sorted(peak_hours.items(), key=lambda x: x[1], reverse=True)
    return sorted_peak_hours

def identify_accident_prone_areas(data):
    # Identify areas with high accident rates
    accident_areas = {}
    for entry in data:
        location = entry['location']
        accidents = entry['accidents']

        if accidents > 0:
            accident_areas[location] = accident_areas.get(location, 0) + accidents

    # Sort by number of accidents
    sorted_accident_areas = sorted(accident_areas.items(), key=lambda x: x[1], reverse=True)
    return sorted_accident_areas

def calculate_average_travel_time(data):
    # Calculate average travel time across routes
    travel_times = {}
    for entry in data:
        location = entry['location']
        travel_time = entry.get('travel_time', 0)

        if location not in travel_times:
            travel_times[location] = {'total_time': 0, 'count': 0}

        travel_times[location]['total_time'] += travel_time
        travel_times[location]['count'] += 1

    average_travel_times = {location: times['total_time'] / times['count']
                            for location, times in travel_times.items()}
    return average_travel_times

def write_report(filename, peak_hours, accident_prone_areas, average_travel_time):
    # Write the findings to a text file
    with open(filename, 'w') as file:
        file.write("Traffic Analysis Report\n")
        file.write("\nPeak Traffic Hours:\n")
        for time, frequency in peak_hours:
            file.write(f"Time: {time}, Frequency: {frequency}\n")

        file.write("\nAccident-Prone Areas:\n")
        for area, accidents in accident_prone_areas:
            file.write(f"Area: {area}, Accidents: {accidents}\n")

        file.write("\nAverage Travel Time per Route:\n")
        for route, avg_time in average_travel_time.items():
            file.write(f"Route: {route}, Average Time: {avg_time:.2f} minutes\n")

def main():
    traffic_data = read_traffic_data("traffic_data.json")
    peak_hours = analyze_peak_hours(traffic_data)
    accident_prone_areas = identify_accident_prone_areas(traffic_data)
    average_travel_time = calculate_average_travel_time(traffic_data)
    write_report("traffic_report.txt", peak_hours, accident_prone_areas, average_travel_time)

if __name__ == "__main__":
    main()
