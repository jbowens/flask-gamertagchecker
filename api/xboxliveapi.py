import httplib, urllib, xml.etree.ElementTree

"""
A lightweight wrapper around the Xbox Live Developer Community
program API.

@author jbowens
"""
class XboxLiveApi(object):

    api_guid = None

    def __init__(self):
        self.api_guid = 'EF60077C-336D-4eca-95CD-3F5BD7129142'

    def _raw_gamercard_output(self, gamertag):
        conn = httplib.HTTPConnection('feeds.xbox.com', 80, timeout=5)
        path = '/publicgamercardfeed.ashx?gamertag=' + urllib.quote_plus(gamertag)
        conn.request('GET', path, None, {'Referer': 'http://' + self.api_guid})
        resp = conn.getresponse()
        data = resp.read()
        return data

    def _gamercard_xml_tree(self, gamertag):
        data = self._raw_gamercard_output(gamertag)
        root = xml.etree.ElementTree.fromstring(data)
        return root

    def is_gamertag_taken(self, gamertag):
        """
        Queries the Xbox Live api and returns whether or not the given
        gamertag is currently in use.
        """
        root = self._gamercard_xml_tree(gamertag)
        output_gamertag = root.get('gamertag')
        return output_gamertag != '??????'

api = XboxLiveApi()
print api.is_gamertag_taken('Chiddy Bang')
