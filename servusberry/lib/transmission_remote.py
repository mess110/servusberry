import transmissionrpc

def list_torrents():
  tc = transmissionrpc.Client('localhost', 9091)
  result = {}

  for key in tc.list():
    torrent = tc.info(key)[1]
    result[key] = {
      'name': torrent.name,
      'progress': torrent.progress,
      'eta': torrent.format_eta(),
      'status': torrent.status,
      'files': torrent.files()
    }

  return result
