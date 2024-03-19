def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge
   
def batch_badge_creator(names):
    badge_list = []
    for person in names:
        badge_list.append(f"Hello, my name is {person}.")
    return badge_list

def assign_rooms(names):
    index = 0
    rm_assignments = []
    
    for person in names:
        index += 1
        rm_assignments.append(f"Hello, {person}! You'll be assigned to room {index}!")
    return rm_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room in room_assignments:
        print(room)
