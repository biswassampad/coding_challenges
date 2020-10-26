def main():
    crew_id = int(input("get the crewId"))
    job_id = int(input("get the task id"))
    distance = getMinCost(crew_id,job_id)
    print('success')


def getMinCost(crew_id,job_id):
    distance = job_id - crew_id
    return distance
if __name__ == "__main__":
    main()