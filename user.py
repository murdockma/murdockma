class user:
  
  def __init__(self, path, user):
    self.path = path
    self.user = user
    
  def __eq__(self, other):
    return self.path == other.path and self.user == other.user
  
  def __hash__(self):
    return ('The hash is:')
  
  return str(hash((self.path, self.user)))
  
