import random
from datetime import datetime, timedelta
from tabulate import tabulate

def merge_sort_schedule(events):
    if len(events) > 1:
        mid = len(events) // 2
        left_half = events[:mid]
        right_half = events[mid:]

        merge_sort_schedule(left_half)
        merge_sort_schedule(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]["start_time"] < right_half[j]["start_time"]:
                events[k] = left_half[i]
                i += 1
            else:
                events[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            events[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            events[k] = right_half[j]
            j += 1
            k += 1

def generate_time_slots():
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("16:00", "%H:%M")
    slots = []
    while start_time < end_time:
        slots.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=40)
    return slots

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = generate_time_slots()

timetable = [
    {"event": "Math Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Physics Lecture", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Chemistry Lab", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Computer Science Seminar", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "History Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "English Literature", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Biology Lecture", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Physical Education", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Art Workshop", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Music Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Economics Lecture", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Psychology Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Environmental Science", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Business Studies", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Geography Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "French Language", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Spanish Language", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Programming Workshop", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Astronomy Lecture", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Dance Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Robotics Club", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Debate Session", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Drama Rehearsal", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Philosophy Class", "day": random.choice(days), "start_time": random.choice(time_slots)},
    {"event": "Graphic Design Workshop", "day": random.choice(days), "start_time": random.choice(time_slots)},
]


grouped_timetable = {day: [] for day in days}
for event in timetable:
    grouped_timetable[event["day"]].append(event)

for day in days:
    merge_sort_schedule(grouped_timetable[day])


print("Sorted Timetable:")
for day in days:
    print(f"\n{day}:")
    for event in grouped_timetable[day]:
        print(f"  {event['event']} at {event['start_time']}")

table_data = []
for day in days:
    for event in grouped_timetable[day]:
        table_data.append([day, event["event"], event["start_time"]])

print("\nTimetable in Table Format:")
print(tabulate(table_data, headers=["Day", "Event", "Start Time"], tablefmt="grid"))