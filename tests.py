#!/usr/bin/env python
import unittest2
import requests
from mock import patch
from requests.exceptions import RequestException, Timeout, ConnectionError
from client_tweet import ClientTweet, BadStatus

CONN_EXCEPTIONS = [RequestException, Timeout, ConnectionError]

@patch.object(requests, 'get')
class GetTweetsTest(unittest2.TestCase):

    def test_requests_raise(self, get):
        for exception in CONN_EXCEPTIONS:
            with self.assertRaises(exception):
                get.side_effect = exception
                cli = ClientTweet()
                cli.get_tweets()

    def test_status_code(self, get):
        with self.assertRaises(BadStatus):
            get.return_value.status_code = 403
            cli = ClientTweet()
            cli.get_tweets()

    def test_ok(self, get):
        get.return_value.status_code = 200
        cli = ClientTweet()
        gtweets = cli.get_tweets()
        self.assertEqual(gtweets.status_code, 200)

if __name__ == '__main__':
    unittest2.main()
