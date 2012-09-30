import transmissionrpc

def list_torrents():
  tc = transmissionrpc.Client('127.0.0.1')
  result = []

  for key in tc.list():
    torrent = tc.info(key)[1]
    result.append({
      'name': torrent.name,
      'key': key,
      'progress': torrent.progress,
      'eta': torrent.format_eta(),
      'status': torrent.status,
      'hashString': torrent.hashString,
      'files': torrent.files()
    })

  return result
