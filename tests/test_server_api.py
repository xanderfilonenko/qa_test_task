import unittest
import requests
import random
import re
import server_api

def get_all_ids():
    candidates = server_api.get_all_candidates().text
    return re.findall('"id": (.+?),', candidates)

def get_random_candidate_id():
    return random.choice(get_all_ids())

class TestServerApi(unittest.TestCase):
    def test_get_all_candidates_response(self):
        self.assertEqual(200, server_api.get_all_candidates().status_code)

    def test_get_candidate_by_id_response(self):
        candidate_id = get_random_candidate_id()
        self.assertEqual(200, server_api.get_candidate_by_id(candidate_id).status_code)

    def test_add_candidate_response(self):
        candidate_name = "Name_"
        candidate_position = "Position_"
        # Positive case
        self.assertEqual(201, server_api.add_candidate(candidate_name, candidate_position).status_code)
        # Case when header is absent
        payload = {'name': str(candidate_name), 'position': str(candidate_position)}
        self.assertEqual(400, requests.post(server_api.link_to_server, data=payload).status_code)
        # Case when name is absent
        payload = {'position': str(candidate_position)}
        self.assertEqual(400, requests.post(server_api.link_to_server, json=payload).status_code)

    def test_delete_candidate_response(self):
        candidate_id = get_random_candidate_id()
        self.assertEqual(200, server_api.delete_candidate_by_id(candidate_id).status_code)

    def test_add_candidate_get_all_candidates_operations(self):
        candidate_name = 'Name_' + str(random.randint(0, 1000))
        candidate_position = 'Position_' + str(random.randint(0, 1000))
        # Get number of candidates
        number_of_candidates = len(get_all_ids())
        # Add test candidate
        server_api.add_candidate(candidate_name, candidate_position)
        all_candidates = server_api.get_all_candidates().text
        # Check that our candidate was added
        self.assertTrue(all_candidates.find(candidate_name) > 0 and all_candidates.find(candidate_position) > 0)
        # Check that number of candidates was increased
        self.assertTrue(number_of_candidates < len(get_all_ids()))

    def test_delete_candidate_operation(self):
        candidate_id = get_random_candidate_id()
        server_api.delete_candidate_by_id(candidate_id)
        # Check that removed id is not in the list
        self.assertFalse(candidate_id in get_all_ids())

    def test_get_candidate_by_id_operation(self):
        candidate_id = get_random_candidate_id()
        candidate = server_api.get_candidate_by_id(candidate_id).text
        # Check that we get candidate with same id
        self.assertTrue(candidate_id == re.search('"id": (.+?),', candidate).group(1), 'Incorrect candidate is shown')

if __name__ == '__main__':
    unittest.main()
