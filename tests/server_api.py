import requests

link_to_server = 'http://qainterview.cogniance.com/candidates'

def get_all_candidates():
    return requests.get(link_to_server)

def get_candidate_by_id(candidate_id):
    return requests.get(link_to_server + '/' + str(candidate_id))

def add_candidate(candidate_name, candidate_position):
    payload = {'name': str(candidate_name), 'position': str(candidate_position)}
    return requests.post(link_to_server, json=payload)

def delete_candidate_by_id(candidate_id):
    return requests.delete(link_to_server + '/' + str(candidate_id))
