import gu_rest_api
from gu_rest_api.rest import ApiException
from gu_rest_api.none import NONE_IT


class Driver(object):
    __slots__ = ('client', 'api_instance')

    def __init__(self, configuration=None):
        configuration = configuration if configuration else \
            gu_rest_api.Configuration()
        client = gu_rest_api.ApiClient(configuration)
        self.client = client
        self.api_instance = gu_rest_api.SessionApi(client)

    def session(self, name=None, tags=None, expires=None, allocation=None, ):
        sessionSpec = gu_rest_api.HubSession(name=name, expires=expires, allocation=allocation, tags=tags)
        session_id = self.api_instance.create_session(sessionSpec)
        return Session(self.client, session_id)

    def session_from_id(self, session_id):
        return Session(self.client, session_id)

    @property
    def peers(self):
        peer_api = gu_rest_api.PeerApi(self.client)
        return peer_api.list_peers()

class Session(object):

    def __init__(self, client, session_id):
        self.client = client
        self.rest_api = gu_rest_api.SessionApi(client)
        self.session_id = session_id

    @property
    def id(self):
        return self.session_id

    @property
    def info(self):
        return self.rest_api.get_session(self.session_id)

    @property
    def config(self):
        return self.rest_api.get_config(self.session_id)

    @config.setter
    def write_config(self, new_config):
        return self.rest_api.set_config(self.session_id, new_config)

    def add(self, *peers):
        self.rest_api.add_session_peers(self.session_id, peers)

    def peer(self, node_id):
        return SessionPeer(self.client, self.session_id, node_id)

    def upload(self, f):
        blob_ids = self.rest_api.create_blob(self.session_id, body=f)
        return Blob(self.client, self.session_id, blob_ids[0])

    def new_lob(self):
        blob_id = self.rest_api.create_blob(self.session_id)
        return Blob(self.client, self.session_id, blob_id)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.rest_api.delete_session(self.session_id)


class Blob(object):

    __slots__ = ('_client', '_session_id', '_blob_id', '_api')

    def __init__(self, client, session_id, blob_id):
        self._client = client
        self._api = gu_rest_api.SessionApi(client)
        self._blob_id = blob_id
        self._session_id = session_id

    @property
    def id(self):
        return self._blob_id

    @property
    def uri(self):
        url = '%s/sessions/%s/blobs/%s' % (self._client.configuration.host, self._session_id, self._blob_id)
        return url

    

class SessionPeer(object):
    __slots__ = ('client', 'session_api', 'peer_api', 'session_id', 'node_id')

    def __init__(self, client, session_id, node_id):
        self.client = client
        # TODO: get configuration
        self.peer_api = gu_rest_api.PeerApi(client)
        self.session_api = gu_rest_api.SessionApi(client)
        self.session_id = session_id
        self.node_id = node_id

        print('session_id=', session_id, ',node_id=', node_id)

    @property
    def info(self):
        return self.peer_api.get_peer_details(self.node_id)

    def new_deployment(self, spec):
        return Deployment(self.client, self.session_id, self.node_id,
                          self.peer_api.create_deployment(self.node_id, spec))


class Deployment(object):
    __slots__ = ('client', 'peer_api', 'session_id', 'node_id', 'deploymnet_id', '_open')

    def __init__(self, client, session_id, node_id, deployment_id):
        self.client = client
        self.peer_api = gu_rest_api.PeerApi(client)
        self.session_id = session_id
        self.node_id = node_id
        self.deploymnet_id = deployment_id
        self._open = False

    @property
    def info(self):
        deployments = self.peer_api.list_deployments(self.node_id)
        deploymnet_id = self.deploymnet_id
        return next(deployment for deployment in deployments if deployment.id == deploymnet_id)

    def begin(self):
        return Commands(self)

    def send_commands(self, commands):
        return self.peer_api.update_deployment(self.node_id, self.deploymnet_id, commands= commands)

    def __enter__(self):
        self._open = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._open:
            self.peer_api.drop_deployment(self.node_id, self.deploymnet_id)
            self._open = False


class Commands(object):

    __slots__ = ('_deployment', '_cmds')

    def __init__(self, deployment):
        self._deployment = deployment
        self._cmds = []

    def do_open(self):
        cmd = gu_rest_api.Command(open= NONE_IT)
        self._cmds.append(cmd)
        return self

    def do_close(self):
        cmd = gu_rest_api.Command(close= NONE_IT)
        self._cmds.append(cmd)
        return self


    def do_exec(self, executable, *args):
        cmd = gu_rest_api.Command(_exec= gu_rest_api.ExecCommand(executable= executable, args= args))
        self._cmds.append(cmd)
        return self

    def do_download(self, uri, path):
        cmd = gu_rest_api.Command(download_file=gu_rest_api.DownloadFileCommand(uri=uri, file_path=path))
        self._cmds.append(cmd)
        return self

    def do_upload(self, uri, path):
        cmd = gu_rest_api.Command(upload_file=gu_rest_api.UploadFileCommand(uri=uri, file_path=path))
        self._cmds.append(cmd)
        return self

    def _print(self, client):
        print('cmds=', client.sanitize_for_serialization(self._cmds))

    def send(self):
        cmds = self._cmds
        self._cmds = []
        return self._deployment.send_commands(cmds)


__all__=['Driver']

