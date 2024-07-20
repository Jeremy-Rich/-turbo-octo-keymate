def award_points(task):
    points = 0
    if task['completed']:
        points += 10
        if task['time_taken'] < task['estimated_time']:
            points += 5
    return points

def complete_task(task):
    points = award_points(task)
    return {"points_awarded": points}

